"""
Searches for files based on the config.py either in directories or single files against the github api v3.

TODO:
- rate limiting (properly to optimise speed!)


"""

from github import Github, GithubException, ContentFile
from github.GithubException import UnknownObjectException, BadAttributeException, IncompletableObject, \
    BadUserAgentException, RateLimitExceededException
from dotenv import load_dotenv
from os import getenv
import csvReader
import time
import config
import logging
from sys import argv

if len(argv) == 2:
    load_dotenv(argv[1])
else:
    load_dotenv()

# sets up the logging level
LOG_LEVEL = getenv("LOG_LEVEL", "").lower()
if LOG_LEVEL == "info":
    LOG_LEVEL = logging.INFO
elif LOG_LEVEL == "warning":
    LOG_LEVEL = logging.WARNING
elif LOG_LEVEL == "debug":
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO

logging.basicConfig(
    filename="{}.log".format(getenv("LOG_FILE", "logfile")),
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%H:%M:%S"
)


class EmptyRepository(Exception):
    """
    repo.get_contents can cause a GithubException where the repository is empty. Therefore we want to have specified
    type for this kind of exception. In order that we can handle the exception instead of dealing with parsing a
    GithubException whenever this is the issue.
    """


FILE_NAME = getenv("FILE_NAME", "penguins")
NO_PAGES = int(getenv("NO_PAGES", 100))
REQUEST_TIMEOUT = int(getenv("REQUEST_TIMEOUT", 120))
ITERATION_DIFFERENCE = int(getenv("ITERATION_DIFFERENCE", 10))
ITERATION_START = int(getenv("ITERATION_START", 1000))
ITERATION_END = int(getenv("ITERATION_END", 999999))
NUMBER_OF_POTENTAIL_FILES = int(getenv("NUMBER_OF_POTETNAIL_FILES", 24))
NUMBER_OF_POTENTAIL_FILES_FOR_SINGLE_FILES = int(getenv("NUMBER_OF_POTENTAIL_FILES_FOR_SINGLE_FILES", 5))
RATE_LIMITING = getenv("RATE_LIMITING", 1000)
TIMEOUT = int(getenv("TIMEOUT_FOR_SEARCH", 30))
TIMEOUT_FOR_SEARCH = int(getenv("TIMEOUT", 1))
MAX_NO_OF_PAGES = int(getenv("MAX_NO_OF_PAGES", 9))  # zero indexed fun stuff
GITHUB_TOKEN = getenv("GITHUB_TOKEN")

# NOTE: due to this: https://developer.github.com/changes/2012-09-05-watcher-api/
# subscribers count is used to demonstrate the number of people watching the repository. Watchers etc. is now for
# the star count.
REPO_KEYS = ["name", "id", "description", "language", "open_issues",
             "stargazers_count", "topics",
             "subscribers_count", "fork", "forks_url"]

logging.info(f"file name {FILE_NAME}, no page {NO_PAGES}, request timeout {REQUEST_TIMEOUT}, "
             f"iteration f{ITERATION_START} - f{ITERATION_END} incrementing by f{ITERATION_DIFFERENCE}")
logging.info(f"no of potential config files for github actions: f{NUMBER_OF_POTENTAIL_FILES}, "
             f"rate limiting f{RATE_LIMITING}, default timeout: f{TIMEOUT}, max no. of pages f{MAX_NO_OF_PAGES}")
logging.debug(f"github token {GITHUB_TOKEN}")


def check_for_empty_repo(repo, path, count=0):
    try:
        return repo.get_contents(path)
    except GithubException as e:
        if e.status == 404 and "This repository is empty." in e.data:
            raise EmptyRepository()
        elif e.status >= 500 and e.status < 600 and count < 5:
            # note: this will cause a horrible stacktrace error
            logging.error("first 50 characters: " + e.data[:50])
            return check_for_empty_repo(repo, path, count+1)
        else:
            raise e


