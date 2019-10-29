from github import Github, GithubException
from dotenv import load_dotenv
from os import getenv
load_dotenv()

GITHUB_TOKEN = getenv("GITHUB_TOKEN")
if GITHUB_TOKEN is None:
    print("place a github token in the .env file")
else:
    g = Github(GITHUB_TOKEN)
    repos = g.get_user().get_repos()
    keys = ["name", "id", "description", "language", "open_issues", "stargazers_count", "topics", "watchers_count"]
    methods = ["get_readme"]
    for repo in repos:
        readme = 0
        try:
            readme = repo.get_readme().size
        except GithubException as e:
            pass
        print("{}\t readme: {}".format("\t".join(["{} {}".format(k, getattr(repo, k)) for k in keys]), readme))