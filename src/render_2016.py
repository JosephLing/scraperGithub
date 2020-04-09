import math
import matplotlib.pyplot as plt
import csvReader
import pandas as pd
import numpy as np

from data_parser import dtypes, format_as_percentage
from render_main import save_as_pdf, topn


def langs_topn(data, n):
    return topn(data["language"], n, "languages")


def compare_coprus(data, data2):
    plot = plt
    plot.xlabel('number of projects')
    plot.ylabel('stars')
    data = data.sort_values(by=["stars"], ascending=True)
    data2 = data2.sort_values(by=["stargazers_count"], ascending=True)
    print(data["stars"])
    plot.plot(range(len(data)), data["stars"], label="2016")
    plot.plot(range(len(data2)), data2["stargazers_count"], label="2020")

    plot.legend()
    return plot


def write_to_latex(name, no_repos, sorted_data):
    filtered = sorted_data
    filtered_data = sorted_data[sorted_data["CI_multi"] > 1]
    data = """
    \\begin{{table}}[h]
\\begin{{tabular}}{{|l|l|l|l|l|}}
\\hline
    CI/CD & \\textbf{{count}} & \\textbf{{repos with config}} & \\textbf{{no. multiple}} & \\textbf{{multiple percent}}   \\\\ \\hline
config file(s) &           {}     & {}                                & {}          & {}             \\\\ \\hline
none found &            {}     & {}                                &             &             \\\\ \\hline
\\end{{tabular}}
\caption[Percentage of CI used for projects]{{Percentage of CI used for projects out of a sample of {} }}
\\label{{table_ci_usage}}
\\end{{table}}
    """.format(len(filtered), format_as_percentage(len(filtered) / no_repos),
               len(filtered_data),
               format_as_percentage((len(filtered_data)) / len(filtered)),
                                    (no_repos - len(filtered)),
                                    format_as_percentage((no_repos - len(filtered)) / no_repos),
                                    no_repos)

    data = data.replace("%", "\\%")  # because latex
    with open(name, "w", encoding="utf-8") as f:
        f.write(data)

    print(f"written to {name} the table of stats on the data")


def languages_table_topn(n, data, sorted_data):
    data["language"] = data["language"].apply(lambda x: x[2:-1] if isinstance(x, str) and x.startswith("b'") else x)
    data["language"] = data["language"].apply(lambda x: x[2:-1] if isinstance(x, str) and x.startswith('b"') else x)
    c = data["language"].value_counts
    # data.index.size - data["id"].value_counts().apply(lambda x: x if x == 1 else 0).sum()

    c2 = sorted_data["language"].value_counts
    frames = {"total count": c(), "using CI": c2(), "percentage CI": c2() / c() * 100}
    df = pd.DataFrame(frames)
    df = df.fillna(0)
    # df["percentage CI"] = df["percentage CI"].apply(lambda x: x if x <=100 else -100)
    df["percentage CI"] = format_as_percentage(df["percentage CI"])
    df = df.sort_values("total count", ascending=False)
    df = df.head(n)
    return df


def popularity_vs_percentage_CI_scatter(df, data):
    plot = plt
    x = []
    y = []
    names = []
    s = []
    for key, value in df["total count"].iteritems():
        s.append((value / df["total count"].max()))

    for key, value in df["percentage CI"].iteritems():
        x.append(float(value.replace("%", "")))
        y.append(data[data["language"] == key]["stars"].median())
        names.append(key)

    fig, ax = plt.subplots()
    ax.scatter(y, x, [a * 50 for a in s])
    for i, txt in enumerate(names):
        ax.annotate(txt, (y[i], x[i]), fontsize=4 + (s[i] * 5))
    plt.ylim(0, 100)
    plt.xlabel("stars")
    plt.ylabel("percentage")
    return fig