def save_repo(repo, content):
    logging.info("saving >>> {}".format(repo.name))

    readme = ""
    try:
        readme = repo.get_readme().content
    except UnknownObjectException:
        pass

    dictionary = {}
    for k in REPO_KEYS:
        # this deals with one recorded case of a 502 error when doing getting the attributes from github
        # in doing so this makes it more versatile and allows for better error recovery and recording of the issues
        try:
            dictionary[k] = fixEncoding(getattr(repo, k))
        except UnknownObjectException as e:
            logging.error("---------------")
            logging.error("github exception happened when searching for: {} in {}".format(k, repo.name))
            logging.error("---------------")
            dictionary[k] = ""
        except BadAttributeException as e:
            logging.error("---------------")
            logging.error("github exception happened when searching for: {} in {}".format(k, repo.name))
            logging.error("---------------")
            dictionary[k] = ""
        except IncompletableObject as e:
            logging.error("---------------")
            logging.error("github exception happened when searching for: {} in {}".format(k, repo.name))
            logging.error("---------------")
            dictionary[k] = ""
        except BadUserAgentException as e:
            logging.error("---------------")
            logging.error("github exception happened when searching for: {} in {}".format(k, repo.name))
            logging.error("---------------")
            dictionary[k] = ""

    dictionary["readme"] = readme
    dictionary["config"] = content
    dictionary["watch"] = repo.watchers_count

    return dictionary


def save_repos(repos, contents):
    data = []
    index = 0
    for repo in repos:
        data.append(save_repo(repo, contents[index]))
        index += 1
    return data


def fixEncoding(value):
    if isinstance(value, str):
        return value.encode("utf8")
    else:
        return value

def get_yaml_from_directory(repo, path):
    """
    @param repo github.Repository object
    @param path get all the files in this path

    returns an array of up too NUMBER_OF_POTENTIAL_FILES that match the search criteria and are yaml
    """
    try:
        temp = repo.get_contents(path)
        if isinstance(temp, list):
            # we slice here to avoid having extra files of configuration over 24
            # 24 atm is just a magic number as we should ideally never get above that
            return [(f.content, f.name) for f in repo.get_contents(path) if
                    f is not None and (
                            f.name.endswith(".yaml")
                            or f.name.endswith(".yml")
                            or f.name.endswith(".xml")
                            or f.name.endswith(".kts"))][:NUMBER_OF_POTENTAIL_FILES]
        else:
            return [(temp.content, temp.name)]
    except UnknownObjectException:
        return []
    except EmptyRepository:
        return []



def process_repo_ci_files(repo):
    # NOTE: files with the same name as directories will currently break
    # there has been issue created on the repo based on this by someone else 2days ago!
    # also this api call will get depracted which might fix this issue
    # https://github.com/PyGithub/PyGithub/issues/1283
    # attempting to hotfix by copying in the changes into the library to see if that will work
    # NOTE: this will require hotfixing every time it is installed!!!! (or deployed)

    path_results = {}
    files = {}
    try:
        for root_file in check_for_empty_repo(repo, "."):
            file_name = root_file.name.lower()
            if files.get(file_name) is not None:
                logging.info("duplicate file in root directory found: {}".format(file_name))
            files[file_name] = root_file
    except UnknownObjectException:
        pass
    except EmptyRepository:
        pass

    for key in config.PATHS.keys():
        search_results = []

        if key in config.PATHS_MULTIPLE:
            search_results = get_yaml_from_directory(repo, config.PATHS.get(key))  # [(content, name)]
        else:
            result = None
            if "jenkins" in key:
                result = files.get(config.PATHS.get(key))
            else:
                for search in [f".{key}.yml", f".{key}.yaml", f"{key}.yml", f"{key}.yaml"]:
                    if search in files.keys():
                        result = files.get(search)

            if result is not None:
                search_results = [(result.content, result.name)]

        for i in range(len(search_results)):
            path_results["{}{}".format(key, i)] = search_results[i][0]
            path_results["{}{}_file".format(key, i)] = search_results[i][1]

        time.sleep(TIMEOUT_FOR_SEARCH)

    if len(path_results.keys()) == 0:
        logging.info("found no results")
        return {}

    if path_results:
        logging.info("found configuration files for: {}".format(path_results.keys()))

    return path_results


def tidyup_dictinary_keys(data):
    for k in config.PATHS.keys():
        number_of_configs = 0
        if "jenkins" in k:
            number_of_configs = 1
        elif k in config.PATHS_MULTIPLE:
            number_of_configs = NUMBER_OF_POTENTAIL_FILES
        else:
            number_of_configs = NUMBER_OF_POTENTAIL_FILES_FOR_SINGLE_FILES

        for i in range(number_of_configs):
            if data[0].get("{}{}".format(k, i)) is None:
                data[0]["{}{}".format(k, i)] = ""

            if data[0].get("{}{}_file".format(k, i)) is None:
                data[0]["{}{}_file".format(k, i)] = ""

    return data


