import turtle
import time

t1 = turtle.Pen()
t2 = turtle.Pen()
t1.hideturtle()
t2.hideturtle()


def move(t, a, b):
    t.seth(0)
    t.pu()
    t.goto(a, b)
    t.pd()


def straight(t, a, b):
    move(t, a, b)
    t.seth(90)
    t.fd(500)
    move(t, a - 100, b)
    t.fd(200)


def plate(t, a, b, c, d):
    move(t, a, b)
    t.color("purple", "pink")
    t.begin_fill()
    t.fd(c)
    t.right(90)
    t.fd(d)
    t.right(90)
    t.fd(c)
    t.right(90)
    t.forward(d)
    t.end_fill()


def hannuota(i, A, B, C):  # i为汉诺塔层数，参数A为起始柱子，参数B为中转柱子，参数C为目标柱子
    if i == 1:
        print(A, "移动到", C)  # 将盘子从传入的第一个塔移动到第三个塔
    else:
        hannuota(i - 1, A, C, B)  # 如果不是最下面的盘子，调换目标位置为中转柱子
        print(A, "移动到", C)  # 此时塔1上已经只剩下一个盘子，移到目标柱子
        hannuota(i - 1, B, A, C)  # 将剩下的盘子通过起始柱子移到目标柱子


# 画汉诺塔
my_list = [t1, t2, t3]
my_place = []
m = -250
n = -220
for i in range(3):
    straight(t4, m, n)
    m += 300

# 画盘子
x = -330
y = -200
length = 150
width = 20
for i in my_list:
    plate(i, x, y, length, width)
    length -= 30
    x += 15
    y += width

# 移动盘子


turtle.tracer(True)
turtle.mainloop()
