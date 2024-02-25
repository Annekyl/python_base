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

print("你来到了长江大学西校区门口")
point = 1
q = input("请选择：1:左边3教  2:中间1教  3:右边2教")

while 1:  # 循环
    if q == "1":
        print("你选择了左边3教")
        break
    if q == "2":
        print("你选择了中间1教")
        break
    if q == "3":
        print("你选择了右边2教")
        break
