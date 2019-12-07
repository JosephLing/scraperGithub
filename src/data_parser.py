import yaml
from src import config
import lib
from src import csvReader
csvfiledata = csvReader.readfile("combined.csv")
print("start")
import csv

FIELDS = ["comments", "blank_lines", "code", "config", "yaml_encoding_error", "code_with_comments", "lines", "percentage", "stars", "sub", "data", "id"]


def isCommentInString(message):
    search = "#"
    if message.startswith(search):
        return 1
    if search in message:
        inString = False
        specailCharacter = False
        for c in message:

            if c == search and not inString and not specailCharacter:
                return 2

            specailCharacter = False

            if c == "'":
                inString = True
            elif inString and c == "'":
                inString = False

            elif not inString and c == '\\':
                specailCharacter = True
    return 0

def appendData(name, data):
    with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        for d in data:
            writer.writerow(d)

def get_comment_stats(fileasstring):
    yaml_file_lines = fileasstring.split("\n")
    comments = 0
    blank_lines = 0
    code_with_comments = 0
    code = 0
    for yaml_line in yaml_file_lines:
        yaml_line = yaml_line.replace(" ", "")
        isComment = isCommentInString(yaml_line)
        if isComment == 1:
            comments += 1
        elif isComment == 2:
            code += 1
            code_with_comments += 1
        elif yaml_line == "":
            blank_lines += 1
        else:
            code += 1
    return comments, blank_lines, code, code_with_comments, len(yaml_file_lines)

def process(data, line, key):
    fileasstring = lib.base64Decode(data)
    if fileasstring:
        yaml_encoding_error = ""
        blob = None
        try:
            blob = yaml.safe_load(fileasstring)
        except yaml.composer.ComposerError as e:
            yaml_encoding_error = "composer error"
        except yaml.scanner.ScannerError as e:
            yaml_encoding_error = "scanner error"
        except yaml.parser.ParserError as e:
            yaml_encoding_error = "parse error"
        except yaml.constructor.ConstructorError as e:
            yaml_encoding_error = "constructor error"
        except yaml.reader.ReaderError as e:
            yaml_encoding_error = "reader error"

        if blob is not None:
            pass
        comments, blank_lines, code, code_with_comments, yaml_file_lines = get_comment_stats(fileasstring)

        return {"comments": comments,
                "blank_lines": blank_lines,
                "code": code,
                "config":key,
                "yaml_encoding_error": yaml_encoding_error,
                "code_with_comments": code_with_comments,
                "lines": yaml_file_lines,
                "percentage": (comments / yaml_file_lines) * 100,
                "stars": line["stargazers_count"],
                "sub": line.get("subscribers_count"),
                "data": data,
                "id": line.get("id")}


def foo_worker(line, name):
    yaml_stats = []
    for key in config.PATHS.keys():
        for j in range(24):
            data = line.get("{}{}".format(key, j))
            if data:
                yaml_stats.append(process(data, line, key))
    appendData(name, yaml_stats)



def check(name):
    data = csvReader.readfile("{}.csv".format(name))
    count = 0
    for line in data:
        print(line.keys())
        print("{} {} {}".format(line.get("config"), line.get("stars"), line.get("lines")))
        count += 1
        if count > 10:
            break
    # import pandas as pd
    # print(pd.read_csv("{}.csv".format(name)))


def main(name):

    import threading
    import queue
    num_worker_threads = 5
    with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

    def worker():
        while True:
            line = q.get()
            if line is None:
                break
            foo_worker(line, name)
            q.task_done()

    q = queue.Queue()
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for line in csvfiledata:
        q.put(line)

    # block until all tasks are done
    q.join()
    print("all workers are done!")

    # stop workers
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()

if __name__ == '__main__':
    main("yaml threaded")
    check("yaml threaded")
    # print(len(csvfiledata))