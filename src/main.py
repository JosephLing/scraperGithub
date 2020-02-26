import csvReader
import data_parser
import render_main
import checker
from pathlib import Path
from dotenv import load_dotenv
from os import getenv
import time

OUTPUT_RESULTS_PATH = "./results"

Path(OUTPUT_RESULTS_PATH).mkdir(parents=True, exist_ok=True)

load_dotenv()

def is_bool(value):
    return value in ["True", "true"]

CHECK = is_bool(getenv("CHECK", ""))
MERGE = is_bool(getenv("MERGE", ""))
PARSE = is_bool(getenv("PARSE", ""))
RENDER = is_bool(getenv("RENDER", ""))

name1_base_name = "combined"
name2_base_name = "yaml threaded"

name1 = ""
name2 = ""
user_input = ""

print("config check:{} merge:{} parse:{} render:{}".format(CHECK, MERGE, PARSE, RENDER))
s = time.time()
if CHECK:
    checker.merge("./newData", query="socket", save=False)
    user_input = input("do you want to save the merge?").replace(" ", "")
    while user_input not in ["yes", "y", "no", "n"]:
        user_input = input("do you want to save the merge?").replace(" ", "")

if (MERGE and user_input == "") or user_input in ["yes", "y"]:
    print("running merge")
    name1 = checker.merge("./newData", query="socket", save=True)
    name2 = data_parser.main(name2_base_name, csvReader.readfile(name1), OUTPUT_RESULTS_PATH)

if PARSE:
    print("parsing data")
    if name1 == "":
        name1 = csvReader.get_latest_name(name1_base_name)
    name2 = data_parser.main(name2_base_name, csvReader.readfile(name1), OUTPUT_RESULTS_PATH)

if RENDER:
    print("rendering")
    if name1 == "":
        print("check1")
        name1 = csvReader.get_latest_name(name1_base_name)
    if name2 == "":
        print("check2")
        name2 = csvReader.get_latest_name(name2_base_name)
    print(f"reading data from {name1} and {name2}")
    render_main.main(False, name1, name2, "pdf", OUTPUT_RESULTS_PATH)

if not RENDER and not PARSE and not MERGE and not CHECK:
    print("no options were selected")

print("ran in {}".format(s-time.time()))