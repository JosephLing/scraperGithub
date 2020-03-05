"""
exporting to latex guide: https://timodenk.com/blog/exporting-matplotlib-plots-to-latex/

graphing guides:
- https://matplotlib.org/3.1.1/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py



"""
import math
import matplotlib.pyplot as plt
import csvReader
import pandas as pd

import render_sankey_diagram
from data_parser import dtypes


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


def spread_of_data_v2(data, sorted_data):
    plot = spread_of_data_sub_to_stars(data)

    x = []
    y = []
    for line in sorted_data:
        x.append(int(line.get("stars")))
        y.append(int(line.get("sub")))
    plot.scatter(x, y, s=1, alpha=0.3)

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


def spread_of_data_line_star(data, sorted_data):
    stars = {}
    for line in data:
        stars[int(line.get("id"))] = (int(line.get("stargazers_count")), 0)

    for line in sorted_data:
        stars[int(line.get("id"))] = (int(line.get("stars")), 1)
    return create_percentage_bar_graphs(list(stars.values()), "percentage of stars that use CI")


def spread_of_data_line_sub(data, sorted_data):
    stars = {}
    for line in data:
        stars[int(line.get("id"))] = (int(line.get("subscribers_count")), 0)

    for line in sorted_data:
        stars[int(line.get("id"))] = (int(line.get("sub")), 1)
    return create_percentage_bar_graphs(list(stars.values()), "percentage of subcriptions that use CI")


def create_percentage_bar_graphs(stars, name, grouping_amount=540):
    stars.sort(key=lambda x: x[0])
    groups = []
    j = 0
    i = 1
    while j < len(stars):
        group = []
        while j < grouping_amount * i and j < len(stars):
            group.append(stars[j][1])
            # group.append((stars[keys[j]], keys[j]))
            j += 1
        groups.append((stars[j - 1][0], group))
        i += 1

    heights = []
    bottom = []
    for group in groups:
        print(group)
        bottom.append(group[0])
        if len(group[1]) != 0:
            heights.append((sum(group[1]) / len(group[1])) * 100)
        else:
            heights.append(0)

    plot = plt
    plot.bar([str(a) for a in bottom], heights)
    plot.xticks(rotation=90)
    plot.rc(({'font.size': 10}))
    plot.title(name)
    plot.ylim(0, 100)

    return plot


def save_as_pdf(plot, name, encoding="pdf"):
    print(f'writing: {name}.{encoding}')
    plot.savefig(f'{name}.{encoding}')
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
    # data.pop("travis")
    # data.pop("github")
    plot.bar(list(data.keys()), [data[k] for k in data.keys()])
    plot.xticks(rotation=45)
    return plot


def _value_counts_bar_graph_log(plot, data):
    print(data.head(5))
    data = data.to_frame()
    print(data.columns)
    print(data.index)
    print(data.keys())
    plot.bar(list(data.keys()), [data[k] for k in data.keys()], width=0.5)
    plot.xticks(rotation=45)
    plot.rc(({'font.size': 5}))
    return plot


def config_bargraph(plot, dataset):
    # returns the config count for all config types
    # note: this doesn't matter if we have multiple configurations in the repo
    return _value_counts_bar_graph_log(plot, dataset.groupby(["id", "lang"])["lang"].value_counts())


def yaml_config_errors_to_latex(name, dataset):
    df = dataset.groupby(['config', 'yaml_encoding_error']).size().unstack(fill_value=0)
    with open(name, 'w') as tf:
        s = "\\begin {table}[!htbp]" + df.to_latex(caption="cats", bold_rows=True).replace("\\midrule", "").replace("\\toprule", "\\hline").replace(
            "\\bottomrule", "").replace("\\begin{table}", "").replace("\centering", "").replace("\\\\", "\\\\ \\hline").replace("lrrr", "|l|l|l|l|")
        s = "\n".join([v for v in s.split("\n") if not v.startswith("config")])
        tf.write(s)


def foo(dataset):
    langs = {}
    for lang in dataset.groupby(["id", "lang"]).size().keys():
        k = lang[1]
        if langs.get(lang[1]) is None:
            langs[lang[1]] = 0
        langs[lang[1]] += 1

    top = list(langs.items())
    top.sort(key=lambda x: x[1])
    top = top[len(top) - 10:]
    top = dict(top)
    # plt.rcParams.update({'font.size': 5})

    plot = plt
    plot.bar(["{}".format(k) for k in top.keys() if k is not None and k != ""], [top[k] for k in top.keys()])
    plot.xticks(rotation=45)
    # plot.show()
    return plot


def config_type_split(name, dataset):
    df = dataset["config"].value_counts()
    total = sum([df[k] for k in df.keys()])
    values = ["{:.0%}".format(df[k] / total) for k in df.keys()]
    df = df.to_frame()
    df["percentage"] = values

    s = "\\begin {table}[!htbp]" + df.to_latex(caption="dogs").replace("\\midrule", "").replace("\\toprule", "\\hline").replace(
        "\\bottomrule", "").replace("\\begin{table}", "").replace("\centering", "").replace("\\\\", "\\\\ \\hline").replace("lrrrr", "|l|l|l|l|l|")

    with open(name, 'w') as tf:
        tf.write(s)


def main(experimenting, name1, name2, image_encoding, output="."):
    if experimenting:
        # data = csvReader.readfile("combined1.csv")
        # sorted_data = csvReader.readfile("yaml threaded6.csv")
        # spread_of_data_v2(data, sorted_data).show()
        # plt.clf()
        # spread_of_data_line_sub(data, sorted_data).show()
        sorted_data = load_dataframe(name2)
        save_as_pdf(foo(sorted_data), "./results/top15_langs", "svg")
        save_as_pdf(foo(sorted_data), "./results/top15_langs", "pdf")
    else:
        data = csvReader.readfile(name1)
        #
        # save_as_pdf(spread_of_data_sub_to_stars(data), f"{output}/sub vs stars", image_encoding)
        # save_as_pdf(spread_over_time_stars(data), f"{output}/spread over time", image_encoding)
        # save_as_pdf(spread_data_issues_vs_stars(data), f"{output}/issues vs stars", image_encoding)

        sorted_data = load_dataframe(name2)
        yaml_config_errors_to_latex(f"{output}/yaml config errors.tex", sorted_data)
        config_type_split(f"{output}/configuration type count.tex", sorted_data)

        # sorted_data_csv = csvReader.readfile(name2)
        # save_as_pdf(spread_of_data_line_star(data, sorted_data_csv), f"{output}/percentage stars with CI",
        #             image_encoding)
        # save_as_pdf(spread_of_data_line_sub(data, sorted_data_csv), f"{output}/percentage sub with CI", image_encoding)

        # render_sankey_diagram.save_sanky_daigram_for_errors_and_comments(f"./{output}/sankey",
        #                                                                  pd.read_csv(name2, dtype=dtypes), False, False,
        #                                                                  image_encoding)
        # render_sankey_diagram.save_sanky_daigram_for_errors_and_comments(f"./{output}/sankey2",
        #                                                                  pd.read_csv(name2, dtype=dtypes), False, True,
        #                                                                  image_encoding)
        # render_sankey_diagram.save_sanky_daigram_for_errors_and_comments(f"./{output}/sankey3",
        #                                                                  pd.read_csv(name2, dtype=dtypes), True, False,
        #                                                                  image_encoding)

        print("finished building")


if __name__ == '__main__':
    main(False, "combined5.csv", "yaml threaded9.csv", "pdf", "./results")
    # main(True, "combined1.csv", "yaml threaded6.csv", "svg", "./results")
