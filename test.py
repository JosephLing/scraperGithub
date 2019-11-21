import math

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import csvReader
from config import PATHS
import plotly.express as px
import pandas as pd
import copy
import plotly.colors as cat


# csvfiledata = csvReader.readfile("data/raptor14_04_19stars30004000.csv")
csvfiledata = csvReader.readfile("combined2.csv")
# csvfiledata = []

#
# ids = {}
# for line in csvfiledata:
#     if ids.get(line.get("id")) is None:
#         ids[line.get("id")] = 0
#     ids[line.get("id")] += 1
#
#
# temp = [k for k in ids.keys() if ids[k] != 1]

# print(len(temp))

def get_spreadofdata():
    stars = []
    watchers = []
    for line in csvfiledata:
        stars.append(int(line.get("stargazers_count")))
        if line.get("watchers"):
            if line.get("watchers_count"):
                watchers.append(int(line.get("watchers_count")))
            else:
                watchers.append(0)
        else:
            watchers.append(int(line.get("watchers")))

    xAxis = list(range(len(csvfiledata)))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xAxis, y=watchers))
    fig.add_trace(go.Scatter(x=xAxis, y=stars))
    fig.show()


#
# def get_stars():
#     stars = []
#     watchers = []
#     for line in csvfiledata:
#         stars.append(int(line.get("stargazers_count")))
#         if line.get("watchers"):
#             if line.get("watchers_count"):
#                 watchers.append(int(line.get("watchers_count")))
#             else:
#                 watchers.append(0)
#         else:
#             watchers.append(int(line.get("watchers")))
#
#     xAxis = list(range(len(csvfiledata)))
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=xAxis, y=watchers))
#     fig.add_trace(go.Scatter(x=xAxis, y=stars))
#     fig.show()


def configCountPerLanguage():
    data = {"lang": {}}
    # lang:[str], travis:[], ...

    pathKeysCopy = copy.copy(PATHS)
    pathKeysCopy["none"] = 0

    for line in csvfiledata:
        if data["lang"].get(line.get("language")) is None:
            data["lang"][line.get("language")] = ""

    data["lang"] = list(data["lang"].keys())

    for k in pathKeysCopy.keys():
        data[k] = [0 for i in range(len(data["lang"]))]

    for line in csvfiledata:
        for configType in pathKeysCopy.keys():
            for config in csvReader.KEYS_TO_TRY:
                if configType in config:
                    if line.get(config):
                        data[configType][data["lang"].index(line.get("language"))] += 1

    for i in range(len(data["lang"])):
        total = 0
        for k in pathKeysCopy.keys():
            total += data[k][i]

        if total == 0:
            total = 1

        none = 1
        for k in pathKeysCopy.keys():
            data[k][i] = float(data[k][i]) / total
            none -= data[k][i]

        data["none"][i] = none

    col_count = 3
    language_leng = len(data["lang"])
    row_count = math.ceil(language_leng / float(col_count))
    fig = make_subplots(
        shared_xaxes=True,
        rows=row_count, cols=col_count,
        subplot_titles=data["lang"],
        column_widths=[1/col_count for i in range(col_count)],
        row_heights=[1/row_count for i in range(row_count)])

    languageIndex = 0
    for row in range(row_count):
        for col in range(col_count):
            if languageIndex >= language_leng:
                pass
            else:
                fig.add_trace(
                    go.Bar(
                        x=list(pathKeysCopy.keys()),
                        y=[data[buildType][languageIndex] for buildType in pathKeysCopy.keys()]),
                    row=row+1,
                    col=col+1)

            languageIndex += 1
    print(len(data["lang"]))
    fig.update_layout(height=6000)
    fig.show()

    #
    # wide_df = pd.DataFrame(data)
    # print(wide_df)
    # tidy_df = wide_df.melt(id_vars="lang")
    # print(tidy_df)
    # fig = px.bar(tidy_df, x="lang", y="value", color="variable", barmode="group")
    # fig.show()


def getBuildSystemStats():
    temp = dict([(k, 0) for k in PATHS.keys()])
    for line in csvfiledata:
        for configType in PATHS.keys():
            for config in csvReader.KEYS_TO_TRY:
                if configType in config:
                    if line.get(config):
                        temp[configType] += 1

    fig = go.Figure()
    fig.add_trace(go.Pie(values=list(temp.values()), labels=list(temp.keys())))
    fig.show()


def checkValidConfigHeader(config):
    for t in PATHS.keys():
        if t in config:
            return True
    return False


def configNo():
    build_system_count = 0
    for line in csvfiledata:
        for config in csvReader.KEYS_TO_TRY:
            if checkValidConfigHeader(config):
                if line.get(config):
                    build_system_count += 1
                    break

    print("no. of repositories with some kind of build files: %d" % build_system_count)
    print("no. of repositories with no build files: %d" % (len(csvfiledata) - build_system_count))
    print("%s%% of repositories have build config" % ((build_system_count / len(csvfiledata)) * 100))


# getBuildSystemStats()
configCountPerLanguage()
# get_spreadofdata()
