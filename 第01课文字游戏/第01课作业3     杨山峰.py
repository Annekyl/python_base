a = input("请输入你的姓名\n")
b = input("请输入你的性别\n")
c = input("请输入你的年龄\n")
d = int(c)

if b == "男" and d <= 20:
    print("\n少年出英雄啊\n")
    print("\n欢迎你，勇士\n")
if b == "男" and d >= 20:
    print("\n你是个老江湖啊")
    print("\n欢迎你，勇士\n")
if b == "女" and d <= 20:
    print("\n少年出英雄啊\n")
    print("\n欢迎你，美女\n")
if b == "女" and d >= 20:
    print("\n你是个老江湖了啊\n")
    print("\n欢迎你，美女\n")

print("你来到了学校门口")
point = 1
while 1:  # 循环
    if point == 1:
        q = input("\n请选择：1:左边3教  2:中间1教  3:右边2教\n")

        if q == "1":
            print("\n你选择了右边2教\n")
            point = 2
        if q == "2":
            print("\n你选择了中间1教\n")
            point = 3
        if q == "3":
            print("\n你选择了左边3教\n")
            point = 4

    if point == 2:
        print("\n你到达了右边2教\n")
        w = input("你选择 1:进入2教上课 2:继续向前去6-7教 3:前往体育馆\n")
        if w == "1":
            print("终于下课了，你决定\n")
            e = input("1:去吃饭 2:回宿舍\n")
            if e == "1":
                print("\n吃完饭了，你回到了宿舍睡觉\n")
                print("\n你结束了在学校的一天，goodbye\n")
                print("游戏结束")
                break
            if e == "2":
                print("\n经过一天的旅途，你感到很累\n")
                print("你一上床就睡着了，goodbye\n")
                print("游戏结束")
                break
        if w == "3":
            print("你遇到了大二的学长\n")
            print("学长邀请你一起打篮球\n")
            r = input("你选择1:接受 2：拒绝")
            if r == "1":
                print("\n你与学长打的酣畅淋漓，虽然你输掉了比赛。。。\n")
                print("\n你感到很疲惫，于是回到了宿舍睡觉\n")
                break
            if r == "2":
                print("\n虽然你拒绝了学长的邀请，学长并没有生气\n")
                print("他们表示希望有机会可以一起打球")
                break
        if w == "2":
            print("你进入了6-7教\n")
            print("你开始上课了\n")
            input("在课堂上，你决定1:摸鱼 2:认真听讲\n")
            print("终于下课了，你决定\n")
            e = input("1:去吃饭 2:回宿舍\n")
            if e == "1":
                print("\n吃完饭了，你回到了宿舍睡觉\n")
                print("\n你结束了在学校的一天，goodbye\n")
                print("游戏结束")
                break
            if e == "2":
                print("\n经过一天的旅途，你感到很累\n")
                print("你一上床就睡着了，goodbye\n")
                print("游戏结束")
                break

    if point == 3:
        print("你进入了1号教学楼，你选择\n")
        e = input("1:上理论课 2:上实验课\n")
        if e == "1":
            input("在课堂上，你决定1:摸鱼 2:认真听讲\n")
            print("上完课的你疲惫不堪，你决定回宿舍大睡一觉\n")
            print("游戏结束")
            break
        if e == "2":
            print("看到千奇百怪的实验器材,你倍感兴奋\n")
            input("你选择：1：上手操作 2：观察老师做实验\n")
            print("然而愉快的时间总是短暂的，很快就下课了\n")
            print("goodbye!\n")
            print("游戏结束")
            break
    if point == 4:
        print("\n你到达了3教\n")
        a = input("你选择：1：去上课 2：继续前进\n")
        if a == "1":
            print("你开始上课了\n")
            input("在课堂上，你决定1:摸鱼 2:认真听讲\n")
            print("终于下课了，你决定\n")
            e = input("1:去吃饭 2:回宿舍\n")
            if e == "1":
                print("\n吃完饭了，你回到了宿舍睡觉\n")
                print("\n你结束了在学校的一天，goodbye\n")
                print("游戏结束")
                break
            if e == "2":
                print("\n经过一天的旅途，你感到很累\n")
                print("你一上床就睡着了，goodbye\n")
                print("游戏结束")
                break
        if a == "2":
            print("你到达了西2食堂，你决定在这里吃饭\n")
            input("你选择吃：1：麻辣烫 2：面食 3：米饭\n")
            print("吃饱喝足，你决定会宿舍睡一觉\n")
            print("游戏结束")