def config_bar(data):
    """
    This is rather hacky but limited time and Cloud Bees isn't in the corpus so...
    """
    configs = ["Travis", "CircleCI", "AppVeyor", "Werker"]
    values = []
    for config in configs:
        if config == "Werker":
            configs.append("Cloud Bees")
            values.append(223)
        if config != "Cloud Bees":
            values.append(data[config].sum())
    print(values)
    print(configs)
    total = sum(values)
    plt.ylim(0, 100)

    plot = plt

    plot.bar(configs, [(v / total) * 100 for v in values])
    plot.xlabel("Configuration")
    plot.ylabel("Percentage")
    plt.xticks(rotation=45)

    return plot

def create_percentage_bar_graphs(stars, xname, grouping_amount=540):
    # stars.sort(key=lambda x: x)
    print(stars)
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
        bottom.append(group[0])
        if len(group[1]) != 0:
            heights.append((sum(group[1]) / len(group[1])) * 100)
        else:
            heights.append(0)

    fig, ax = plt.subplots()

    # We need to draw the canvas, otherwise the labels won't be positioned and
    # won't have values yet.

    # so what happens here is we set the positions for all the bars
    # then with those positions we set the label
    # the key here that ax.bar primarily takes positions and then works out labels after that
    # so that means you can't try do clever stuff as it will work out the positions first which will muck up
    # all the things

    ax.bar(np.arange(len(bottom)), heights)
    plt.rc(({'font.size': 9}))
    plt.xticks(rotation=90)

    plt.ylim(0, 100)
    plt.xlabel(xname)
    plt.ylabel("percentage")
    labels = []
    for i in range(len(bottom)):
        if i == len(bottom) - 1:
            labels.append(str(bottom[i]))
        else:
            if i % 5 == 0:
                labels.append(str(bottom[i]))
            else:
                labels.append("")

    # this line is needed here
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=45, zorder=100)

    # ax.set_xticklabels(labels)
    return fig


def compare_coprus3(data, label):
    stars = {}
    for line in data:
        if stars.get(line) is None:
            stars[line] = 0

        stars[line] += 1

    return create_percentage_bar_graphs(stars, "percentage of stars that use CI", "stars")

def compare_coprus2(data, label):
    plot = plt
    bins = 15
    # K = 1 + 3. 322 logN
    bins = 1 + int(3.322 * math.log(len(data)))
    density = False
    log = True
    plt.xlim(0, 111000)
    plot.hist(data, bins, density=density, log=log, label=label, stacked=True)
    # plot.hist(data2["stargazers_count"], bins, density=density, log=log, label="2020")
    plot.xlabel("stars")
    plot.ylabel("density")
    plot.legend()
    return plot


def main(output, image_encoding):
    data = pd.read_csv("breadth_corpus.csv")
    data = data.fillna(0)
    data["CI_multi"] = data["Travis"] + data["AppVeyor"] + data["CircleCI"] + data["Werker"]
    data2 = pd.read_csv("combined9.csv")
    sorted_data = data[data["CI"] > 0]
    # write_to_latex(f"{output}/2016 usage first table raw data from corpus", len(data), sorted_data)
    # # save_as_pdf(compare_coprus(data, data2), f"{output}/comparison_corpus", image_encoding)
    #
    # # save_as_pdf(langs_topn(sorted_data, 20), f"{output}/comparison_langs_topn_sorted", image_encoding)
    # # save_as_pdf(langs_topn(data, 20), f"{output}/comparison_langs_topn", image_encoding)
    # # save_as_pdf(config_bar(data), f"{output}/comparison_config_bar", image_encoding)
    # config_bar(data)
    # df = languages_table_topn(30, data, sorted_data)
    #
    # print(df)
    # print(df["total count"].sum())
    # print(df["using CI"].sum())
    #
    # save_as_pdf(popularity_vs_percentage_CI_scatter(df, data), f"{output}/scatter", image_encoding)

    save_as_pdf(compare_coprus2(data["stars"], "2016"), f"{output}/density_2016", image_encoding)
    save_as_pdf(compare_coprus2(data2["stargazers_count"], "2020"), f"{output}/density_2020", image_encoding)

    # popularity_vs_percentage_CI_scatter
    return data


if __name__ == '__main__':
    data = main("results", "pdf")

    # sorted_data = data[data["CI"] > 0]
