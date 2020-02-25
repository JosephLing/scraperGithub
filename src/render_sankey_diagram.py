import math
import plotly.graph_objects as go
import pandas as pd
import plotly
from data_parser import dtypes


def load_dataframe(name):
    return pd.read_csv(name, dtype=dtypes)

    
def save_sanky_daigram_for_errors_and_comments(name, dataset, normalise, medain, encoding="svg"):
    df = dataset.groupby(['config', 'yaml_encoding_error']).size().unstack(fill_value=0)
    df_configs = dataset[dataset['yaml_encoding_error'].isnull()]["config"].value_counts()
    # df_comments = dataset[dataset["yaml"] & (dataset["yaml_encoding_error"].isnull())]

    # labels is errors, config, valid config, comments, blank lines, code
    labels = list(df.keys())
    for i in df.index:
        labels.append(i)    

    for i in df.index:
        labels.append("{} valid".format(i))

    labels.append("comments")
    labels.append("blank lines")
    labels.append("code")

    sources = []
    targets = []
    values = []
    for k in range(len(df.keys())):
        for v in range(len(df[df.keys()[k]])):
            if df[df.keys()[k]][v] != 0:
                sources.append(4 + v)
                targets.append(k)
                values.append(df[df.keys()[k]][v])

    for i in range(len(df.index)):
        sources.append(4 + i)
        targets.append(8 + i)
        values.append(df_configs[df.index[i]])

    comments = []
    blank = []
    code = []
    for i in range(len(df.index)):
        config_comments = dataset[dataset["yaml"] & (dataset["yaml_encoding_error"].isnull())][
            dataset["config"] == df.index[i]]
        if medain:
            comments.append(config_comments[dataset["comments"].notnull()]["comments"].median())
            blank.append(config_comments[dataset["blank_lines"].notnull()]["blank_lines"].median())
            code.append(config_comments[dataset["code"].notnull()]["code"].median())
        else:
            comments.append(config_comments[dataset["comments"].notnull()]["comments"].mean())
            blank.append(config_comments[dataset["blank_lines"].notnull()]["blank_lines"].mean())
            code.append(config_comments[dataset["code"].notnull()]["code"].mean())

        
    for i in range(len(comments)):
        total = comments[i] + blank[i] + code[i]
        if not normalise:
            comments[i] = (comments[i] / total) * df_configs[df.index[i]]
            blank[i] = (blank[i] / total) * df_configs[df.index[i]]
            code[i] = (code[i] / total) * df_configs[df.index[i]]
        else:
            comments[i] = (comments[i] / total) * math.log2(df_configs[df.index[i]])
            blank[i] = (blank[i] / total) * math.log2(df_configs[df.index[i]])
            code[i] = (code[i] / total) * math.log2(df_configs[df.index[i]])

    for i in range(len(df.index)):
        sources.append(8 + i)
        targets.append(12)
        values.append(comments[i])

    for i in range(len(df.index)):
        sources.append(8 + i)
        targets.append(13)
        values.append(blank[i])

    for i in range(len(df.index)):
        sources.append(8 + i)
        targets.append(14)
        values.append(code[i])

    if normalise:
        # the last 12 values are those that are the comments and they are already normalised
        # when they are caculated
        for i in range(len(values)-12):
            if values[i] > 0:
                values[i] = math.log2(values[i])

    # the first 3 things are the errors and we want them to have different positions
    # therefore we set the x,y values of them and the rests use the arrangement 'snap'
    fig = go.Figure(data=[go.Sankey(
        arrangement="snap",
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            x=[0.5, 0.5, 0.5],
            y=[-0.5, -0.5, -0.5],
            label=labels,
            color="blue"
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values
        ))])

    fig.update_layout(title_text="Analysis of yaml continous integeration file formats", font_size=10)
    # fig.write_html('first_figure.html', auto_open=True)
    plotly.io.write_image(fig, f"{name}.{encoding}")


if __name__ == "__main__":
    dataset = load_dataframe("yaml threaded6.csv")
    save_sanky_daigram_for_errors_and_comments("1",dataset, True, True)
    save_sanky_daigram_for_errors_and_comments("2",dataset, False, True)
    save_sanky_daigram_for_errors_and_comments("3",dataset, True, False)
    save_sanky_daigram_for_errors_and_comments("4",dataset, False, False)
