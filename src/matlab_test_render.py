"""
exporting to latex guide: https://timodenk.com/blog/exporting-matplotlib-plots-to-latex/

graphing guides:
- https://matplotlib.org/3.1.1/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py



"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import numpy as np
import csvReader


# mplstyle.use(['dark_background', 'ggplot', 'fast'])


def spread_of_data_sub_to_stars(axis, data):
    plt.xlabel('stars')
    plt.ylabel('subscribers')

    x = []
    y = []
    for line in data:
        x.append(int(line.get("stargazers_count")))
        y.append(int(line.get("subscribers_count")))
    print(len(x))
    plt.scatter(x, y, s=1, alpha=0.75)

    plt.title("Sample of repositories from github")

    # plt.legend()

    # plt.show()
    plt.savefig(f'spreadscatter_starsandsubs.pdf')


def spread_over_time_stars_pgf(axis, data):
    """
    this seems bad atm
    :param axis:
    :param data:
    :return:
    """
    # matplotlib.use("pgf")
    #
    # matplotlib.rcParams.update({
    #     "pgf.texsystem": "pdflatex",
    #     'font.family': 'serif',
    #     'text.usetex': True,
    #     'pgf.rcfonts': False,
    # })

    plt.ylabel('stars')

    x = []
    for line in data:
        x.append(int(line.get("stargazers_count")))

    print(len(x))
    x.sort()

    count = 0
    for a in x:
        if a == 0:
            count += 1

    print(count)
    print(x[:10])
    plt.scatter(list(range(len(x))), x, s=0.5)

    plt.title("Sample of repositories from github")
    export_to_latex(plt, "dogs")

    # plt.legend()

    plt.show()
    # plt.savefig(f'latex thing.pgf')


def spread_over_time_stars_pdf(axis, data):
    """
    this seems bad atm
    :param axis:
    :param data:
    :return:
    """
    plt.ylabel('stars')

    x = []
    for line in data:
        x.append(int(line.get("stargazers_count")))

    print(len(x))
    x.sort()

    plt.scatter(list(range(len(x))), x, s=0.5)

    plt.title("Sample of repositories from github")

    name = "sample over time"

    plt.savefig(f'{name}.pdf', format="pdf")



def export_to_latex(plot, name):
    pass



def main():
    data = csvReader.readfile("combined0.csv")

    spread_over_time_stars_pdf(plt, data)
    # spread_of_data_sub_to_stars(plt,data)


if __name__ == '__main__':
    main()
