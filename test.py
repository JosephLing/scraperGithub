import plotly.graph_objects as go
import csvReader
from config import PATHS
import plotly.express as px
import pandas as pd

# csvfiledata = csvReader.readfile("data/raptor14_04_19stars30004000.csv")
csvfiledata = csvReader.readfile("combined.csv")
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

def get_stars():
    temp = [int(line.get("stargazers_count")) for line in csvfiledata]
    temp.sort()
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=temp))
    fig.show()


def configCountPerLanguage():
    data = {"lang": {}}

    for line in csvfiledata:
        if data["lang"].get(line.get("language")) is None:
            data["lang"][line.get("language")] = ""

    data["lang"] = list(data["lang"].keys())

    for k in PATHS.keys():
        data[k] = [0 for i in range(len(data["lang"]))]

    for line in csvfiledata:
        for configType in PATHS.keys():
            for config in csvReader.KEYS_TO_TRY:
                if configType in config:
                    if line.get(config):
                        data[configType][data["lang"].index(line.get("language"))] += 1

    wide_df = pd.DataFrame(data)
    print(wide_df)
    tidy_df = wide_df.melt(id_vars="lang")
    print(tidy_df)
    fig = px.bar(tidy_df, x="lang", y="value", color="variable", barmode="group")
    fig.show()



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
    print("%s%% of repositories have build config" % ((build_system_count/len(csvfiledata))*100))

# getBuildSystemStats()
# configCountPerLanguage()
get_stars()