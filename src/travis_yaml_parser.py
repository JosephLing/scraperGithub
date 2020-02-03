import yaml
import lib
import csvReader
# Note: at 10/12/2019 travis lint didn't work
# or at the very least did not provide error messages approritate to there own docs
# as well as was doing it via sending requests off. Therefore ratelimiting would have
# been an issue.

#
def parse_dict(init, lkey='', depth=0):
    ret = {}
    for rkey, val in init.items():
        # some how someone has put a
        # True:
        # - asdf
        # - asdfsdfasd
        # peice of yaml!!!
        # why!?
        if isinstance(rkey, bool):
            rkey = str(rkey)
        key = lkey + rkey
        if isinstance(val, dict):
            ret.update(parse_dict(val, key + '.'))
        elif isinstance(val, list):
            if len(val) == 0:
                ret["{}[_]".format(key)] = None

            elif len(val) == 1:
                # speicail case where its only a list of one item
                # we are doing this to simplify the pre-processing to make sure it is easier to check for lists
                # we could just pretend that it is a value but that would break the comparison e.g. cat[0].dog
                # would not be the same as cat.dog
                if isinstance(val[0], dict):
                    if depth >= 1:
                        print("oh no")
                    ret.update(parse_dict(val[0], "{}[*].".format(key), depth+1))
                else:
                    ret["{}[*]".format(key)] = val[0]
            else:
                keyValuePair = isinstance(val[0], dict)
                for i in range(len(val)):
                    if isinstance(val[i], dict):
                        if not keyValuePair:
                            print("mis-matched types")
                            keyValuePair = True
                        if depth >= 1:
                            print("oh no")
                        ret.update(parse_dict(val[i], "{}[{}].".format(key, i), depth+1))
                    else:
                        if keyValuePair:
                            print("mis-matched types")
                            keyValuePair = False
                        ret["{}[{}]".format(key, i)] = val[i]
        else:
            ret[key] = val
    return ret


def generateStuff(name):
    """
    Need to look into transforming [] -> that contain objects into something that can easily be compared

    if we used the dot synatx we could check for it properly
    e.g. cat[0] vs cat[0].
    so cat[1....3] -> cat.array = []

    cat[0].whateverthingitwas......

    maybe...

    what is important is maintaining some semblenance of the ordering as for example for the before_all hook the order
    in which you execute the actions is importnat
    """
    parsed_data = []
    data = csvReader.readfile("{}.csv".format(name))
    count = 0
    for line in data:
        if line.get("config") == "travis" and line.get("yaml_encoding_error") == "":
            string = lib.base64Decode(line.get("data"))
            # print(string)
            ydata = yaml.safe_load(string)

            # if there is no yaml code in the file just comments it will return as a string
            if isinstance(ydata, dict):
                parsed_data.append(parse_dict(ydata, ""))

    all_keys = {}
    for line in parsed_data:
        for k in line.keys():
            all_keys[k] = 1
        if line.get("language") is None:
            line["language"] = "ruby"
        elif line.get("os[0]") is None and line.get("os") is None:
            line["os[0]"] = "linux"
        elif line.get("os") is not None:
            line["os[0]"] = line.get("os")
            line.pop("os")
    return all_keys, parsed_data

if __name__ == '__main__':
    all_keys, parsed_data = generateStuff("yaml threaded")
# name = csvReader.check_name("travis_flattened")
# csvReader.writeToCsv(parsed_data, name, list(all_keys.keys()))





# data = csvReader.readfile_low_memory("travis_flattened2.csv")
# print(len(data))
# print(len(data[0]))
# print(data[0])
# print(dict([(data[0][i], i) for i in range(len(data[0]))]))

# print(basics_stats)
# print(master)

