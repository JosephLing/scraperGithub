from github import Github, GithubException
from dotenv import load_dotenv
from os import getenv
import csv
load_dotenv()

def saveRepos(repos, name="repo"):
    keys = ["name", "id", "description", "language", "open_issues", "stargazers_count", "topics", "watchers_count"]
    methods = ["get_readme"]
    for repo in repos:
        print("saving >>> {}".format(repo.name))

        readme = ""
        try:
            readme = repo.get_readme().content
        except GithubException as e:
            pass
        
        dictionary = dict([(k, getattr(repo, k)) for k in keys])
        dictionary["readme"] = readme

        field = list(dictionary.keys())
        
        with open("{}.csv".format(name), "a") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=field)
            writer.writerow(dictionary)
        
def getReposFromFiles(files):
    repos = []
    contents = []
    for file in files:
        repos.append(file.repository)
        contents.append(file.content)
    return repos,contents

def main():
    GITHUB_TOKEN = getenv("GITHUB_TOKEN")
    if GITHUB_TOKEN is None:
        print("place a github token in the .env file")
    else:
        g = Github(GITHUB_TOKEN)
        temp = g.search_code("filename:travis.yml")
        print(temp.get_page(0))
        repos, content = getReposFromFiles(temp.get_page(0))
        saveRepos(repos, "travis2")


if __name__ == "__main__":
    main()