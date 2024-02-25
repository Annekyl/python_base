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


