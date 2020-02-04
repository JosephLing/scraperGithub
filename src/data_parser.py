import yaml
import config
import lib
import re
import csvReader
import csv
import threading
import queue
from scraper import NUMBER_OF_POTENTAIL_FILES

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
}

FIELDS = [*FILTERS.keys(), "comments", "blank_lines", "code", "config", "lang", "yaml_encoding_error",
          "code_with_comments", "lines  ",
          "percentage", "stars", "sub", "data", "id", "single_line_comment", "config_name", "multi_line_comment_unique",
          "multi_line_comment", "file_lines", "yaml"]

dtypes = {"comments": int, "blank_lines": int, "code": int, "config": str,
          "lang": str,
          "yaml_encoding_error": str, "code_with_comments": int, "lines": int, "percentage": float, "stars": int,
          "sub": int, "data": str, "id": int}

global_lock = threading.Lock()


def is_comment_in_string(message) -> str:
    """
    :returns str: the comment
    """
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


def write_to_csv(name, data, fields):
    with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        for d in data:
            writer.writerow(d)


def appendData(name, data, fields):
    if data:
        global_lock.acquire()
        write_to_csv(name, data, fields)
        global_lock.release()

def handle_multiple(multi, result):
    if multi > 1:
        result["multi_line_comment"] += multi
        result["multi_line_comment_unique"] += 1
        result["single_line_comment"] -= multi
    return result

def get_comment_stats_kotlin_style(file_as_string):
    yaml_file_lines = file_as_string.split("\n")
    result = {}

    for filter_type in [*FILTERS.keys(), "comments", "blank_lines", "code_with_comments", "code",
                        "multi_line_comment_unique", "single_line_comment", "multi_line_comment"]:
        result[filter_type] = 0
    multi = 0
    for i in range(len(yaml_file_lines)):
        yaml_line = yaml_file_lines[i]

        if yaml_line.replace(" ", "") == "":
            result = handle_multiple(multi, result)
            multi = 0

            result["blank_lines"] += 1
        else:

            comment = is_comment_in_string(yaml_line)
            if comment != "":
                result["comments"] += 1

                for filter_type in FILTERS.keys():
                    if re.findall(FILTERS[filter_type]["search"], comment):
                        result[filter_type] += 1

                if len(comment) == len(yaml_line):
                    result["single_line_comment"] += 1
                    multi += 1
                else:
                    result = handle_multiple(multi, result)
                    multi = 0

                    result["code"] += 1
                    result["code_with_comments"] += 1
            else:
                result = handle_multiple(multi, result)
                multi = 0

                # moved this into an else as is_commment_in_string returns just the comment
                # therefore if it is empty then it must be code
                # in doing this it should tidy up the raitos of code to comments
                result["code"] += 1

    result = handle_multiple(multi, result)
    result["file_lines"] = len(yaml_file_lines)
    return result


def get_comment_stats_yaml(file_as_string):
    yaml_file_lines = file_as_string.split("\n")
    result = {}

    for filter_type in [*FILTERS.keys(), "comments", "blank_lines", "code_with_comments", "code",
                        "multi_line_comment_unique", "single_line_comment", "multi_line_comment"]:
        result[filter_type] = 0
    multi = 0
    comments = [is_comment_in_string(yaml_line) for yaml_line in yaml_file_lines]
    for i in range(len(yaml_file_lines)):
        yaml_line = yaml_file_lines[i]

        if yaml_line.replace(" ", "") == "":
            result = handle_multiple(multi, result)
            multi = 0

            result["blank_lines"] += 1
        else:

            comment = is_comment_in_string(yaml_line)
            if comment != "":
                result["comments"] += 1

                for filter_type in FILTERS.keys():
                    if re.findall(FILTERS[filter_type]["search"], comment):
                        result[filter_type] += 1

                if len(comment) == len(yaml_line):
                    result["single_line_comment"] += 1
                    multi += 1
                else:
                    result = handle_multiple(multi, result)
                    multi = 0

                    result["code"] += 1
                    result["code_with_comments"] += 1
            else:
                result = handle_multiple(multi, result)
                multi = 0

                # moved this into an else as is_commment_in_string returns just the comment
                # therefore if it is empty then it must be code
                # in doing this it should tidy up the raitos of code to comments
                result["code"] += 1

    result = handle_multiple(multi, result)
    result["file_lines"] = len(yaml_file_lines)
    return result


