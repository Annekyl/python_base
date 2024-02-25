import re
from pyecharts.charts import Bar

total_dx = []  # 统计大学
total_xy = []  # 统计学院
f = open("慕课MOOC.txt", "r", encoding="UTF-8")
for line in f:
    if "alt=" in line:
        name = re.findall(r'[\u4e00-\u9fa5]+', line)
        name = name[0]
        check = name[-2::1]
        if check == "大学":
            total_dx.append(name)
        if check == "学院":
            total_xy.append(name)
print(f"大学共有{len(total_dx)}所")
for i in total_dx:
    print(i, end='\t')
print(f"\n学院共有{len(total_xy)}所")
for i in total_xy:
    print(i, end='\t')
my_list1 = ['大学', "学院"]
my_list2 = [len(total_dx), len(total_xy)]
Bar().add_xaxis(my_list1).add_yaxis("统计", my_list2).render("统计图.html")
