import base64

from . import csvReader
from . import lib

from os import listdir
from os.path import isfile, join




def pad(msg,prev_mesg, padding=20):
    return "{}{}".format(" " * (padding - len(prev_mesg)), msg)

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


def check(filename):
    lines = csvReader.readfile(filename)
    i = 0
    keysLength = 0
    validConfig = 0
    base64Errors = 0
    readMeEncoding = 0
    maxKeys = {}
    for line in lines:
        if i == 0:
            keysLength = len(line.keys())
            if keysLength > len(maxKeys.keys()):
                maxKeys = line.keys()

        base64 = lib.base64Decode(line.get("readme"))
        if base64 is None:
            readMeEncoding += 1
        if keysLength == 10:
            r = parseFile(line.get("config"))
            if r == "base64":
                base64Errors += 1
            elif r == "yaml":
                validConfig += 1
        for k in csvReader.KEYS_TO_TRY:
            if line.get(k) is not None and line.get(k) != "":
                r = parseFile(line.get(k))
                if r == "base64":
                    base64Errors += 1
                elif r == "yaml":
                    validConfig += 1
        i += 1

    print("name: %slines: %s keys: %s decode error: %s valid yml:%s readme: %d" % (filename, pad(i,filename, 40),
                                                                                   pad(keysLength, str(i),10),
                                                                                   pad(validConfig, str(keysLength), 5),
                                                                                   pad(base64Errors, str(validConfig), 5), readMeEncoding ))
    return maxKeys

def checkJenkins(line):
    if line.get("jenkinsPipeline0"):
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


def main():
    print("running")
    # checkfiles("./data", "raptor")
    # checkfiles(".", "combined")
    merge(mypath="./newData")

if __name__ == "__main__":
    main()
