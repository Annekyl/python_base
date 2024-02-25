import random

x = random.randint(1, 100)
while 1:
    m = eval(input("请输入你猜测的数字"))
    if m > x:
        print("大了")
    if m < x:
        print("小了")
    if m == x:
        print("对了")
        break
