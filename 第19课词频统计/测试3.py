from pyecharts.charts import Pie
from pyecharts import options as opts
from collections import Counter

# 示例数据
data = [
    [
        "分类 A",
        Counter([
            "子分类 A1",
            "子分类 A2",
            "子分类 A3",
        ])
    ],
    [
        "分类 B",
        Counter([
            "子分类 B1",
            "子分类 B2",
            "子分类 B3",
        ])
    ],
    [
        "分类 C",
        Counter([
            "子分类 C1",
            "子分类 C2",
            "子分类 C3",
        ])
    ],
]

def draw_pie_charts(data):
    pies = []
    for i, item in enumerate(data):
        pie = Pie()
        pie.add_schema(
            name=item[0],
            series=[
                opts.PieInnerItem(
                    name=k,
                    value=v,
                    radius="50%",
                    center=["50%", "50%"],
                )
                for k, v in item[1].items()
            ],
        )
        pies.append(pie)

    for i, pie in enumerate(pies):
        pie.set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"{data[i][0]}详细数据",
                left="50%",
                textstyle_opts=opts.TextStyleOpts(color="red"),
            ),
             ToolTipOpts(trigger="item", axis_pointer_type="cross"),
             visualmap_opts=opts.VisualMapOpts(
                 max_=max(pie.data()[1].values()),
                 min_=min(pie.data()[1].values()),
                 range_color=[
                     "blue",
                     "navy",
                     "purple",
                     "red",
                     "lightcoral",
                     "dodgerblue",
                 ],
                 is_piecewise=True,
             ),
             label_opts=opts.LabelOpts(is_show=True),
             grid_opts=opts.GridOpts(is_show=True),
             legend_opts=opts.LegendOpts(is_show=True),
        )

    for pie in pies:
        pie.render("./png/{}.png".format(i))

if __name__ == "__main__":
    draw_pie_charts(data)
