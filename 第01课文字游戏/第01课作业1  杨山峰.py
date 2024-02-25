a = input("请输入你的姓名")
b = input("请输入你的性别")
c = input("请输入你的年龄")
d = int(c)

if b == "男" and d <= 20:
    print("少年出英雄啊")
    print("欢迎你，勇士")
if b == "男" and d >= 20:
    print("你是个老江湖啊")
    print("欢迎你，勇士")
if b == "女" and d <= 20:
    print("少年出英雄啊")
    print("欢迎你，美女")
if b == "女" and d >= 20:
    print("你是个老江湖了啊")
    print("欢迎你，美女")
