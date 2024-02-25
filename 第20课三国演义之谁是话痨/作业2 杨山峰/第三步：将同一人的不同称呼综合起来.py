import re
from collections import Counter

# 读取《三国演义》文本文件
with open('sg（原文）.txt', 'r', encoding='utf-8') as file:  # 读取文件
    text = file.read()

# 通过正则表达式提取人物对话
dialogues = re.findall(r'[\u4e00-\u9fa5]{2,5}：“.*?”', text)  # 通过正则表达式找到人说的话
print(dialogues)
# 统计每个人物的说话字数
word_count = Counter()  # 类似于字典，键值对中的值用来计数

for dialogue in dialogues:
    # 提取人物名称
    match = re.match(r'([\u4e00-\u9fa5]{2,5})：“.*?”', dialogue)  # 将说话前的内容加括号用group显示
    if match:
        character = match.group(1)  # 说话前的字
        # 统计字数
        words = re.findall(r'[^\u4e00-\u9fa5\s]', dialogue)
        word_count[character] += len(words)

# 打印人物说话字数统计结果
for character, count in word_count.most_common():
    print(f'{character}: {count}字 ')
# m=word_count["大惊曰"]
# print(m)
a = {}
a["诸葛亮"] = word_count["孔明曰"] + word_count["孔明笑曰"] + word_count["孔明答曰"] + word_count["孔明暗思"] \
              + word_count["孔明厉声曰"] + word_count["孔明又曰"] + word_count["明仰面笑曰"] + \
              word_count["孔明亦谢曰"] + word_count["孔明喜曰"] + word_count["孔明大惊曰"]
a["周瑜"] = word_count["瑜曰"] + word_count["瑾曰"] + word_count["瑜笑曰"] + word_count["瑜执干手曰"] \
            + word_count["瑜令众将曰"] + word_count["周瑜曰"] + word_count["瑜怒曰"] + word_count["瑜懊悔曰"] + \
            word_count["周瑜笑曰"] + word_count["瑜思曰"] + word_count["瑜告众官曰"] + word_count["周瑜大喜曰"] + \
            word_count["瑜惊曰"] + \
            word_count["瑜喝"] + word_count[""] + word_count["瑜又问"]
a["孙权"] = word_count["权曰"] + word_count["权抚瑜背曰"] + word_count["权矍然起曰"] + word_count["权叹曰"] \
            + word_count["权大悦曰"] + word_count["瑜问"] + word_count["孙权曰"]
a["鲁肃"] = word_count["肃曰"] + word_count["鲁肃愕然曰"] + word_count["鲁肃入见曰"] + word_count["肃责孔明曰"] \
            + word_count["肃先问瑜曰"] + word_count["肃密谓瑜曰"] + word_count["鲁肃曰"] + word_count["肃问瑜曰"] + \
            word_count["鲁肃入问曰"] + word_count[
                "肃谓孔明曰"] + word_count["鲁肃看毕曰"] + word_count["鲁肃看毕曰"] + word_count["肃手而言曰"] + \
            word_count["鲁肃大怒曰"]
a["刘备"] = word_count["玄德曰"] + word_count["玄德聚众曰"] + word_count["玄德愕然曰"]
a["曹操"] = word_count["操曰"] + word_count["操怒曰"] + word_count["操问"] + word_count["操问众将曰"] + word_count[
    "操问曰"] + word_count["操大怒曰"] + word_count["操方省悟曰"]
print(a)
