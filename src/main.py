import csvReader
import data_parser
import render_main
import render_sankey_diagram
import checker
from pathlib import Path
from dotenv import load_dotenv
from os import getenv

Path("/results").mkdir(parents=True, exist_ok=True)

CHECK = bool(getenv("CHECK", False))
MERGE = bool(getenv("CHECK", False))
RENDER = bool(getenv("RENDER", False))
PARSE = bool(getenv("PARSE", False))

name1_base_name = "combined"
name2_base_name = "yaml threaded"

name1 = ""
name2 = ""
user_input = ""
if CHECK:
    checker.merge(".", query="socket", save=False)
    user_input = input("do you want to save the merge?")
    while user_input not in ["yes", "y", "no", "n"]:
        user_input = input("do you want to save the merge?")

if MERGE or user_input in ["yes", "y"]:
    name1 = checker.merge(".", query="socket", save=True)
    name2 = data_parser.main(name2_base_name, csvReader.readfile(name1))

if PARSE:
    if name1:
        name1 = csvReader.get_latest_name(name1_base_name)
    name2 = data_parser.main(name2_base_name, csvReader.readfile(name1))

if RENDER:
    if name1:
        name1 = csvReader.get_latest_name(name1_base_name)
    if name2:
        name2 = csvReader.get_latest_name(name2_base_name)
    render_main.main(False, name1, name2, "pdf", "./results")

if not RENDER and not PARSE and not MERGE and not CHECK:
    print("no options were selected")