# temp = {'dist': 3118, 'language': 14706, 'cache': 4589,
#         'env': 4607, 'matrix': 3890, 'services': 1676,
#         'before_script': 3553, 'before_install': 4972,
#         'install': 5809, 'script': 11394,
#         'after_success': 2761,
#         'jdk': 1331, 'sudo': 6279,
#         'os': 1375, 'node_js': 4291,
#         'addons': 2385, 'notifications': 3358,
#         'deploy': 1189, 'after_script': 888,
#         'git': 722, 'branches': 2050,
#         'xcode_workspace': 64, 'xcode_scheme': 158,
#         'osx_image': 835, 'after_failure': 274, 'php': 808,
#         'jobs': 804, 'compiler': 573, 'python': 1525, 'go': 986, 'rvm': 1069, 'before_cache': 545,
#         'group': 120, 'gemfile': 221, 'before_deploy': 408, 'bundler_args': 144, 'before_scrpt': 8,
#         'android': 523, 'after_deploy': 57, 'doctr': 1, 'xcode_project': 127, 'xcode_sdk': 92,
#         'if': 60, 'rust': 156, 'stage': 14, 'stages': 294, 'solution': 49, 'mono': 97,
#         'dotnet': 58, 'go_import_path': 176, 'anchors': 3, 'scala': 119,
#         'x-pyenv-shard': 1, 'x-py27': 1, 'x-py37': 1, 'x-pypy': 1,
#         'x-linux-shard': 1, 'x-linux-27-shard': 1, 'x-linux-pypy-shard': 1,
#         'x-linux-37-shard': 1, 'x-osx-shard': 1, 'x-osx-ssl': 1, 'x-osx-27-shard': 1,
#         'x-osx-37-shard': 1, 'podfile': 40, 'julia': 16, 'codecov': 2, 'virtualenv': 22,
#         'conditions': 7, '_base_envs': 2, 'conan-linux': 2, 'conan-linux-master': 1,
#         'conan-osx': 2, 'perl': 23, 'haxe': 3, 'licenses': 25, 'mysql': 5, 'elixir': 56,
#         'otp_release': 102, 'xcode_destination': 14, 'components': 3, 'linux': 2,
#         'osx': 2, 'allow_failures': 4, 'lein': 25, '_integration_job_template': 1,
#         '_android_job_template': 1, '_ios_job_template': 1,
#         'xcode_schemes': 6, 'notification': 10, 'before_script_reference': 1,
#         'esudo': 1, 'only': 13, 'email': 18, 'apt': 6, 'sources': 1, 'packages': 1,
#         'global': 5, 'provider': 2, 'skip_cleanup': 4, 'profile': 2, 'base_postgres': 1,
#         'base_acceptance': 1, '// From Travis support': 1, 'skip_build': 1, 'sqlite': 1,
#         'echo': 1, 'dummy': 1, 'webhooks': 2, './.travis/deploy.enc': 1, 'test': 6,
#         'sbt_args': 4, 'after_error': 1, 'warnings_are_errors': 21, 'r_packages': 7,
#         'r_binary_packages': 2, 'arch': 14, 'addons_shortcuts': 2,
#         '.ubuntu_precise_toolchain_sources': 1, '.ubuntu_trusty_toolchain_sources': 1,
#         'after_install': 10, 'min_amd64_deps': 1, 'min_amd64_conf': 1, 'max_amd64_deps': 1,
#         'max_amd64_conf': 1, 'max_x86_deps': 1, 'max_x86_conf': 1, 'ghc': 2, 'build': 2,
#         'ios_env': 1, 'tvos_env': 1, 'gobuild_args': 4, 'stage_generic': 1, 'stage_linux': 1,
#         'macros': 1, 'x_base_steps': 1, 'version': 6, 'import': 3, 'github_token': 1,
#         'linux-ppc64le': 1, 'lint_steps': 1, 'crystal': 2, 'r': 12, 'service': 3, 'requires': 1,
#         'serivces': 1, 'custom': 3, 'testSmokeCy': 1, 'testPostDeploy': 1, 'global_env': 2, 'pandoc_version': 6,
#         'nix': 3, 'not-on-master': 1, 'extended-test-suite': 1, 'custom_scripts': 1, 'fast_finish': 14,
#         'defaults': 1, '.before_script': 1, 'travisBuddy': 2, '_bindings': 1, '_browsers': 2, '_defaults': 1,
#         'ruby': 2, 'get': 1, '.org.ruby-lang.ci.matrix-definitions': 1, 'x-template': 1, 'include': 5,
#         '.disable_global': 1, '.moban': 1, 'languages': 1, 'xcode_schema': 2, 'xcodebuild': 2,
#         'py27-steps': 1, 'py37-steps': 1, 'pyinstaller-steps': 1, 'cran': 1, 'smoke_script': 1,
#         'unit_script': 1, 'integration_script': 1, 'repos': 6, 'exclude': 3, 'before_install_rl': 1,
#         'install_dl': 1, 'install_rl': 1, 'apt_packages': 2, 'before_depoly': 1, 'allow_failure': 2,
#         'linux_clang': 1, 'linux_gcc': 1, 'scala_version_212': 1, 'scala_version_213': 1, 'java_8': 1,
#         'java_11': 1, 'before script': 2, 'scheme': 2, 'before-caching': 1, 'xcode-project': 1, 'latex': 9,
#         'fortran': 1, 'common_sources': 4, 'dart': 11, 'workspaces': 1, 'build-shared': 1, 'shared': 1,
#         'before-script': 1, '_unittest': 1, '_build': 1, '_node_js': 1, '_python': 1, '_docker': 1,
#         '_version': 1, 'default-cflags': 1, 'secure': 1, 'd': 3, 'node_js-steps': 1, 'branch': 1,
#         'maven': 1, 'cabal': 2, 'slack': 3, 'on_failure': 3, 'linux_deps': 1, 'finish': 1,
#         'cross_deps': 1, 'normal_install': 1, 'cross_install': 1, 'dd': 2, 'bioc_required': 2,
#         'e2e_tests': 1, 'install_mongo': 1, True: 3, '.mixtures': 2, 'r_github_packages': 8,
#         'before-cache': 1, '-cache': 1, '.steps': 1, 'notificaitons': 1, 'filter_secrets': 4,
#         'postgres': 1, 'after_sucess': 1, 'directories': 2, '.apt': 1, '.hosts': 1, '.sauce_connect': 1,
#         'langauage': 1, 'apt_targets': 1, 'deploy_build': 1, 'linux_after_success': 1,
#         'env_template': 1, 'with_content_shell': 1, '_ios': 6, '_android': 6, 'llvm_current_packages': 1,
#         'r_build_args': 3, 'r_check_args': 4, 'clojure': 1, 'build_script': 1, '.deploy_job_template': 1,
#         'java/service-account': 1, 'api_key': 1, 'file': 1, 'tags': 1, 'repo': 1, 'aliases': 1, 'anguage': 1,
#         'dart_task': 1, 'jsdecena': 1, 'required': 1, 'pkg_deps_prereqs_distro': 2, 'pkg_deps_prereqs_source': 2,
#         'pkg_deps_prereqs': 2, 'pkg_deps_doctools': 2, 'pkg_deps_devtools': 2, 'pkg_src_zeromq_ubuntu12': 1,
#         'pkg_src_zeromq_ubuntu14': 2, 'pkg_src_zeromq_ubuntu16': 2, 'java': 1, 'pkg_deps_zproject': 1,
#         'manylinux-build': 1, 'brefore_install': 2, '.mixins': 1, 'intstall': 1, 'INSTALL_NODE_VIA_NVM': 2,
#         'INSTALL_WASM_PPACK': 1, 'defaults_go': 1, 'defaults_js': 1, 'source_key': 1, 'hxml': 1, 'langauge': 2,
#         'addons_linux_build': 1, 'addons_macos_build': 1, 'addons_linux_docker': 1, 'linux_target': 1,
#         'linux_target32': 1, 'osx_target': 1, 'osx_target32': 1, 'install_llvm': 1, 'install_gtest': 1,
#         'docker_llvm': 1, 'compile_and_test': 1, 'docker_compile_and_test': 1, '_packages': 1,
#         '_stylecheck': 1, 'branchs': 1, 'scripts': 2, '_deploy': 1, 'dist_check': 1, 'languange': 1,
#         'general': 1, 'machine': 1, 'osx_sdk': 1, 'irc': 1, 'notifcations': 1, 'udo': 1,
#         '-notifications': 1, '_addons': 1, 'aarch64_packages': 1, 'extra_packages': 1,
#         'build_32b_packages': 1, 'doc_packages': 1, 'docker_setup': 1, 'docker_login': 1,
#         '.stage_build_linux_template': 1, '.stage_build_linux_asan_template': 1,
#         '.stage_build_linux_tsan_template': 1, '.stage_build_linux_cov_template': 1,
#         '.stage_build_osx_template': 1, 'install_coveralls_commands': 1, 'newsboat_brew_commands': 1,
#         'native_image': 1, 'reference': 1, 'base_script': 1, 'coveralls_script': 1,
#         'after_coveralls_script': 1, 'deploy.skip_cleanup': 1, 'phps': 1, 'brefore_script': 1,
#         'stage_base': 1, 'stage_build_docker': 1, 'stage_build_osx': 1, 'stage_deploy': 1,
#         'stage_deploy_ppa': 1, 'r_check_revdep': 1, 'languaje': 1, 'coveralls': 1}





