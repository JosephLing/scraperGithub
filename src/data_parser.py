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
          "code_with_comments",
          "stars", "sub", "data", "id", "single_line_comment", "config_name", "multi_line_comment_unique",
          "multi_line_comment", "file_lines", "yaml", "bash", "powershell"]

dtypes = {**{"comments": int, "blank_lines": int, "code": int, "config": str,
             "lang": str,
             "yaml_encoding_error": str, "code_with_comments": int, "stars": int,
             "sub": int, "data": str, "id": int, "single_line_comment": int, "config_name": str,
             "multi_line_comment_unique": int, "multi_line_comment": int, "file_lines": int, "yaml": bool},
          **dict([(k, int) for k in FILTERS.keys()])}

global_lock = threading.Lock()

results = []
results_ci = []
no_readme = 0


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


def is_comment_in_yaml(message) -> str:
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

            inString, inStringQuoted, specailCharacter = handle_specail_character_and_strings(c, inString,
                                                                                              inStringQuoted)

    return ""


def handle_multiple(multi, result):
    if multi > 1:
        result["multi_line_comment"] += multi
        result["multi_line_comment_unique"] += 1
        result["single_line_comment"] -= multi
    return result


def yaml_thing(yaml_file_lines):
    return [is_comment_in_yaml(yaml_line) for yaml_line in yaml_file_lines]


def handle_specail_character_and_strings(c, inString, inStringQuoted):
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
    return inString, inStringQuoted, specailCharacter


def java_thing(file_lines):
    multi_line = False
    comments = []
    line_count = 0
    open_comment = -1

    for message in file_lines:
        if multi_line:
            if "*/" in message:
                multi_line = False
            else:
                comments.append(message)
        else:
            if message.startswith("//"):
                comments.append(message)
            else:
                open_comment = -1
                inString = False
                inStringQuoted = False
                specailCharacter = False
                for i in range(len(message)):
                    c = message[i]
                    if i + 1 <= len(message) and not inString and not specailCharacter and not inStringQuoted:
                        if message[i - 1:i + 1] == "//":
                            comments.append(message[i - 1:])
                            break
                        elif message[i - 1:i + 1] == "/*":
                            open_comment = i - 1
                        elif message[i - 1:i + 1] == "*/" and open_comment != -1:
                            if len(comments) - 1 == line_count:
                                # in the case that we have more than one comment on the line
                                # we append it onto the line of the comments
                                # this is a little bit hacky as the system is currently only designed to handle
                                # 1 comment per line as it was written for yaml
                                comments[line_count] += message[open_comment:i + 1]
                            else:
                                comments.append(message[open_comment:i + 1])

                            # so this is stupid, what it does is stops the parser from picking up:
                            # "/*hello*//*world*/" as "/*hello*/" and then "//*world/"
                            # yeah...
                            message = message[:i] + "@" + message[i + 1:]

                            open_comment = -1
                            # we could still have more comments after here so we do not break the loop

                    inString, inStringQuoted, specailCharacter = handle_specail_character_and_strings(c, inString,
                                                                                                      inStringQuoted)

        if open_comment != -1 and not multi_line and len(message) > 0:
            multi_line = True
            # if we are starting or ending the multi-line comment
            # this is where that comment proportion gets appended on
            if len(comments) - 1 == line_count:
                # in the case that we have more than one comment on the line
                # we append it onto the line of the comments
                # this is a little bit hacky as the system is currently only designed to handle
                # 1 comment per line as it was written for yaml
                comments[line_count] += message[open_comment:]
            else:
                if len(message) == open_comment:
                    comments.append(message)
                else:
                    comments.append(message[open_comment:])

        line_count += 1

        # so if we did not find a comment we need to have a blank line representing that
        if len(comments) != line_count:
            comments.append("")

    return comments