def process_jenkins_teamcity_style_config(config_data, config_name, line, config_type):
    """
    :param config_data str: hash of the config
    :param config_name str: filename of that config
    :param line dictionary: all the data for that line
    :param config_type str: the type of configuration this config belongs too
    :returns dictionary: of values to be saved:
    """
    fileasstring = lib.base64Decode(config_data)
    if fileasstring:
        print(fileasstring)
        return {**{
            "config": config_type,
            "config_name": config_name,
            "yaml_encoding_error": "",
            "lang": line.get("language"),
            "stars": line["stargazers_count"],
            "sub": line.get("subscribers_count"),
            "data": config_data,
            "yaml": False,
            "id": line.get("id")}, **get_comment_stats_yaml(fileasstring)}


def process_yaml_files(config_data, config_name, line, config_type):
    """
    :param config_data str: hash of the config
    :param config_name str: filename of that config
    :param line dictionary: all the data for that line
    :param config_type str: the type of configuration this config belongs too
    :returns dictionary: of values to be saved:
    """
    fileasstring = lib.base64Decode(config_data)
    if fileasstring:
        yaml_encoding_error = ""
        blob = None
        try:
            blob = yaml.safe_load(fileasstring)
        except yaml.composer.ComposerError:
            yaml_encoding_error = "composer error"
        except yaml.scanner.ScannerError:
            yaml_encoding_error = "scanner error"
        except yaml.parser.ParserError:
            yaml_encoding_error = "parse error"
        except yaml.constructor.ConstructorError:
            yaml_encoding_error = "constructor error"
        except yaml.reader.ReaderError:
            yaml_encoding_error = "reader error"

        return {**{
            "config": config_type,
            "config_name": config_name,
            "yaml_encoding_error": yaml_encoding_error,
            "lang": line.get("language"),
            "stars": line["stargazers_count"],
            "sub": line.get("subscribers_count"),
            "data": config_data,
            "yaml": True,
            "id": line.get("id")}, **get_comment_stats_yaml(fileasstring)}


def process_line(line, name):
    yaml_stats = []
    for key in config.PATHS.keys():
        for j in range(NUMBER_OF_POTENTAIL_FILES):
            config_data = line.get("{}{}".format(key, j))
            config_name = line.get("{}{}_file".format(key, j))

            if config_data:
                if key in config.NONE_YAML:
                    print(line.get("name"))
                    process_jenkins_teamcity_style_config(config_data, config_name, line, key)
                else:
                    dataToSave = process_yaml_files(config_data, config_name, line, key)
                    yaml_stats.append(dataToSave)

    appendData(name, yaml_stats, FIELDS)


def run_main(num_worker_threads, data, name):
    def worker():
        while True:
            line = q.get()
            if line is None:
                break
            process_line(line, name)
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
    print("finished")


def check_output(name):
    data = csvReader.readfile(name)
    print(data[0])


def main(name, data):
    """
    sets up the files to write the
    """
    num_worker_threads = 5

    name = csvReader.check_name(name)

    if name == "":
        print("file already found for the files for the main file so can't write to disk")
        return
    print(f"writing to {name}.csv")

    with open(f"{name}.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

    run_main(num_worker_threads, data, name)


if __name__ == '__main__':
    # main("yaml threaded", csvReader.readfile("combined0.csv"))
    check_output("yaml threaded2.csv")
