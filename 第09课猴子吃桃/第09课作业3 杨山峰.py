# 抢30
print("欢迎使用抢30作弊器(规则：每次可以说最多2个数)")
start = int(input("请选择：1.先手 2.后手"))
if start == 2:
    print("请说到3")
    while 1:
        num = int(input("请输入对方的最后一个数字"))
        i = num % 3
        num = num + 3 - i
        print(f"请说到{num}")
        if num == 30:
            print("游戏结束")
            break
if start == 1:
    print("不一定会赢")
    print("说到1和2均可以")
    while 1:
        num = int(input("请输入对方的最后一个数字"))
        i = num % 3
        if i != 0:
            num = num + 3 - i
            print(f"请说到{num}")
        if i == 0:
            print("说1或2个数字均可")
        if num == 30:
            print("游戏结束")
            break