def get_comment_stats(file_as_string, func_comments):
    yaml_file_lines = file_as_string.split("\n")
    result = {}

    for filter_type in [*FILTERS.keys(), "comments", "blank_lines", "code_with_comments", "code",
                        "multi_line_comment_unique", "single_line_comment", "multi_line_comment", "bash", "powershell"]:
        result[filter_type] = 0
    multi = 0
    comments = func_comments(yaml_file_lines)
    for i in range(len(yaml_file_lines)):
        yaml_line = yaml_file_lines[i]

        if yaml_line.replace(" ", "") == "":
            result = handle_multiple(multi, result)
            multi = 0

            result["blank_lines"] += 1
        else:
            comment = comments[i]
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
                    yaml_line = yaml_line.replace(comment, "")  # get rid of the comment from the line of code
                    if yaml_line and len(re.findall("\w+\.sh", yaml_line)) != 0:
                        result["bash"] += 1
                    if yaml_line and len(re.findall("\w+\.ps1", yaml_line)) != 0:
                        result["powershell"] += 1

                    result["code"] += 1
                    result["code_with_comments"] += 1
            else:
                result = handle_multiple(multi, result)
                multi = 0

                if yaml_line and len(re.findall("\w+\.sh", yaml_line)) != 0:
                    result["bash"] += 1

                if yaml_line and len(re.findall("\w+\.ps1", yaml_line)) != 0:
                    result["powershell"] += 1

                # moved this into an else as is_commment_in_string returns just the comment
                # therefore if it is empty then it must be code
                # in doing this it should tidy up the raitos of code to comments
                result["code"] += 1

    result = handle_multiple(multi, result)
    result["file_lines"] = len(yaml_file_lines)
    return result


def get_yaml_encoding_error(fileasstring):
    yaml_encoding_error = ""
    # TODO: do we ever want to pass on the yaml blob to anywhere?
    blob = None
    try:
        blob = yaml.safe_load(fileasstring)
    except yaml.composer.ComposerError as e:
        yaml_encoding_error = "composer error"
        # print(f"composer: {e}")
    except yaml.scanner.ScannerError as e:
        yaml_encoding_error = "scanner error"
        # print(f"scanner: {e}")

    except yaml.parser.ParserError as e:
        yaml_encoding_error = "parse error"
        # print(f"parse: {e}\n{fileasstring}")

    except yaml.constructor.ConstructorError as  e:
        yaml_encoding_error = "constructor error"
        print(f"constructor: {e}\n{fileasstring}")

    except yaml.reader.ReaderError as e:
        yaml_encoding_error = "reader error"
        print(f"reader: {e}")

    return yaml_encoding_error


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
        return {**{
            "config": remove_byte_string(config_type),
            "config_name": remove_byte_string(config_name),
            "yaml_encoding_error": get_yaml_encoding_error(fileasstring),
            "lang": remove_byte_string(line.get("language")),
            "stars": line["stargazers_count"],
            "sub": line.get("subscribers_count"),
            "data": config_data,
            "yaml": True,
            "id": line.get("id")}, **get_comment_stats(fileasstring, yaml_thing)}
    else:
        print("error")


def process_config(config_data, config_type, config_name, line, is_yaml):
    # TODO: for teamcity config should we try and parse all of it for comments???
    # as we going to ignore it in later stages as well
    # but as it will be included in the stats of overall data it either needs parsing or being
    # removed from the commment data set.
    # Difficulty and pain point being that it is <!-- --> xml comments ahaha :(
    fileasstring = lib.base64Decode(config_data)
    if is_yaml:
        comment_stats = get_comment_stats(fileasstring, yaml_thing)
    else:
        comment_stats = get_comment_stats(fileasstring, java_thing)
    if fileasstring:
        return {**{
            "config": remove_byte_string(config_type),
            "config_name": remove_byte_string(config_name),
            "lang": remove_byte_string(line.get("language")),
            "stars": line["stargazers_count"],
            "sub": line.get("subscribers_count"),
            "data": config_data,
            "yaml_encoding_error": get_yaml_encoding_error(fileasstring) if is_yaml else "",
            "yaml": is_yaml,
            "id": line.get("id")}, **comment_stats}
    else:
        print("error")


def remove_byte_string(s):
    if s.startswith("b'"):
        return s[2:-1]
    return s


