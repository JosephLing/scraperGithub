import csvReader
import lib
from os import listdir
from os.path import isfile, join


def parseFile(config):
    y = None
    if config is not None:
        data = None
        lib.base64Decode(config)
        if data is not None:
            y = lib.yamlParse(config)
        else:
            return "base64"

    if y is not None:
        return "yaml"


def pad(msg, count=10):
    return "{}{}".format(" " * (count - len(str(msg))), msg)


def check(filename):
    if filename is None:
        return 0
    lines = csvReader.readfile(filename)
    if len(lines) == 0:
        keys_length = 0
    else:
        keys_length = len(lines[0].keys())
    readme = 0
    jenkins = 0
    for line in lines:
        if line.get("readme") is not None:
            readme += 1

        if line.get("jenkinsPipeline0"):
            jenkins += 1


    print("filename: {}{}{}{}{}".format(filename, pad(keys_length, 20), pad(len(lines),20) , pad(readme), pad(jenkins)))
    return len(lines)


def merge(mypath, save=True, query="raptor"):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv") and query in f]
    combined = {}
    duplicates = 0
    forks = 0
    for i in range(len(onlyfiles)):
        tempfiles = csvReader.readfile(join(mypath, onlyfiles[i]))
        for line in tempfiles:
            for k in csvReader.KEYS_TO_TRY:
                # if there is no config
                if line.get(k) is None:
                    line[k] = ""

            # watchers not working
            if line.get("watchers") is None:
                line["watchers"] = 0

            # duplicates numbers
            if combined.get(line.get("id")) is not None:
                duplicates += 1
            if line.get("fork") is not None and isinstance(line.get("fork"), bool) and line.get("fork"):
                forks += 1
            combined[line.get("id")] = line


    print("duplicates: ", duplicates)
    print("forks: ", forks)
    print("results: ", len(combined.values()))
    if save:
        name = csvReader.check_name("combined")
        if name:
            csvReader.writeToCsv(list(combined.values()), name)
        else:
            print("too many combined copies already found")


def checkfiles(mypath, regexp=""):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv") and regexp in f]
    total = 0
    for f in onlyfiles:
        total += check(join(mypath, f))
    print(total)

if __name__ == '__main__':
    checkfiles(".", "socket")
    merge(".", query="socket", save=True)
