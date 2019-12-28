# all yaml apart from jenkins which is a single file
PATHS = {
    "travis": ".travis.yml",
    "gitlab": ".gitlab-ci.yml",
    "jenkinsPipeline":  "JenkinsFile",
    "cirrus": ".cirrus.yml",  # file endings .yml .yaml
    "github": ".github/workflows/",
    "cds": ".cds",  # file endings .yml .yaml
    "azure":  "azure-pipelines.yml",
    "circleci": ".circleci/"
}
PATHS_MULTIPLE = ["github", "circleci"]