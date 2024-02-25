# 汉诺塔最终图形版
import turtle
import time

tower = [[-250, -100], [250, -100], [-150, -100], [-150, 100], [0, -100], [0, 100], [150, -100], [150, 100]]


# 数据描述：塔底线左点，塔底线右点， A柱下点，A柱上点  ，B柱下点，B柱上点， C柱下点，C柱上点

def draw_line(x1, y1, x2, y2):  # 画一条线
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()
    t1.goto(x2, y2)


def draw_tower():  # 画汉诺塔背景：三根柱子一条底线
    t1.speed(0)
    for i in range(0, len(tower), 2):
        draw_line(tower[i][0], tower[i][1], tower[i + 1][0], tower[i + 1][1])
    time.sleep(2)


def draw_plate(x, y, lss):  # 画一个柱子上全部盘子：(x,y)为柱子的起点（下点）坐标，lss为柱子盘子数据
    t2.penup()
    t2.goto(x, y + 20)
    t2.pendown()
    for i in range(len(lss)):
        t2.forward(lss[i] * 20)
        t2.backward(lss[i] * 40)
        t2.forward(lss[i] * 20)
        t2.goto(x, y + 20 * (i + 2))


def draw_plates():  # 画三个柱子的全部盘子
    turtle.tracer(0)
    t2.clear()
    draw_plate(tower[2][0], tower[2][1], a)  # A柱坐标
    draw_plate(tower[4][0], tower[4][1], b)  # B柱坐标
    draw_plate(tower[6][0], tower[6][1], c)  # C柱坐标
    turtle.tracer(1)
    time.sleep(2)


def han(n, x, y, z):
    if n == 1:
        z.append(x[len(x) - 1])  # print(x,'移动到',z)
        del x[len(x) - 1]
        print(a, b, c)
        draw_plates()

    else:
        han(n - 1, x, z, y)  # 1
        z.append(x[len(x) - 1])  # print(x,'移动到',z)
        del x[len(x) - 1]
        print(a, b, c)
        draw_plates()
        han(n - 1, y, x, z)  # 2


# ---------初始化画笔----------
t1 = turtle.Pen()
t2 = turtle.Pen()
t1.hideturtle()
t2.hideturtle()
t1.pensize(15)
t2.pensize(15)

# ---------初始化柱子的数据----------
a = [3, 2, 1]
b = []
c = []
print(a, b, c, '\n')

draw_tower()  # 画汉诺塔背景
draw_plates()  # 画初始的盘子
han(3, a, b, c)  # 使用递归法移动盘子
