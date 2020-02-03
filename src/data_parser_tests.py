import unittest
from data_parser import is_comment_in_string, get_comment_stats

example_files_test_cases = [
    """addons:
  apt:
    packages: &id001
    - nodejs
cache:
  apt: true
  directories:
  - $HOME/cmake-3.3.2-Linux-x86_64/bin
  - $HOME/cmake-3.3.2-Linux-x86_64/share
  - $TRAVIS_BUILD_DIR/Submodules/CEF
  - $TRAVIS_BUILD_DIR/.git/modules/Submodules/CEF
compiler: gcc
dist: trusty
env:
  global:
  - MAKEFLAGS=-j4
  - CXXFLAGS=-Wno-invalid-offsetof
git:
  submodules: false
language: cpp
matrix:
  exclude:
  - addons:
      apt:
        packages:
        - *id001
        - gcc-mingw-w64-x86-64
        - g++-mingw-w64-x86-64
        - binutils-mingw-w64-x86-64
    before_script: 'ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/windows.h
      Windows.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/shobjidl.h ShObjIdl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/strsafe.h Strsafe.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/psapi.h Psapi.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/sddl.h Sddl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/accctrl.h AccCtrl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/aclapi.h Aclapi.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/oleidl.h OleIdl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/lib/libws2_32.a libWs2_32.a

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/lib/libiphlpapi.a libIphlpapi.a

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/lib/libwldap32.a libWldap32.a

      export CFLAGS="-I`pwd` -L`pwd` $CFLAGS"

      export CXXFLAGS="-I`pwd` -L`pwd` $CXXFLAGS"

      '
    env: CMAKE_TOOLCHAIN_FILE=Build/CMake/Toolchains/MinGW.cmake CMAKE_SYSTEM_PROCESSOR=x86_64
      ATOMIC_D3D9=1
  - addons:
      apt:
        packages:
        - *id001
        - gcc-mingw-w64-i686
        - g++-mingw-w64-i686
        - binutils-mingw-w64-i686
    before_script: 'ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/windows.h
      Windows.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/shobjidl.h ShObjIdl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/strsafe.h Strsafe.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/psapi.h Psapi.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/sddl.h Sddl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/accctrl.h AccCtrl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/aclapi.h Aclapi.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/include/oleidl.h OleIdl.h

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/lib/libws2_32.a libWs2_32.a

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/lib/libiphlpapi.a libIphlpapi.a

      ln -s /usr/$CMAKE_SYSTEM_PROCESSOR-w64-mingw32/lib/libwldap32.a libWldap32.a

      export CFLAGS="-I`pwd` -L`pwd` $CFLAGS"

      export CXXFLAGS="-I`pwd` -L`pwd` $CXXFLAGS"

      '
    env: CMAKE_TOOLCHAIN_FILE=Build/CMake/Toolchains/MinGW.cmake CMAKE_SYSTEM_PROCESSOR=i686
      ATOMIC_D3D9=1
  - addons: &id002
      apt:
        packages:
        - *id001
        - g++-multilib
        - libasound2-dev:i386
        - libxrandr-dev:i386
        - libgl1-mesa-dev:i386
        - libglu1-mesa-dev:i386
    env: LINUX=1 ATOMIC_64BIT=0 CFLAGS=-m32 CXXFLAGS=-m32
  - addons: *id002
    compiler: clang
    env: LINUX=1 ATOMIC_64BIT=0 CFLAGS=-m32 CXXFLAGS=-m32
  fast_finish: true
  include:
  - addons: &id003
      apt:
        packages:
        - *id001
        - libgtk-3-dev
        - libasound2-dev
        - libxrandr-dev
        - libgl1-mesa-dev
        - libglu1-mesa-dev
    env: LINUX=1
  - addons: *id003
    compiler: clang
    env: LINUX=1
notifications:
  email:
    on_failure: always
    on_success: change
  webhooks:
    on_failure: always
    on_start: always
    on_success: always
    urls:
    - https://webhooks.gitter.im/e/c123a34751c16d5a7b40
os: linux
script: "# Update CMake to 3.3 (minimum required version)\nif [[ ! -f $HOME/cmake-3.3.2-Linux-x86_64/bin/cmake\
  \ ]];\nthen\n    wget --no-check-certificate https://cmake.org/files/v3.3/cmake-3.3.2-Linux-x86_64.tar.gz\
  \ -O $HOME/cmake.tar.gz && \\\n    tar xf $HOME/cmake.tar.gz -C $HOME && \\\n  \
  \  rm $HOME/cmake.tar.gz\nfi\nexport PATH=$HOME/cmake-3.3.2-Linux-x86_64/bin:$PATH\n\
  mkdir build\ncd build\ncmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE}\
  \ ..\ncmake --build .\n"
sudo: false
""",
    """
    after_success:
- mkdir -p ./releases/
- cp "$(which hadolint)" "./releases/${BINARY_NAME}"
before_install:
- export BINARY_NAME="hadolint-$(uname -s)-$(uname -m)"
- mkdir -p ~/.local/bin
- "if [[ \"${TRAVIS_OS_NAME}\" = \"osx\" ]]\nthen\n  travis_retry curl -sSL https://www.stackage.org/stack/${TRAVIS_OS_NAME}-x86_64\
  \ \\\n    | tar xz --strip-components=1 -C ~/.local/bin --include   '*/stack'\n\
  else\n  travis_retry curl -sSL https://www.stackage.org/stack/${TRAVIS_OS_NAME}-x86_64\
  \ \\\n    | tar xz --strip-components=1 -C ~/.local/bin --wildcards '*/stack'\n\
  fi\n"
cache:
  directories:
  - $HOME/.stack
  timeout: 300
compiler: gcc
git:
  depth: 100
install:
- travis_retry stack --no-terminal --install-ghc $ARGS test --only-dependencies
- stack --no-terminal $ARGS install --ghc-options='-fPIC'
language: c
matrix:
  allow_failures:
  - env: ARGS="--resolver nightly"
  include:
  - dist: xenial
    env: ARGS="--resolver lts"
  - addons:
      artifacts:
        paths:
        - ./releases
    before_deploy:
    - ldd $(which hadolint) || true
    - curl -sSL https://github.com/upx/upx/releases/download/v3.95/upx-3.95-amd64_linux.tar.xz
      | tar -x --xz --strip-components=1 -C ~/.local/bin upx-3.95-amd64_linux/upx
    - upx -q --best --ultra-brute "./releases/${BINARY_NAME}"
    deploy:
      provider: releases
      api_key: &id001
        secure: bAcEdQB7Hk4yDz58u5oo8aEoitbbobaqW7Dr58asJHnm0KG3g1lJqCrgRP2ldbmG8I9zj1osfw0qGCNc3MZW2sV5AaWqxUGC1Sw2jmz0fqdajk8f0bZXZMECFeryPeXmPRftw0VAKz5dVw5wzjunaAVUEuCC3B4a80v/3+Qj8t2FaslG+uNoTTEEzHPfwgowYPQf+QR1Ob3lWM41g0ORC9mgYAD/PIUi8mnxCVRExUecHwhTM1A8UMo/MDVQuv3cclJ+Xc10O9KTCr7tf9uh4g2ZY4RD/aW5zuUt1tqMVJfcL/BQi5wOrhJd0jwMW8LZg0eBypezXZ70CC1Eb+vwe7OUrDlUroyzPUsOXd7u6LAWe+dBE0zNwvWXFnUF6ls8cJDhrVoSmVV3SFd208/xmemDgMmtBWwcjxyCM3kMyCBx1T6nkXQ4czS5Nvn1dav87sgyowR52W52oiyomJyJtBrmrlP/2qgNAJgQuzah/ltuBBvyGCaiwFQFHzUjUNv/ENCNP06aEVTLdbkLXLNfvlw6NZbn8KIOGFmSncLT3hNtcRhS6XnrCIyOc6hYelzVLXPNhmWFo7Ob3/1GFSvlWVmzHEp5+AeTYAQmsAZMAe/E5ofVSrU/3DhXvxMjzdOq5bZ9FsOMfooxYIPp05kVsW4H6dB8kIUqQcWTntt4ys4=
      file: ./releases/${BINARY_NAME}
      skip_cleanup: true
      draft: true
      tag_name: ${TRAVIS_TAG}
      true: &id002
        tags: true
    dist: xenial
    env: ARGS=""
  - dist: xenial
    env: ARGS="--resolver nightly"
  - env: ARGS="--resolver lts"
    os: osx
  - addons:
      artifacts:
        paths:
        - ./releases
    before_deploy:
    - brew install upx
    - otool -L $(which hadolint) || true
    - upx -q --best --ultra-brute "./releases/${BINARY_NAME}"
    deploy:
      provider: releases
      api_key: *id001
      file: ./releases/${BINARY_NAME}
      skip_cleanup: true
      draft: true
      tag_name: ${TRAVIS_TAG}
      true: *id002
    env: ARGS=""
    os: osx
  - env: ARGS="--resolver nightly"
    os: osx
  - after_success: true
    before_install: true
    env: Build_Docker_Image
    install:
    - travis_wait 30 docker build --tag hadolint:$(git describe --always --tags --dirty)
      --file docker/Dockerfile --target distro .
    - docker build --tag hadolint:$(git describe --always --tags --dirty)-debian --file
      docker/Dockerfile --target debian-distro .
    script:
    - docker image ls
    - docker run --rm -i hadolint:$(git describe  --always --tags --dirty) < docker/Dockerfile
    - grep $(git describe --dirty) <<< $(docker run --rm -i hadolint:$(git describe  --always
      --tags --dirty) hadolint --version)
    - grep $(git describe --dirty) <<< $(docker run --rm -i hadolint:$(git describe  --always
      --tags --dirty)-debian hadolint --version)
    services:
    - docker
    sudo: required
  - after_success: true
    before_install: true
    env: Version_Check_and_Linting
    install:
    - docker pull zemanlx/remark-lint:0.1.4
    script:
    - docker run --rm -i -v $PWD:/lint/input:ro zemanlx/remark-lint:0.1.4 --frail
      .
    - curl -sL https://raw.github.com/ndmitchell/hlint/master/misc/travis.sh | sh
      -s .
    - "GIT_VERSION=$(git describe | grep -oE \"[0-9]+\\.[0-9]+\\.[0-9]+\")\nHARDCODED_VERSION=$(grep\
      \ version package.yaml | grep -oE \"[0-9]+\\.[0-9]+\\.[0-9]+\")\necho \"${GIT_VERSION}\\\
      n${HARDCODED_VERSION}\" | sort --check --version-sort \\\n  || ( echo \"Update\
      \ version in package.yaml and then tag git commit.\" && false )\n"
    services:
    - docker
    sudo: required
script:
- stack --no-terminal $ARGS test
- hadolint docker/Dockerfile
sudo: false
"""
]


class IsCommentInStringTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(is_comment_in_string("#hello"), "#hello")

    def test_end_of_string(self):
        self.assertEqual(is_comment_in_string("asdfasdfasdf#hello"), "#hello")

    def test_quotes(self):
        self.assertEqual(is_comment_in_string("'a'#hello"), "#hello")

    def test_single_quotes(self):
        self.assertEqual(is_comment_in_string('"asdf"#hello'), "#hello")

    def test_mixed_quotes(self):
        self.assertEqual(is_comment_in_string("'asdf#assd'#cat"), "#cat")

    def test_mixed_quotes2(self):
        self.assertEqual(is_comment_in_string('"asa#cats"asdfdfsdf#dog'), "#dog")

    def test_empty(self):
        self.assertEqual(is_comment_in_string(''), "")

    def test_newline(self):
        self.assertEqual(is_comment_in_string('\n'), "")

    def test_no_comment(self):
        self.assertEqual(is_comment_in_string('hello world'), "")


class GetCommentStats(unittest.TestCase):
    def gen_default(self):
        return {'?!': 0,
                'blank_lines': 0,
                'code': 0,
                'code_with_comments': 0,
                'comments': 0,
                'dead': 0,
                'explodes': 0,
                'fixme': 0,
                'header': 0,
                'hmm': 0,
                'http': 0,
                'important': 0,
                'multi_line_comment': 0,
                'multi_line_comment_unique': 0,
                'note': 0,
                'single_line_comment': 0,
                'todo': 0,
                'version': 0,
                'yaml_file_lines': 0}

    def test_basic(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 1
        expected["comments"] = 1
        expected["single_line_comment"] = 1
        self.assertEqual(get_comment_stats("#hello"), expected)

    def test_none(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 1
        expected["code"] = 1
        self.assertEqual(get_comment_stats("cats"), expected)

    def test_code_and_single_comment(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 2
        expected["code"] = 1
        expected["comments"] = 1
        expected["single_line_comment"] = 1

        self.assertEqual(get_comment_stats("cats\n#dogs"), expected)

    def test_actual_file(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 150
        expected["blank_lines"] = 27
        expected["code"] = 123

        self.assertEqual(get_comment_stats(example_files_test_cases[0]), expected)

    def test_actual_file_with_complex_script_tags(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 119
        expected["blank_lines"] = 2
        expected["code"] = 117

        self.assertEqual(get_comment_stats(example_files_test_cases[1]), expected)

    def test_todo_comment(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 11
        expected["blank_lines"] = 2
        expected["code"] = 8
        expected["code_with_comments"] = 1
        expected["todo"] = 1
        expected["comments"] = 2
        expected["single_line_comment"] = 1

        self.assertEqual(get_comment_stats("""
go:
- 1.12
language: go # woo I am a comment
os:
- linux
- osx
script:
- go test -v
#TODO: I am a todo 
"""), expected)

    def test_multiline_comment(self):
        expected = self.gen_default()
        expected["yaml_file_lines"] = 6
        expected["comments"] = 5
        expected["code"] = 1
        expected["multi_line_comment"] = 5
        expected["multi_line_comment_unique"] = 2

        self.assertEqual(get_comment_stats("# hello world\n#cats\n#dogs\nfoo bar\n# another testt\n#foo"), expected)


if __name__ == '__main__':
    unittest.main()
