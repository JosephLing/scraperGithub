import base64

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
    return "{}{}".format(count - len(str(msg)), msg)


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





def checkJenkins(line):
        temp = base64.b64decode(line.get("jenkinsPipeline0"))
        print(len(temp))

def merge(mypath, save=True):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv") and "raptor" in f]
    configs = []
    for f in onlyfiles:
        configs.append(check(join(mypath, f)))

    print("combining csv files")
    combined = {}
    duplicates = 0
    for i in range(len(configs)):
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
            combined[line.get("id")] = line


    print("duplicates: ", duplicates)
    print("results: ", len(combined.values()))
    if save:
        name = csvReader.check_name("combined")
        if name:
            csvReader.writeToCsv(list(combined.values()), name)
        else:
            print("too many combined copies already found")


def checkfiles(mypath, regexp=""):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv") and regexp in f]
    for f in onlyfiles:
        check(join(mypath, f))

if __name__ == '__main__':
    checkfiles(".", "travis")