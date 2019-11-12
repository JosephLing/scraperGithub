import os
import csv
import sys

from os import listdir
from os.path import isfile, join

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


def check(filename):
    with open(filename, "r", encoding="utf-8") as cat:
        reader = csv.DictReader(cat)
        i = 0
        keysLength = 0
        for row in reader:
            if i == 0:
                keysLength = len(row.keys())
            i += 1
        print("name: %s%slines: %d%skeys: %d" % (filename, " " * (40 - len(filename)), i, " " * (10-len(str(i))), keysLength))


def main():
    mypath = "."
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".csv")]
    for f in onlyfiles:
        check(f)


if __name__ == "__main__":
    main()
