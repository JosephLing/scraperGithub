from src import csvReader
import re

FILTERS = {
    "todo": {"data": [], "search": "todo"},
    "note": {"data": [], "search": "note"},
    "http": {"data": [], "search": "(http:\/\/)|(https:\/\/)"},
    "fixme": {"data": [], "search": "fixme"},
    "important": {"data": [], "search": "important"},
    "header": {"data": [], "search": "###|---|===|\*\*\*"},
    "hmm": {"data": [], "search": "hmm"},
    "?!": {"data": [], "search": "\?\!"},
    "explodes": {"data": [], "search": "\!\!\!"},
    "dead": {"data": [], "search": "dies|dead|explodes|not working"},
    "version": {"data": [], "search": "(\d+\.\d+\.\d+)|(\d+\.\d+)"},
    "isMultiLine": {"data": [], "search": "\\n"}
}


def get_multi_line_comments(data) :
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
    return comments_compressed


def run():
    data = csvReader.readfile("comments threaded0.csv")

    comments_compressed = get_multi_line_comments(data)
    assert len(data) == len(comments_compressed)

    results = []
    for i in range(len(comments_compressed)):
        result = {"id":data[i].get("id")}
        for filter_type in FILTERS.keys():
            result[filter_type] = 0
        result["linecount"] = 0

        for filter_type in FILTERS.keys():
            for j in range(len(comments_compressed[i])):

                if re.findall(FILTERS[filter_type]["search"], comments_compressed[i][j]):
                    result[filter_type] += 1
                result["linecount"] += 1

        results.append(result)

    assert len(data) == len(results)
    return results

if __name__ == "__main__":
    results = run()
    name = csvReader.check_name("notes test")
    if name == "":
        print("failed no names are available :(")
    else:
        print(f"saving data to: {name}")
        csvReader.writeToCsv(results, name)
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


hash, char count, type

"""
