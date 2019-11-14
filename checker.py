import csvReader
import lib

from os import listdir
from os.path import isfile, join, exists




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
        if keysLength == 80:

            for k in csvReader.KEYS_TO_TRY:
                if line.get(k) is not None and line.get(k) != "":
                    r = parseFile(line.get("config"))
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

def merge():
    mypath = "./data"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv") and "raptor" in f]
    configs = []
    for f in onlyfiles:
        configs.append(check(join(mypath, f)))

    print("combining csv files")
    combined = []
    for i in range(len(configs)):
        if len(configs[i]) == 108:
            tempfiles = csvReader.readfile(join(mypath, onlyfiles[i]))
            for line in tempfiles:
                combined.append(line)

    name = "combined"
    count = 0
    while exists("{}.csv".format(name)):
        name = "combined%d" % count
        count += 1
        print("file already exists trying alternative name")
        if count > 10:
            break
    if count < 10:
        csvReader.writeToCsv(combined, name)
    else:
        print("too many combined copies already found")

def checkfiles(mypath, regexp=""):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv") and regexp in f]
    for f in onlyfiles:
        check(join(mypath, f))


def main():
    # checkfiles("./data", "raptor")
    checkfiles(".", "combined0")
    # merge()

if __name__ == "__main__":
    main()
