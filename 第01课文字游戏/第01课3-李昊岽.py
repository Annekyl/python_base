print("欢迎来到长大西校区")

a = input("你遇到了学姐帮你登记，请输入姓名:")

print("\n好的", a)

sex = input("请输入性别：")

if (sex == "男"):
    print("\n收到", a, "先生")
    c = input("\n敢问贵庚？")
    c = int(c)
    if (c >= 20):
        print("好的，前辈")
    else:
        print("我带你飞，小弟弟")

if (sex == "女"):
    print("\n收到", a, "女士")
    d = input("请问芳龄几许？\n ")
    d = int(d)
    if (d >= 20):
        print("女侠跟我来")
    else:
        print("小姐姐加个微信，跟我来")
print("\n你到达了校门口，你想向那边走？")
point = 1
while (1):
    if point == 1:
        a = input("\n1.左边 2.直行 3.右边\n4.回头\n")
        if (a == "1"):
            print("\n你来到了农科大楼\n")
            point = 2
        if (a == "2"):
            print("\n你看到了校医院，选择其他路或许会用到\n")
            point = 3
        if (a == "3"):
            print("\n你在6，7教间发现了漂亮学姐\n")
            point = 4
        if (a == "4"):
            print("\n触发事件“鬼打墙”\n你迷失了\n")
            point = 5

    if point == 2:
        print("\n农科大楼欢迎您，你发现了一只修狗\n")
        a = input("\n是否挑逗它\n1是   2否\n")
        if (a == "1"):
            print("\n你被修狗咬伤了\n")
            point = 6
        if (a == "2"):
            print("\n什么事都没有发生，你回到校门口准备看看别的\n")
            point = 1

    if point == 3:
        a = input("\n1接受治疗\n2返回校门口\n3去6，7教看看")
        if (a == "1"):
            print("\n你被治好了，并开始了美好的大学生活并决定返回校门口参观\n")
            point = 1
        if (a == "2"):
            print("\n你回到了校门口\n")
            point = 1
        if (a == "3"):
            print("\n你在6，7教间发现了漂亮学姐\n")
            point = 4

    if point == 4:
        a = input("\n1耍帅吸引她的注意\n2主动加微信\n3不感兴趣去农科看看")
        if (a == "1"):
            print("\n你发现没什么用，默默的回到校门口\n")
            point = 1
        if (a == "2"):
            print("\n你被无情拒绝了，决定去农科看看\n")
            point = 2
        if (a == "3"):
            print("有志向的你想去医院看看")
            point = 3

    if point == 5:
        a = input("\n1稳重的回到校门口\n2一意孤行，继续出校\n")
        if (a == "1"):
            print("\n你回到校门口\n")
            point = 1
        if (a == "2"):
            print("\n你误入地狱\n")
            point = 7

    if point == 6:
        a = input("\n1前往医院\n爱咋咋地，我不管\n")
        if (a == "1"):
            print("\n你到医院了\n")
            point = 3
        if (a == "2"):
            print("\n你失血过多被送往大医院后，康复回到校门口\n")
            point = 1

    if point == 7:
        a = input("\n1向相关人员报告情况\n2自己寻找出路\n")
        if (a == "1"):
            print("\n你被送回校门口\n")
            point = 1
        if (a == "2"):
            print("\n你嘎了，重生回到校门口\n")
            point = 4
            break
