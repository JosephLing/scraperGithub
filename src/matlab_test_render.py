"""
exporting to latex guide: https://timodenk.com/blog/exporting-matplotlib-plots-to-latex/

graphing guides:
- https://matplotlib.org/3.1.1/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py



"""

import matplotlib.pyplot as plt
import csvReader
import pandas as pd
from data_parser import dtypes
import numpy as np
import config


def spread_of_data_sub_to_stars(data):
    plot = plt
    plot.xlabel('stars')
    plot.ylabel('subscribers')

    x = []
    y = []
    for line in data:
        x.append(int(line.get("stargazers_count")))
        y.append(int(line.get("subscribers_count")))
    plot.scatter(x, y, s=1, alpha=0.75)

    plot.title("Sample of repositories from github")

    plot.legend()
    return plot


def spread_data_issues_vs_stars(data):
    plot = plt
    plot.xlabel('stars')
    plot.ylabel('issues')

    x = []
    y = []
    for line in data:
        x.append(int(line.get("stargazers_count")))
        y.append(int(line.get("open_issues")))

    plot.scatter(x, y, s=1, alpha=0.75)

    plot.title("Sample of repositories from github")

    plot.legend()
    return plot


def save_as_pdf(plot, name):
    plot.savefig(f'{name}.svg', format="svg")
    # delete the graph
    plot.clf()


def spread_over_time_stars(data):
    plot = plt
    plot.ylabel('stars')
    plot.xlabel('index')
    x = []
    for line in data:
        x.append(int(line.get("stargazers_count")))

    x.sort()
    plot.scatter(list(range(len(x))), x, s=0.5)

    plot.title("Spread over time of stars")

    return plot


def boxplot_stars(plot, data):
    """
    kind of works but doesn't create anything that can be easily displayed as all the data is
    grouped up as predicted at one end....

    therefore the line graph still is the best way to show the spread still
    """
    plot.ylabel('stars')
    x = []
    for line in data:
        x.append(int(line.get("stargazers_count")))

    plot.boxplot(x, vert=False, showfliers=False, autorange=True)

    return plot


def load_dataframe(name):
    return pd.read_csv(name, dtype=dtypes)


def _value_counts_bar_graph(plot, data):
    data.pop("travis")
    data.pop("github")
    plot.bar(list(data.keys()), [data[k] for k in data.keys()])
    return plot


def config_bargraph(plot, dataset):
    # returns the config count for all config types
    # note: this doesn't matter if we have multiple configurations in the repo
    return _value_counts_bar_graph(plot, dataset["config"].value_counts())


def yaml_config_errors_to_latex(name, dataset):
    df = dataset.groupby(['config', 'yaml_encoding_error']).size().unstack(fill_value=0)
    with open(name, 'w') as tf:
        s = "\\begin {table}[h]" + df.to_latex().replace("\\midrule", "").replace("\\toprule", "\\hline").replace(
            "\\bottomrule", "").replace("\\\\", "\\\\ \\hline").replace("lrrrr", "|l|l|l|l|l|") + "\\end {table}"
        s = "\n".join([v for v in s.split("\n") if not v.startswith("config")])
        tf.write(s)


def config_type_split(name, dataset):
    df = dataset["config"].value_counts()
    total = sum([df[k] for k in df.keys()])
    values = ["{:.0%}".format(df[k] / total) for k in df.keys()]
    df = df.to_frame()
    df["percentage"] = values

    s = "\\begin {table}[h]" + df.to_latex().replace("\\midrule", "").replace("\\toprule", "\\hline").replace(
        "\\bottomrule", "").replace("\\\\", "\\\\ \\hline").replace("lrrrr", "|l|l|l|l|l|") + "\\end {table}"

    with open(name, 'w') as tf:
        tf.write(s)


def main(experimenting):
    """
    failed:
    - stars box plot
    """
    if experimenting:
        # dataset = load_dataframe("yaml threaded5.csv")
        # print(dataset[["config_name", "config", "file_lines"]].head(5))
        # print("-----------")
        # print(dataset.loc[dataset["config"] == "travis"].head(5))
        # yaml_config_errors(plt, dataset).show()
        # temp(plt, [])
        # yaml_config_errors_per_config(plt, dataset).show()
        # blank lines, comments, code, total lines
        dataset = load_dataframe("yaml threaded6.csv")
        # config_bargraph(plt, dataset).show()

    else:
        data = csvReader.readfile("combined.csv")

        save_as_pdf(spread_of_data_sub_to_stars(data), "sub vs stars")
        save_as_pdf(spread_over_time_stars(data), "spread over time")
        save_as_pdf(spread_data_issues_vs_stars(data), "issues vs stars")

        dataset = load_dataframe("yaml threaded6.csv")
        yaml_config_errors_to_latex("yaml config errors.tex", dataset)
        config_type_split("configuration type count.tex", dataset)

        print("finished building")


if __name__ == '__main__':
    main(False)
    # main(True)
