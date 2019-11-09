from github import Github, GithubException, enable_console_debug_logging
from dotenv import load_dotenv
from os import getenv
import csv
import time
load_dotenv()

TIMEOUT = 30
REQUEST_TIME_TO_COMPLETE_TIMEOUT = 30
MAX_NO_OF_PAGES = 100
GITHUB_TOKEN = getenv("GITHUB_TOKEN")


def saveRepos(repos, contents, name="repo"):
    data = []
    keys = ["name", "id", "description", "language", "open_issues",
            "stargazers_count", "topics", "watchers_count"]
    methods = ["get_readme"]
    index = 0
    for repo in repos:
        print("saving >>> {}".format(repo.name))

        readme = ""
        try:
            readme = repo.get_readme().content
        except GithubException as e:
            pass

        dictionary = dict([(k, fixEncoding(getattr(repo, k))) for k in keys])
        dictionary["readme"] = readme
        dictionary["config"] = contents[index]

        data.append(dictionary)

        index += 1
    return data


def writeToCsv(data, name):
    if len(data) >= 1:
        print("saving: data")
        field = list(data[0].keys())

        with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:

            writer = csv.DictWriter(
                csvfile, fieldnames=field, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for d in data:
                writer.writerow(d)
    else:
        print("no data found")


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

        if "," in file.content:
            print("ERROR")
            print(file.content)
            print("--------------------")

        contents.append(file.content)
    return repos, contents


def getConfigStuff(search, name):
    g = Github(GITHUB_TOKEN, timeout=REQUEST_TIME_TO_COMPLETE_TIMEOUT)
    searches = 0

    print("----------------------------------------")
    print("getting data for: {} will take around 2mins".format(name))
    name += time.strftime("%X").replace(":", "_")
    temp = g.search_code(search)
    index = 3
    page = temp.get_page(index)
    while len(page) >= 1 and index < MAX_NO_OF_PAGES and searches < 1000:
        g = Github(GITHUB_TOKEN, timeout=REQUEST_TIME_TO_COMPLETE_TIMEOUT)
        print("getting page: {}".format(index))
        repos, content = getReposFromFiles(page)

        if len(repos) > 1:
            print(
                "sleeping for a few seconds just not to abuse the rate limiting too much")
            time.sleep(TIMEOUT)
            writeToCsv(saveRepos(repos, content), name)
        else:
            print("no data found")

        index += 1
        searches += len(repos)
        page = temp.get_page(index)
        print("currently {}% complete".format(searches / 1000))
        print("sleeping for: {}s to avoid 403 errors due to rate limiting".format(TIMEOUT))
        time.sleep(TIMEOUT)
    print("finished going through {} pages of results and got {} results".format(
        index, searches))


def foo(g, repo):
    # TODO: make me global!!! as its a read only constant that needs to have global access to avoid to fun stuff
    paths = {
        "travis": {"file": "single", "path": ".travis.yml"},
        "gitlab": {"file": "single", "path": ".gitlab-ci.yml"},
        "jenkinsPipeline": {"file": "single", "path": "JenkinsFile"},
        "cirrus": {"file": "single", "path": ".cirrus.yml"},  # file endings .yml .yaml
        "github": {"file": "dir", "path": ".github/workflows/"},
        "cds": {"file": "dir", "path": ".cds"},  # file endings .yml .yaml
        "azure": {"file": "single", "path": "azure-pipelines.yml"}
    }

    path_results = {}
    for key in paths.keys():
        print("searching for {} search style: {} and query: {}".format(key, paths.get(key).get("file"), paths.get(key).get("path")))

        if paths.get(key).get("file") == "single":
            try:
                temp = repo.get_contents(paths.get(key).get("path"))
                if temp is not None:
                    path_results[key] = [temp.content]
            except GithubException as e:
                pass
        else:
            try:
                path_results[key] = [f.content for f in repo.get_dir_contents(paths.get(key).get("path")) if f is not None and (f.name.endswith(".yaml") or f.name.endswith(".yml"))]
            except GithubException as e:
                pass

        time.sleep(2)

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
    g = Github(GITHUB_TOKEN, timeout=REQUEST_TIME_TO_COMPLETE_TIMEOUT, per_page=100)
    search = "stars:{}..{}".format(stars_start, stars_end)  # TODO: add in stars
    print("----------------------------------------")

    temp = g.search_repositories(search)
    pageination_page = 0
    page = temp.get_page(pageination_page)
    searches = 0
    while len(page) >= 1 and pageination_page < MAX_NO_OF_PAGES and searches < 1000:
        file_name = name + time.strftime("%X").replace(":", "_") + "stars{}{}".format(stars_start, stars_end)

        g = Github(GITHUB_TOKEN, timeout=REQUEST_TIME_TO_COMPLETE_TIMEOUT, per_page=100)

        print("getting page: {}".format(pageination_page))

        saveData = saveRepos(page, ["" for i in range(len(page))], name)

        results = []
        for repo in page:
            print("querying:" + repo.name)
            results.append(foo(g, repo))

        print("got all the data from the on the repository now sleeping for a bit")
        time.sleep(TIMEOUT)

        data = []
        for i in range(len(saveData)):
            data.append({**saveData[i], **results[i]})

        paths = {
            "travis": {"file": "single", "path": ".travis.yml"},
            "gitlab": {"file": "single", "path": ".gitlab-ci.yml"},
            "jenkinsPipeline": {"file": "single", "path": "JenkinsFile"},
            "cirrus": {"file": "single", "path": ".cirrus.yml"},  # file endings .yml .yaml
            "github": {"file": "dir", "path": ".github/workflows/"},
            "cds": {"file": "dir", "path": ".cds"},  # file endings .yml .yaml
            "azure": {"file": "single", "path": "azure-pipelines.yml"}
        }

        for k in paths.keys():
            for i in range(10):
                if data[0].get("{}{}".format(k, i)) is None:
                    data[0]["{}{}".format(k, i)] = ""

        writeToCsv(data, name)

        searches += len(saveData)
        pageination_page += 1

        page = temp.get_page(pageination_page)

        print("sleeping for: {}s to avoid 403 errors due to rate limiting".format(TIMEOUT))
        print("progress >>> {}%".format((searches / 1000) * 100))
        time.sleep(TIMEOUT)

    print("finished")
    print("finished going through {} pages of results and got {} results".format(pageination_page, searches))


def main():
    if GITHUB_TOKEN is None:
        print("place a github token in the .env file")
    else:
        # getReposStuff("TEST", 9000, 10000)
        for i in range(1000, 99999, 1000):
            getReposStuff("TEST20", i, i + 1000)
            print("sleeping for a minute to not abuse time limits too much")
            # TODO: maths can only have 5000 requests per hour
            time.sleep(60)

        # NOTE: if this is all doesn't work then parsing readme files of popular repositories will be the way to go

        # so we get a 1000 search results for each search
        # writeToCsv([{"a":"cat,fish,dog"}], "test.csv")
        # getConfigStuff("extension:.yml filename:.travis.yml", "allTheTravis")
        # getConfigStuff("extension:.yml path:.circle/ filename:config.yml", "allTheCircles")
        # getConfigStuff("extension:.yml path:.github/workflows name", "githubActions")
        # getConfigStuff("extension:.yml filename:.gitlab-ci.yml", "gitlab")
        # getConfigStuff("filename:JenkinsFile", "jenkinsPipeline")
        # getConfigStuff( "filename:.cirrus.yml", "cirrus") # cirrus https://cirrus-ci.org/examples/
        # getConfigStuff("path:.cds version", "cds") # https://ovh.github.io/cds/docs/tutorials/init_workflow_with_cdsctl/ more CD than CI though
        # team city got to last page before it died
        # getConfigStuff("path:.teamcity version", "teamcity") # note the content of the configuration will be xml and it will be messy most likely as team city has lots of files for all the things

        # got too 48%
        # TODO: triple check this is how it works?? as it could just be any .yml file however it will do the job and there should be around 50,000 results
        # getConfigStuff("filename:azure-pipelines.yml", "azure")

        # note: GoCd seems to be used so little that I can't find any good examples of it its config
        # combined with the fact that they allow .json and .yml ah!


if __name__ == "__main__":
    main()
