from sys import maxsize
import csv
import config
NUMBER_OF_KEYS_PER_CONFIG = 24

KEYS_TO_TRY = ['config']
for k in config.PATHS.keys():
    for i in range(NUMBER_OF_KEYS_PER_CONFIG):
        KEYS_TO_TRY.append("{}{}".format(k, i))



maxInt = maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


def readfile(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            lines.append(row)
    return lines


def writeToCsv(data, name):
    if len(data) >= 1:
        print("saving: data")
        field = list(data[0].keys())

        with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:

            writer = csv.DictWriter(
                csvfile, fieldnames=field, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for d in data:
                writer.writerow(d)
    else:
        print("no data found")