#
# templates = [
#     '%{repository}',
#     '%{repository_slug}',
#     '%{repository_name}',
#     '%{build_number}',
#     '%{build_id}',
#     '%{pull_request}',
#     '%{pull_request_number}',
#     '%{branch}',
#     '%{commit}',
#     '%{author}',
#     '%{commit_subject}',
#     '%{commit_message}',
#     '%{result}',
#     '%{duration}',
#     '%{message}',
#     '%{compare_url}',
#     '%{build_url}',
#     '%{pull_request_url}'
# ]
#
# basic_structure = {
#     "addons": {},
#     "after_deploy": [],  # or single string
#     "after_failure": [],
#     "after_result": [],
#     "after_script": [],
#     "after_sucess": [],
#     "before_cache": [],
#     "before_deploy": [],
#     "before_install": [],
#     "before_script": [],
#     "branches": {},  # or a list of strings or a regular expression
#     "branches.only": [],
#     "branches.except": [],
#     "bundler_args": "",  # only for ruby
#     "cache": {
#         "apt": False,
#         "bundler": False,
#         "ccache": False,
#         "cocoapods": False,
#         "directories": [],
#         "edge": False,
#         "pip": False
#     },
#     "compiler": [],  # gcc, clang, g++ or clang++ compiler[]
#     "composer_args": "",  # php
#     "crystal": [],  # cyrstal,
#     "d": [],  # d
#     "dart": [],  # dart
#     "deploy": [],  # list of key value mappings, or strings, or a single key value mapping or string
#     # deploy[].* key value mapping, or string
#     # deploy.*.* string or encrypter string
#     # deploy.edge boolean
#     # deploy.on {},[],""
#     # deploy.on.all_branches boolean
#     # deploy.on.branch []
#     # deploy.on.condition []
#     # deploy.on.jdk (language: clojure, groovy, java, ruby) string
#     # deploy.on.node string
#     # deploy.on.python
#     # deploy.on.repo
#     # deploy.on.ruby
#     # deploy.on.rvm -> this means deploy.on.ruby
#     # deploy.on.scala
#     # deploy.on.tags boolean
#     # deploy.provider (this setting is required) string
#     "dist": "",
#     "env": {},  # [], "encrypted string"
#     # env.global [], encrypted strings, string
#     # env.matrix
#     "gemfile": [],
#     "ghc": [],
#     "git": {"depth": int, "strategy": int, "submodules": bool},
#     "go": [],
#     "gobuild_args": str,
#     "group": str,
#     "haxe": [],
#     "language": "",  # NOTE: THIS IS REQUIRED!!!!
#     "lein": "",
#     "matrix": {
#         "allow_failures": {},
#         # "allow_failures": list of key value mappings; or a single key value mappings
#         # "allow_failures": key value ammpings
#         # "allow_failures.compiler":
#         # "allow_failures.crystal":
#         # "allow_failures.d":
#         # "allow_failures.dart":
#         # "allow_failures.env":
#         # "allow_failures.gemfile":
#         # "allow_failures.ghc":
#         # "allow_failures.go":
#         # "allow_failures.haxe":
#         # "allow_failures.jdk":
#         # "allow_failures.lien":
#         # "allow_failures.node": -> points to node_js
#         # "allow_failures.node_js":
#         # "allow_failures.os":
#         # "allow_failures.otp":
#         # "allow_failures.otp_release":
#         # "allow_failures.node_js":
#         # "allow_failures.node_js":
#         # "allow_failures.node_js":
#         # "allow_failures.node_js":
#
#         "exclude": {},
#
#         "fast_finish": bool,
#         "include": {}
#     },
#     "node": [],  # -> "node_js"
#     "node_js": [],
#
#     "notifications": {
#         "campfire": {
#             "disabled": False,
#             "enabled": False,
#             "on_failure": "",  # always, never, change
#             "on_start": "",  # always, never, change
#             "on_success": "",  # always, never, change
#             "rooms": [],
#             "template": ""
#             # %{repository}, %{repository_slug}, %{repository_name}, %{build_number}, %{build_id}, %{pull_request}, %{pull_request_number}, %{branch}, %{commit}, %{author}, %{commit_subject}, %{commit_message}, %{result}, %{duration}, %{message}, %{compare_url}, %{build_url}, %{pull_request_url}.
#         },
#         "email": {},  # list, boolean value
#         # email.disabled
#         # email.enabled
#         # email.on_failure
#         # email.on_start
#         # email.on_success
#         # email.recipients
#
#         "flowdock": {},  # string or boolean
#         # flowdock.api_token
#         # flowdock.disabled
#         # flowdock.enabled
#         # flowdock.on_failure
#         # flowdock.on_start
#         # flowdock.on_success
#
#         "hipchat": {},  # list, boolean
#         # .disabled
#         # .enabled
#         # .format text or html
#         # .on_failure
#         # .on_start
#         # .on_success
#         # .rooms [] or string
#
#             "irc":{},
#             "pushover":{},
#             "slack":{},
#             "sqwiggle":{},
#             "webhook":{}, # alais for webhooks
#             "webhooks":{},
#
#     },
#         "npm_args":"", # string,
# "os":[], # defaults to linux,
#         "osx_image":"",
#         "otp":"", # otp_release
#         "perl":"",
#
#
# }