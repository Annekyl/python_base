from pyecharts.charts import Pie, Grid
from pyecharts import options as opts

# 创建第一个饼状图数据
data1 = [("A", 30), ("B", 20), ("C", 50)]
pie1 = (Pie()
        .add("", data1)
        .set_global_opts(title_opts=opts.TitleOpts(title="饼状图1")))

# 创建第二个饼状图数据
data2 = [("D", 40), ("E", 60), ("F", 10)]
pie2 = (Pie()
        .add("", data2)
        .set_global_opts(title_opts=opts.TitleOpts(title="饼状图2")))

# 使用Grid组件将两个饼状图放在同一个网格中
grid = (Grid()
        .add(pie1, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%"))
        .add(pie2, grid_opts=opts.GridOpts(pos_left="60%", pos_right="95%")))

# 渲染图表并保存为HTML文件
grid.render("pie_charts.html")
