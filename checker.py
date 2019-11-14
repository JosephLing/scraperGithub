import csv
import sys
import yaml
import base64
import binascii
from os import listdir
from os.path import isfile, join

import main as mainScraper
NUMBER_OF_KEYS_PER_CONFIG = 12
KEYS_TO_TRY = ['config']
for k in mainScraper.PATHS.keys():
    for i in range(NUMBER_OF_KEYS_PER_CONFIG):
        KEYS_TO_TRY.append("{}{}".format(k, i))

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

def pad(msg,prev_mesg, padding=20):
    return "{}{}".format(" " * (padding - len(prev_mesg)), msg)

def parseFile(config):
    y = None
    if config is not None:
        data = None
        try:
            data = base64.b64decode(config)
        except binascii.Error as e:
            return "base64"

        if data is not None:
            try:
                y = yaml.safe_load(data)
            except yaml.scanner.ScannerError as e:
                # print("invalid scan")
                pass
            except yaml.parser.ParserError as e:
                # print("invalid parse")
                pass
            except yaml.constructor.ConstructorError as e:
                # print("invalid constuctor")
                pass
            except yaml.reader.ReaderError as e:
                # print("invalid reader error")
                pass

    if y is not None:
        return "yaml"


def check(filename):
    with open(filename, "r", encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile)
        i = 0
        keysLength = 0
        validConfig = 0
        base64Errors = 0
        readMeEncoding = 0
        for row in reader:
            if i == 0:
                keysLength = len(row.keys())

            try:
                base64.b64decode(row.get("readme"))
            except binascii.Error as e:
                readMeEncoding += 1

            if keysLength == 10:
                r = parseFile(row.get("config"))
                if r == "base64":
                    base64Errors += 1
                elif r == "yaml":
                    validConfig += 1
            if keysLength == 80:


                for k in KEYS_TO_TRY:
                    if row.get(k) is not None and row.get(k) != "":
                        r = parseFile(row.get("config"))
                        if r == "base64":
                            base64Errors += 1
                        elif r == "yaml":
                            validConfig += 1

            i += 1

        print("name: %slines: %s keys: %s decode error: %s valid yml:%s readme: %d" % (filename, pad(i,filename, 40),
                                                                                pad(keysLength, str(i),10),
                                                                                pad(validConfig, str(keysLength), 5),
                                                                                pad(base64Errors, str(validConfig), 5), readMeEncoding ))


def main():
    mypath = "."
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv")]
    for f in onlyfiles:
        check(f)


if __name__ == "__main__":
    main()
