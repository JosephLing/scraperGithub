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
    plot.ylabel('subscribers')

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
    plot.savefig(f'{name}.pdf', format="pdf")
    # delete the graph
    plot.clf()

def spread_over_time_stars(data):
    plot = plt
    plot.ylabel('stars')
    plot.ylabel('index')
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
    plot.bar(list(data.keys()), [data[k] for k in data.keys()])
    return plot

def config_bargraph(plot, dataset):
    # returns the config count for all config types
    # note: this doesn't matter if we have multiple configurations in the repo
    return _value_counts_bar_graph(plot, dataset["config"].value_counts())

def yaml_config_errors_per_config(plot, dataset):
    labels = [k for k in config.PATHS.keys() if k not in config.NONE_YAML]
    grouped_data = dict([(k, dataset.loc[dataset["config"] == k]["yaml_encoding_error"]) for k in labels])

    for g in grouped_data:
        print("{} {}".format(len(grouped_data[g]), g))

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    print(x)
    fig, ax = plot.subplots()
    # grouped_data[k]
    import random
    # rects1 = ax.bar(x - width / 2, [1,2,3,4,5,6,7,8,9], width, label='Men')
    rects = []
    for i in range(len(labels)):
        print(grouped_data[labels[i]].keys())
        rects.append(ax.bar(x + (width*(i+1))/9, [random.randint(1,100) for i in range(9)], width, label=labels[i]))


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    for rect in rects:
        autolabel(rect)

    fig.tight_layout()

    return plot

def temp(plot, dataset):
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    data = {"erro1":[1,2,3,4,5], "erro3":[1,2,3,4,5], "erro2":[1,2,3,4,5], "erro4":[1,2,3,4,5]}
    x = np.arange(len(labels))  # the label locations
    width = 0.15  # the width of the bars

    fig, ax = plot.subplots()
    rects = []
    import random
    print(len(data))
    for i in range(len(data)):
        k = list(data.keys())[i]
        if len(data)  % 2== 0:

            if i % 2 == 0:
                rects.append(ax.bar(x - width/len(data), data[k], width, label=k))
            else:
                rects.append(ax.bar(x + width/len(data), data[k], width, label=k))

    # rects.append(ax.bar(x - width / 2, [random.randint(50) for i in range(5)], width, label='Men'))
    # rects.append(ax.bar(x - width / 4, [random.randint(50) for i in range(5)], width, label='Men'))
    # rects.append(ax.bar(x + width / 4, [random.randint(50) for i in range(5)], width, label='Women'))
    # rects.append(ax.bar(x + width / 2, [random.randint(50) for i in range(5)], width, label='Women'))

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    for rect in rects:
        autolabel(rect)
    fig.tight_layout()

    plt.show()

def yaml_config_errors(plot, dataset):
    # returns for all the yaml configuration errors
    return _value_counts_bar_graph(plot, dataset.loc[dataset["yaml"]]["yaml_encoding_error"].value_counts())

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
        # config_bargraph(plt, dataset).show()
        # yaml_config_errors(plt, dataset).show()
        temp(plt, [])
        # yaml_config_errors_per_config(plt, dataset).show()
        # blank lines, comments, code, total lines

    else:
        data = csvReader.readfile("combined.csv")

        save_as_pdf(spread_of_data_sub_to_stars(data), "sub vs stars")
        save_as_pdf(spread_over_time_stars(data), "spread over time")
        save_as_pdf(spread_data_issues_vs_stars(data), "issues vs stars")

        dataset = load_dataframe("yaml threaded6.csv")
        print("cats: ", len(dataset))

        save_as_pdf(yaml_config_errors(plt, dataset), "yaml config errors")


if __name__ == '__main__':
    main(False)
