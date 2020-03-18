# all yaml apart from jenkins which is a single file
PATHS = {
    "travis": "travis",
    "gitlab": "gitlab-ci",
    "azure": "azure-pipelines",
    "appVeyor": "appveyor",
    "drone": "drone",

    "jenkinsPipeline": "jenkinsfile",
    
    "teamcity": ".teamcity/",


    "github": ".github/workflows/",
    "circleci": ".circleci/",
    "semaphore": ".semaphore/",
    "buildkite": ".buildkite/"
}
PATHS_MULTIPLE = ["github", "circleci", "semaphore", "teamcity", "buildkite"]
NONE_YAML = ["jenkinsPipeline", "teamcity"]
