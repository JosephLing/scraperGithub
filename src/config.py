# all yaml apart from jenkins which is a single file
PATHS = {
    "travis": "travis",
    "gitlab": "gitlab-ci",
    "azure": "azure-pipelines",

    # this one is weird so it has it's on edge case
    "jenkinsPipeline": "JenkinsFile",

    # these two should just work out of the box
    "circleci": ".circleci/",
    "github": ".github/workflows/",

    # Don't have time for these... really sadly
    # "cirrus": ".cirrus.yml"  # file endings .yml .yaml
    # "cds": ".cds",  # file endings .yml .yaml NEVER GOT ANYTHING FOR THIS AND DON't have time to look into

}
PATHS_MULTIPLE = ["github", "circleci"]