def check_readme(readme):
    """
    methadology search for commonly used methods of showing the CI/CD status in a ReadMe
    then filter the results dependant on whether or not it has a url. The url is used to
    provide a small svg.

    :return: config data or empty string
    """
    config = ""
    if readme:
        readme = lib.base64Decode(readme)

        if 'alt="Build Status"' in readme:
            config = readme.split('alt="Build Status"')[1].split("\n")[0]
        elif "alt='Build Status'" in readme:
            config = readme.split("alt='Build Status'")[1].split("\n")[0]
        elif "status" in readme:
            config = readme.split("status")[1].split("\n")[0]
        elif "Status" in readme:
            config = readme.split("Status")[1].split("\n")[0]

        if config and len(re.findall("(http:\/\/)|(https:\/\/)", config)) == 0:
            config = ""
    else:
        global no_readme
        no_readme += 1

    return config




def process_line(line, name):
    yaml_stats = []
    for key in config.PATHS.keys():
        for j in range(NUMBER_OF_POTENTAIL_FILES):
            config_data = line.get("{}{}".format(key, j))
            config_name = line.get("{}{}_file".format(key, j))

            if config_data:
                if key in config.NONE_YAML:
                    dataToSave = process_config(config_data, key, config_name, line, False)
                else:
                    dataToSave = process_config(config_data, key, config_name, line, True)
                yaml_stats.append(dataToSave)

    if len(yaml_stats) == 0:
        temp = check_readme(line.get("readme"))
        if temp:
            results.append(temp)
            print("{} {} {}".format(line.get("name"), line.get("stargazers_count"), line.get("subscribers_count")))

    if len(yaml_stats) != 0:
        temp = check_readme(line.get("readme"))
        if temp:
            results_ci.append(temp)


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
    print(data[0]["yaml"])
    print(type(data[0]["yaml"]))
    for line in data:
        if line.get("yaml") == "False":
            print(line)
            break


def format_as_percentage(n):
    if isinstance(n, float) or isinstance(n, int):
        return "{}%".format(round(n * 100, 2))
    else:
        return (round(n, 2)).astype("str") + "%"


def write_to_latex(name, no_repos, name_of_filtered):
    filtered = {}
    filtered_data = csvReader.readfile_low_memory(f"{name_of_filtered}.csv")

    for value in filtered_data:
        filtered[value[21]] = 0

    data = """
    \\begin{{table}}[h]
\\begin{{tabular}}{{|l|l|l|l|l|}}
\\hline
    CI/CD & \\textbf{{count}} & \\textbf{{repos with config}} & \\textbf{{no. multiple}} & \\textbf{{multiple percent}}   \\\\ \\hline
config file(s) &           {}     & {}                                & {}          & {}             \\\\ \\hline
found in ReadMe & {}     & {}                                &             &             \\\\ \\hline
none found &            {}     & {}                                &             &             \\\\ \\hline
\\end{{tabular}}
\caption[Percentage of CI used for projects]{{Percentage of CI used for projects out of a sample of {} }}
\\label{{table_ci_usage}}
\\end{{table}}
    """.format(len(filtered), format_as_percentage(len(filtered) / no_repos), len(filtered_data) - len(filtered),
               format_as_percentage((len(filtered_data) - len(filtered)) / len(filtered)),
               len(results), format_as_percentage(len(results) / no_repos),
               no_repos - len(filtered) - len(results),
               format_as_percentage((no_repos - len(filtered) - len(results)) / no_repos),
               no_repos)
    data = data.replace("%", "\\%")  # because latex
    with open(name, "w", encoding="utf-8") as f:
        f.write(data)

    print(f"written to {name} the table of stats on the data")


def main(name, data, output_for_latex):
    """
    sets up the files to write the
    """
    num_worker_threads = 1

    name = csvReader.check_name(name, limit=20)

    if name == "":
        print("file already found for the files for the main file so can't write to disk")
        return

    print(f"writing to {name}.csv")

    with open(f"{name}.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()

    run_main(num_worker_threads, data, name)
    write_to_latex(f"{output_for_latex}/generated_table2.tex", len(data), name)
    return f"{name}.csv"


if __name__ == '__main__':
    main("yaml threaded", csvReader.readfile("combined9.csv"), "./results")
    print(len(results))
    print(len(results_ci))
    print(no_readme)

    # check_output("yaml threaded5.csv")