def getReposStuff(name, stars_start, stars_end):
    g = Github(GITHUB_TOKEN, timeout=REQUEST_TIMEOUT, per_page=NO_PAGES)
    search = "stars:{}..{}".format(stars_start, stars_end)
    logging.info("----------------------------------------")

    pages = g.search_repositories(search)
    pageination_page = 0
    page = pages.get_page(pageination_page)
    searches = 0
    while len(page) >= 1 and pageination_page < MAX_NO_OF_PAGES and searches < RATE_LIMITING:
        file_name = name + time.strftime("%X").replace(":", "_") + "stars{}{}".format(stars_start, stars_end)

        logging.info("getting page: {}".format(pageination_page))

        saveData = save_repos(page, ["" for i in range(len(page))])

        results = []
        for repo in page:
            logging.info("querying:" + repo.name)
            results.append(process_repo_ci_files(repo))

        logging.info("got all the data from the on the repository now sleeping for a bit")
        time.sleep(TIMEOUT)

        data = []
        for i in range(len(saveData)):
            data.append({**saveData[i], **results[i]})

        data = tidyup_dictinary_keys(data)

        csvReader.writeToCsv(data, file_name)

        searches += len(saveData)
        pageination_page += 1
        if searches < RATE_LIMITING:
            page = pages.get_page(pageination_page)
        else:
            logging.info("reached limit for search results")

        logging.info("sleeping for: {}s to avoid 403 errors due to rate limiting".format(TIMEOUT))
        logging.info("progress >>> {}%".format((searches / RATE_LIMITING) * NO_PAGES))
        time.sleep(TIMEOUT)

    logging.info("finished")
    logging.info("finished going through {} pages of results and got {} results".format(pageination_page, searches))


def get_config_from_ids(name, ids):
    """
    @param name str
    @param ids [int]
    """
    g = Github(GITHUB_TOKEN, timeout=REQUEST_TIMEOUT, per_page=NO_PAGES)
    file_name = name
    searches = 0
    len_ids = len(ids)
    data = []
    for repo_id in ids:
        logging.info("getting repo: {}".format(repo_id))
        repo = None
        try:
            repo = g.get_repo(repo_id)  # 1 request
        except UnknownObjectException:
            pass

        if repo:
            try:
                data.append({
                    **save_repo(repo, ""),  # around about 12 requests
                    **process_repo_ci_files(repo)  # 7 requests
                })
            except RateLimitExceededException as e:
                logging.error(e.__str__())
                logging.info(f"searches at: {searches} {repo_id} {data}")
                logging.info("error occured sleeping for 2 mins to allow for correction")
                time.sleep(120)

        if searches == 10 and data:
            data = tidyup_dictinary_keys(data)

            csvReader.writeToCsv(data, file_name)
            data = []
            time.sleep(TIMEOUT)
            logging.info("sleeping for: {}s to avoid 403 errors due to rate limiting".format(TIMEOUT))
            logging.info("progress >>> {}%".format((searches / len_ids) * 100))
        searches += 1

        time.sleep(TIMEOUT)

    logging.info("finished")


def main_scraper():
    for i in range(ITERATION_START, ITERATION_END, ITERATION_DIFFERENCE):
        getReposStuff(FILE_NAME, i, i + ITERATION_DIFFERENCE)
        logging.info("sleeping for a minute to not abuse time limits too much")
        # TODO: maths can only have 5000 requests per hour
        time.sleep(60)

    logging.info("FINISHED!!!!!! woo now time for human to stop sleeping...")


def main_rerun_scrape():
    # name, id so index has to be 1 based on REPO_KEYS
    ids = [int(line[1]) for line in csvReader.readfile_low_memory("combined.csv")[1:]]
    logging.info("got {} ids to scrape through".format(len(ids)))
    get_config_from_ids(FILE_NAME, ids)


def test_cases():
    logging.info("test cases...")
    ids = [106607705, 155825745]
    get_config_from_ids(FILE_NAME, ids)

def main():
    if GITHUB_TOKEN is None:
        logging.info("place a github token in the .env file")
    else:
        main_scraper()
    logging.info("finished running main")


if __name__ == "__main__":
    main()
