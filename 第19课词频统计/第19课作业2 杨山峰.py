# -----------------载入库-------------------
import jieba
from pyecharts import options as opts
from pyecharts.charts import Pie

# ------------------数据准备------------------
with open("政府工作报告2021.txt", "r", encoding="UTF-8") as f:
    all_content1 = f.readlines()
with open("政府工作报告2022.txt", "r", encoding="UTF-8") as f:
    all_content2 = f.readlines()


# --------------------------定义函数-------------------
def all_cut(content):
    my_dict = {}
    for i in content:
        cut = jieba.cut(i)
        for word in cut:
            if len(word) == 2:
                my_dict[word] = my_dict.get(word, 0) + 1
    return my_dict


# -------------------主程序------------------
my_dict1 = all_cut(all_content1)
my_list1 = list(my_dict1.items())
my_list1.sort(key=lambda x: x[1], reverse=True)

my_dict2 = all_cut(all_content2)
my_list2 = list(my_dict2.items())
my_list2.sort(key=lambda x: x[1], reverse=True)
print("2021年政府工作报告二字高频词汇为：")
for i in range(20):
    print(my_list1[i][0], ":", my_list1[i][1])
print("2022年政府工作报告二字高频词汇为：")
for i in range(20):
    print(my_list2[i][0], ":", my_list2[i][1])
x_list1 = list(my_dict1.keys())
y_list1 = list(my_dict1.values())
x_list2 = list(my_dict2.keys())
y_list2 = list(my_dict2.values())

same_list_x = []
same_list_y = []
difference_list1_x = []
difference_list1_y = []

for x1 in x_list1:
    for x2 in x_list2:
        if x1 == x2:  # 共同的高频词
            if len(same_list_x) <= 10:  # 前十个
                same_list_x.append(x1)
                same_list_y.append(my_dict1[x1])
                break
        else:
            if len(difference_list1_x) <= 5:
                difference_list1_x.append(x1)
                difference_list1_y.append(my_dict1[x1])
pie1 = Pie()
pie2 = Pie()
data1 = []
data2 = []
for i in range(len(same_list_x)):
    data1.append((same_list_x[i], same_list_y[i]))
for i in range(len(difference_list1_x)):
    data2.append((difference_list1_x[i], difference_list1_y[i]))
pie1.add('', data1)
pie1.set_global_opts(title_opts=opts.TitleOpts(title='2021年政府报告高频二字词汇统计'))
pie2.add('', data2)
pie2.set_global_opts(title_opts=opts.TitleOpts(title='2022年政府报告高频二字词汇统计'))
pie1.render("比较.html")
pie2.render("比较.html")
