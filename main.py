from github import Github, GithubException
from dotenv import load_dotenv
from os import getenv
from csvReader import writeToCsv
import time
import config
import traceback
load_dotenv()

FILE_NAME = getenv("FILE_NAME", "penguins")
NO_PAGES = int(getenv("NO_PAGES", 100))
REQUEST_TIMEOUT = int(getenv("REQUEST_TIMEOUT", 120))
ITERATION_DIFFERENCE = int(getenv("ITERATION_DIFFERENCE", 10))
ITERATION_START = int(getenv("ITERATION_START", 1000))
ITERATION_END = int(getenv("ITERATION_END", 999999))
NUMBER_OF_POTENTAIL_FILES = int(getenv("NUMBER_OF_POTETNAIL_FILES", 24))
RATE_LIMITING = getenv("RATE_LIMITING", 1000)
TIMEOUT = int(getenv("TIMEOUT", 30))
REQUEST_TIME_TO_COMPLETE_TIMEOUT = getenv("REQUEST_TIME_TO_COMPLETE_TIMEOUT", 120)
MAX_NO_OF_PAGES = int(getenv("MAX_NO_OF_PAGES", 9))  # zero indexed fun stuff
GITHUB_TOKEN = getenv("GITHUB_TOKEN")

def saveRepos(repos, contents):
    data = []

    # NOTE: due to this: https://developer.github.com/changes/2012-09-05-watcher-api/
    # subscribers count is used to demonstrate the number of people watching the repository. Watchers etc. is now for
    # the star count.

    keys = ["name", "id", "description", "language", "open_issues",
            "stargazers_count", "topics", "subscribers_count", "fork", "forks_url"]
    index = 0
    for repo in repos:
        print("saving >>> {}".format(repo.name))

        readme = ""
        try:
            readme = repo.get_readme().content
        except GithubException as e:
            pass

        dictionary = {}
        for k in keys:
            # this deals with one recorded case of a 502 error when doing getting the attributes from github
            # in doing so this makes it more versatile and allows for better error recovery and recording of the issues
            try:
                dictionary[k] = fixEncoding(getattr(repo, k))
            except GithubException as e:
                print("---------------")
                print("github exception happened when searching for: {} in {}".format(k, repo.name))
                traceback.print_tb(e.__traceback__)
                print("---------------")
                dictionary[k] = ""

        dictionary["readme"] = readme
        dictionary["config"] = contents[index]
        dictionary["watch"] = repo.watchers_count

        data.append(dictionary)

        index += 1
    return data


def fixEncoding(value):
    if isinstance(value, str):
        return value.encode("utf8")
    else:
        return value


def getReposFromFiles(files):
    repos = []
    contents = []
    for file in files:
        repos.append(file.repository)
        print("reading >>> {}".format(repos[len(repos) - 1].name))

        contents.append(file.content)
    return repos, contents


def getContentsForYaml(repo, path, isjenkins):
    # jenkins is the only configuration type that isn't yaml so we do validation for all the yaml files that
    # they are actually legit files. Then for jenkins we let it be jenkins :)
    try:
        temp = repo.get_contents(path)
        if isinstance(temp, list):
            # we slice here to avoid having extra files of configuration over 24
            # 24 atm is just a magic number as we should ideally never get above that
            return [f.content for f in repo.get_contents(path) if
                    f is not None and (f.name.endswith(".yaml") or f.name.endswith(".yml") and not isjenkins)][:NUMBER_OF_POTENTAIL_FILES]
        else:
            return [temp.content]
    except GithubException as e:
        return []


def process_repo_ci_files(repo):

    path_results = {}
    for key in config.PATHS.keys():
        # NOTE: files with the same name as directories will currently break
        # there has been issue created on the repo based on this by someone else 2days ago!
        # also this api call will get depracted which might fix this issue
        # https://github.com/PyGithub/PyGithub/issues/1283
        # attempting to hotfix by copying in the changes into the library to see if that will work
        # NOTE: this will require hotfixing every time it is installed!!!! (or deployed)

        # get_contents -> list or single ContentFile depending on what gets returned
        temp = getContentsForYaml(repo, config.PATHS.get(key), "jenkins" in key)
        if temp:
            path_results[key] = temp

        time.sleep(1.5)

    if len(path_results.keys()) == 0:
        print("found no results")
        return {}

    result = {}
    for k in path_results.keys():
        for i in range(len(path_results[k])):
            result["{}{}".format(k, i)] = path_results[k][i]

    if len(result.keys()) > 1:
        print("found multiple results potentailly for multiple filse")
    return result


def getReposStuff(name, stars_start, stars_end):
    g = Github(GITHUB_TOKEN, timeout=REQUEST_TIME_TO_COMPLETE_TIMEOUT, per_page=NO_PAGES)
    search = "stars:{}..{}".format(stars_start, stars_end)  # TODO: add in stars
    print("----------------------------------------")

    pages = g.search_repositories(search)
    pageination_page = 0
    page = pages.get_page(pageination_page)
    searches = 0
    while len(page) >= 1 and pageination_page < MAX_NO_OF_PAGES and searches < RATE_LIMITING:
        file_name = name + time.strftime("%X").replace(":", "_") + "stars{}{}".format(stars_start, stars_end)

        print("getting page: {}".format(pageination_page))

        saveData = saveRepos(page, ["" for i in range(len(page))])

        results = []
        for repo in page:
            print("querying:" + repo.name)
            results.append(process_repo_ci_files(repo))

        print("got all the data from the on the repository now sleeping for a bit")
        time.sleep(TIMEOUT)

        data = []
        for i in range(len(saveData)):
            data.append({**saveData[i], **results[i]})

        for k in config.PATHS.keys():
            for i in range(NUMBER_OF_POTENTAIL_FILES):
                if data[0].get("{}{}".format(k, i)) is None:
                    data[0]["{}{}".format(k, i)] = ""

        writeToCsv(data, file_name)

        searches += len(saveData)
        pageination_page += 1
        if searches < RATE_LIMITING:
            page = pages.get_page(pageination_page)
        else:
            print("reached limit for search results")

        print("sleeping for: {}s to avoid 403 errors due to rate limiting".format(TIMEOUT))
        print("progress >>> {}%".format((searches / RATE_LIMITING) * NO_PAGES))
        time.sleep(TIMEOUT)

    print("finished")
    print("finished going through {} pages of results and got {} results".format(pageination_page, searches))


def main_scraper():
    for i in range(ITERATION_START, ITERATION_END, ITERATION_DIFFERENCE):
        getReposStuff(FILE_NAME, i, i + ITERATION_DIFFERENCE)
        print("sleeping for a minute to not abuse time limits too much")
        # TODO: maths can only have 5000 requests per hour
        time.sleep(60)


def main():
    if GITHUB_TOKEN is None:
        print("place a github token in the .env file")
    else:
        main_scraper()


if __name__ == "__main__":
    main()
