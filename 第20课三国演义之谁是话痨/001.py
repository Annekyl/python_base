import openpyxl

f = open("任务1.txt", "rb")  # rb表示以二进制模式读取文件
# print(f.tell())
# f.seek(5)
# f.seek(-2, 2)
# print(f.tell())
a = f.readlines()
print(a)
f.close()
f = open("任务1.txt", "r", encoding="UTF-8")
content = f.readlines()
f.close()
print(content)
