# all yaml apart from jenkins which is a single file
PATHS = {
    "travis": "travis",
    "gitlab": "gitlab-ci",
    "azure": "azure-pipelines",
    "appVeyor": "appveyor",
    "drone": "drone",

    # code ship doesn't seem to have config as code in the repository

    # this one is weird so it has it's on edge case
    "jenkinsPipeline": "jenkinsfile",

    # these two should just work out of the box
    "github": ".github/workflows/",
    "circleci": ".circleci/",
    "semaphore": ".semaphore/",

    # note: this will not get any folders so we might just get a pom.xml file but might get some .kts files...
    "teamcity": ".teamcity/",

    "buildkite": ".buildkite/"  # can be anywhere but this is the most common

    # Don't have time for these... really sadly
    # "cirrus": ".cirrus.yml"  # file endings .yml .yaml
    # "cds": ".cds",  # file endings .yml .yaml NEVER GOT ANYTHING FOR THIS AND DON't have time to look into

    # wrecker (acquired by oracle):
    # https://github.com/search?q=filename%3Awrecker.yml only 17 results
    # https://devcenter.wercker.com/development/cli/usage/developing/

}
PATHS_MULTIPLE = ["github", "circleci", "semaphore", "teamcity", "buildkite"]
NONE_YAML = ["jenkinsPipeline", "teamcity"]
