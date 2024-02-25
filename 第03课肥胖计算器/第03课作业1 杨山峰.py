# 绩点计算器
print("欢迎使用绩点计算器\n")
a = "1"
# 循环
while a == "1":  # 输入成绩
    m = float(input("请输入高数成绩\n"))
    e1 = float(input("请输入英语读写成绩：\n"))
    e2 = float(input("请输入英语听说成绩：\n"))
    c = float(input("请输入计算机导论成绩：\n"))
    # 计算数学单科绩点
    if m >= 60:
        math = float((m - 50) / 10 * 4)
    if m < 60:
        math = float(0)
    # 计算英语读写单科绩点
    if e1 >= 60:
        english1 = float((e1 - 50) / 10 * 5)
    if e1 < 60:
        english1 = float(0)
    # 计算英语听说单科绩点
    if e2 >= 60:
        english2 = float((e2 - 50) / 10 * 2)
    if e2 < 60:
        english2 = float(0)
    # 计算计算机导论单科绩点
    if c >= 60:
        computer = float((c - 50) / 10 * 2)
    if c < 60:
        computer = float(0)
    # 计算总绩点
    print("您的总绩点为:")
    GPA = ((math + english1 + english2 + computer) / 13)
    print("您的绩点为%.2f" % GPA)
    # 是否循环
    print("还要再玩吗？\n")
    a = input("1.继续 2.不玩了")
