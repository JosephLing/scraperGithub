import csvReader
import re
data = csvReader.readfile("comments test2.csv")

print(len(data))
print(len(data[0]))

print("running compression")
comments_compressed = []
for i in range(len(data)):
    line_count = 0
    multi_line = False
    comment = ""
    compressed = []
    while line_count < 6000:
        if multi_line:
            if data[i][str(line_count)]:
               comment += "\n" + data[i][str(line_count)]
            else:
                multi_line = False
                compressed.append(comment)
                comment = ""
        elif data[i][str(line_count)]:
            comment += data[i][str(line_count)]
            multi_line = True

        line_count += 1
    comments_compressed.append(compressed)
    print(data[i]["id"])

header = []
version = []
cats = {
    "todo":{"data":[], "search":"todo"},
    "note":{"data":[], "search":"note"},
    "http":{"data":[], "search":"(http:\/\/)|(https:\/\/)"},
    "fixme":{"data":[], "search":"fixme"},
    "important":{"data":[], "search":"important"},
    "header":{"data":[], "search":"###|---|===|\*\*\*"},
    "hmm":{"data":[], "search":"hmm"},
    "?!":{"data":[], "search":"\?\!"},
    "explodes": {"data": [], "search": "\!\!\!"},
    "dead": {"data": [], "search": "dies|dead|explodes|not working"}
}
for i in range(len(comments_compressed)):
    header.append([])
    for k in cats.keys():
        cats[k]["data"].append([])

    for line in comments_compressed[i]:
        line = line.lower()
        for k in cats.keys():
            if re.findall(cats[k]["search"], line):
                cats[k]["data"][i].append(line)


        # if re.match("^(\d+\.)?(\d+\.)?(\*|\d+)$", line):
        #     version.append(line)

for k in cats.keys():
    cats[k] = [v for v in cats[k]["data"] if len(v) != 0]



print("-----------")
print(len(header))
print(len(version))
print(cats)
print("overall size: ", len(data))

notes = """
NOTE: -> note Note 
version number
url
todo
fixme
important

check for the --------- for fancy formatting or ***** or =====


TODO:
- stats need to be grouped properly!!!
- comparisons for same comments
- save results so they can be displayed!
- bring across type information!!

"""