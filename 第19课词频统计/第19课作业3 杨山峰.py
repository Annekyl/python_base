f1 = open("论语解读版本.txt", "r", encoding="UTF-8")
f2 = open("论语.txt", "w", encoding="utf-8")
data = ''  # 用于储存要写入的数据
a = 0  # 用于判断行是否需要写入
for line in f1:  # 遍历每一行
    line = line.strip()  # 去除前后空格和换行符

    if line.count("【原文】") != 0:  # 原文下面的内容要写
        a = 1
    if line.count("【注释】") != 0:  # 注释下面的内容不写
        a = 0
    if a == 1 and line.count("【原文】") == 0 and line.count("【注释】") == 0 and len(line) != 0:
        data += line + "\n"

data = data.replace("(", "")  # 去掉左括号
data = data.replace(")", "")  # 去掉右括号
for i in range(10):  # 去掉数字
    data = data.replace(f"{i}", "")
f2.write(data)  # 将数据写入文件中
f1.close()  # 关闭读取文件
f2.close()  # 关闭写入文件
