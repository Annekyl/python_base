# -----------------载入库-------------------
import jieba
import pyecharts

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
x_list1 = x_list1[0:20:1]
y_list1 = list(my_dict1.values())
y_list1 = y_list1[0:20:1]
x_list2 = list(my_dict2.keys())
x_list2 = x_list2[0:20:1]
y_list2 = list(my_dict2.values())
y_list2 = y_list2[0:20:1]
for i in range(20):
    x_list1.append(my_dict1)
picture1 = pyecharts.charts.Bar()\
    .add_xaxis(x_list1)\
    .add_yaxis("出现次数", y_list1)\
    .render("2021年政府报告高频二字词汇.html")
picture2 = pyecharts.charts.Bar()\
    .add_xaxis(x_list2)\
    .add_yaxis("出现次数", y_list2)\
    .render("2022年政府报告高频二字词汇.html")
