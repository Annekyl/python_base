# -----------------------载入库-------------------------
import re
from collections import Counter


# ----------------------主程序---------------------
# 读取《三国演义》文本文件
with open('sg（原文）.txt', 'r', encoding='utf-8') as file:  # 读取文件
    text = file.read()
dialogues = re.findall(r'[\u4e00-\u9fa5]{2,5}：“.*?”', text)  # 通过正则表达式找到人说的话
for i in dialogues:  # 查看说的话
    print(i)
