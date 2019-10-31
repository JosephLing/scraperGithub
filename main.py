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
    keys = ["name", "id", "description", "language", "open_issues", "stargazers_count", "topics", "watchers_count"]
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
        field = list(data[0].keys())

        with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:

            writer = csv.DictWriter(csvfile,fieldnames=field, quoting=csv.QUOTE_MINIMAL)
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
        print("reading >>> {}".format(repos[len(repos)-1].name))

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
    name += time.strftime("%X").replace(":","_")
    temp = g.search_code(search)
    index = 3
    page = temp.get_page(index)
    while len(page) >= 1 and index < MAX_NO_OF_PAGES and searches < 1000:
        g = Github(GITHUB_TOKEN, timeout=REQUEST_TIME_TO_COMPLETE_TIMEOUT)
        print("getting page: {}".format(index))
        repos, content = getReposFromFiles(page)


        if len(repos) > 1:
            print("sleeping for a few seconds just not to abuse the rate limiting too much")
            time.sleep(TIMEOUT)
            writeToCsv(saveRepos(repos, content), name)
        else:
            print("no data found")
        
        index += 1
        searches += len(repos)
        page = temp.get_page(index)
        print("currently {}% complete".format(searches/1000))
        print("sleeping for: {}s to avoid 403 errors due to rate limiting".format(TIMEOUT))
        time.sleep(TIMEOUT)
    print("finished going through {} pages of results and got {} results".format(index, searches))



def main():
    if GITHUB_TOKEN is None:
        print("place a github token in the .env file")
    else:

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
        getConfigStuff("filename:azure-pipelines.yml", "azure") # TODO: triple check this is how it works?? as it could just be any .yml file however it will do the job and there should be around 50,000 results

        # note: GoCd seems to be used so little that I can't find any good examples of it its config
        # combined with the fact that they allow .json and .yml ah!

if __name__ == "__main__":
    main()