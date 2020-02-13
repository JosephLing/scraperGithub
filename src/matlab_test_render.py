"""
exporting to latex guide: https://timodenk.com/blog/exporting-matplotlib-plots-to-latex/

graphing guides:
- https://matplotlib.org/3.1.1/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py



"""

import matplotlib.pyplot as plt
import csvReader


def spread_of_data_sub_to_stars(plot, data):
    plot.xlabel('stars')
    plot.ylabel('subscribers')

    x = []
    y = []
    for line in data:
        x.append(int(line.get("stargazers_count")))
        y.append(int(line.get("subscribers_count")))
    print(len(x))
    plot.scatter(x, y, s=1, alpha=0.75)

    plot.title("Sample of repositories from github")

    plot.legend()
    return plot


def save_as_pdf(plot, name):
    plot.savefig(f'{name}.pdf', format="pdf")

def spread_over_time_stars(plot, data):
    plot.ylabel('stars')
    x = []
    for line in data:
        x.append(int(line.get("stargazers_count")))

    x.sort()
    plot.scatter(list(range(len(x))), x, s=0.5)

    plot.title("Sample of repositories from github")

    return plot


def main():
    data = csvReader.readfile("combined0.csv")
    save_as_pdf(spread_of_data_sub_to_stars(plt, data), "sub vs stars")
    save_as_pdf(spread_over_time_stars(plt, data), "spread over time")


if __name__ == '__main__':
    main()
