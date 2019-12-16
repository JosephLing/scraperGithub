import yaml
from . import config
import lib
from . import csvReader
import csv
import threading
import queue
FIELDS = ["comments", "blank_lines", "code", "config", "lang", "yaml_encoding_error", "code_with_comments", "lines", "percentage", "stars", "sub", "data", "id"]
dtypes = {"comments":int, "blank_lines":int, "code":int, "config":str,
          "lang":str,
          "yaml_encoding_error":str, "code_with_comments":int, "lines":int, "percentage":float, "stars":int, "sub":int, "data":str, "id":int}

COMMENTS_FIELDS = list(range(6000))
COMMENTS_FIELDS.append("id")
COMMENTS_FIELDS.append("lang")


global_lock = threading.Lock()

def isCommentInString(message) -> str:
    search = "#"
    if message.startswith(search):
        return message
    if search in message:
        inString = False
        inStringQuoted = False
        specailCharacter = False
        for i in range(len(message)):
            c = message[i]
            if c == search and not inString and not specailCharacter and not inStringQuoted:
                return message[i:]

            specailCharacter = False
            if not inStringQuoted:
                if c == "'" and not inString:
                    inString = True
                elif inString and c == "'":
                    inString = False
            if not inString:
                if c == '"' and not inStringQuoted:
                    inStringQuoted = True
                elif inStringQuoted and c == '"':
                    inStringQuoted = False

            elif not (inString or inStringQuoted) and c == '\\':
                specailCharacter = True
    return ""

def appendData(name, data, fields):

    if data:
        global_lock.acquire()
        with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
            for d in data:
                writer.writerow(d)

        global_lock.release()

def get_comment_stats(fileasstring):
    yaml_file_lines = fileasstring.split("\n")
    comments_data = []
    comments = 0
    blank_lines = 0
    code_with_comments = 0
    code = 0
    for i in range(len(yaml_file_lines)):
        yaml_line = yaml_file_lines[i]
        if yaml_line.replace(" ", "") == "":
            blank_lines += 1
        else:
            comment = isCommentInString(yaml_line)
            if comment != "":
                comments_data.append((i, comment))
                if len(comment) == len(yaml_line):
                    comments += 1
                else:
                    code += 1
                    code_with_comments += 1

            code += 1
    return comments, blank_lines, code, code_with_comments, len(yaml_file_lines), comments_data

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
        comments, blank_lines, code, code_with_comments, yaml_file_lines, comments_data = get_comment_stats(fileasstring)
        comments_data = dict(comments_data)
        if len(comments_data) != 0:
            comments_data["lang"] = line.get("language")
            comments_data["id"] = line.get("id")
            if comments_data["lang"] is None:
                if blob.get("language") is not None:
                    comments_data["lang"] = blob.get("language")

        return {"comments": comments,
                "blank_lines": blank_lines,
                "code": code,
                "config":key,
                "yaml_encoding_error": yaml_encoding_error,
                "code_with_comments": code_with_comments,
                "lines": yaml_file_lines,
                "lang":line.get("language"),
                "percentage": (comments / yaml_file_lines) * 100,
                "stars": line["stargazers_count"],
                "sub": line.get("subscribers_count"),
                "data": data,
                "id": line.get("id")},comments_data


def foo_worker(line, name):
    yaml_stats = []
    comments = []
    for key in config.PATHS.keys():
        for j in range(24):
            data = line.get("{}{}".format(key, j))
            if data:
                dataToSave, comments_data = process(data, line, key)
                if len(comments_data) > 0:
                    comments.append(comments_data)
                yaml_stats.append(dataToSave)
    appendData(name, yaml_stats, FIELDS)
    appendData("comments test2", comments, COMMENTS_FIELDS)



def check(name):
    data = csvReader.readfile("{}.csv".format(name))
    count = 0
    print(len(data))
    for line in data:
        print(line.keys())
        print("{} {} {} {}".format(line.get("config"), line.get("stars"), line.get("lines"), line.get("id")))
        count += 1
        if count > 10:
            break
    # import pandas as pd
    # print(pd.read_csv("{}.csv".format(name)))


def main(name, data):

    num_worker_threads = 5
    with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

    with open("comments test2.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=COMMENTS_FIELDS, quoting=csv.QUOTE_MINIMAL)
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

    for line in data:
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
    # main("yaml threaded", csvReader.readfile("combined.csv"))
    # check("yaml threaded")
    # print(len(csvfiledata))
    print(isCommentInString('"chat.freenode.net#deadbeefplayer"'))
    print(isCommentInString('"he\'t#dog"#cat'))
    print(isCommentInString('#cat'))
    print(isCommentInString("'asdfasd#asdff'"))
    print(isCommentInString("'asdfasd#asdf'#dogsaretheworst"))
