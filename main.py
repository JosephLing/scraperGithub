from github import Github, GithubException
from dotenv import load_dotenv
from os import getenv
import csv
import time
load_dotenv()

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
    if len(data) > 1:
        field = list(data[0].keys())

        with open("{}.csv".format(name), "a") as csvfile:

            writer = csv.DictWriter(csvfile,fieldnames=field)
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
        contents.append(file.content)
    return repos, contents

def getConfigStuff(g, search, name):
    name += time.strftime("%X")
    temp = g.search_code(search)
    index = 0
    page = temp.get_page(index)
    while len(page):
        print("getting page: {}".format(index))
        repos, content = getReposFromFiles(page)
        if len(repos) > 1:
            writeToCsv(saveRepos(repos, content), name)
        else:
            print("no data found")
        
        index += 1
        page = temp.get_page(index)
        time.sleep(500)



def main():
    GITHUB_TOKEN = getenv("GITHUB_TOKEN")
    if GITHUB_TOKEN is None:
        print("place a github token in the .env file")
    else:
        g = Github(GITHUB_TOKEN)
        getConfigStuff(g, "filename:travis.yml", "allTheTravis")

if __name__ == "__main__":
    main()