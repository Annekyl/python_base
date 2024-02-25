import random
import turtle

turtle.bgcolor("pink")
t1 = turtle.Pen()  # 写字
t1.color('black')
t2 = turtle.Pen()  # 画图案
t2.color("violet")
t3 = turtle.Pen()  # 画球
t4 = turtle.Pen()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
symbol = [
    #   1         2         3         4         5         6         7         8         9         10
    '\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264A', '\u264D', '\u2653', '\u264C', '\u264F',  # 1

    '\u2653', '\u264F', '\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264C', '\u264E', '\u264A',  # 2

    '\u2648', '\u2649', '\u264F', '\u2653', '\u264B', '\u264E', '\u264C', '\u264A', '\u2652', '\u264B',  # 3

    '\u264D', '\u2650', '\u2652', '\u264B', '\u2649', '\u264C', '\u2648', '\u264F', '\u264A', '\u264F',  # 4

    '\u264A', '\u2649', '\u264B', '\u2652', '\u264C', '\u264F', '\u2653', '\u2648', '\u2653', '\u2649',  # 5

    '\u2649', '\u264D', '\u264F', '\u264C', '\u2648', '\u2650', '\u264E', '\u2651', '\u264E', '\u264C',  # 6

    '\u2652', '\u2649', '\u264C', '\u2648', '\u264B', '\u264A', '\u2650', '\u264F', '\u264E', '\u264D',  # 7

    '\u264E', '\u264C', '\u2648', '\u2649', '\u264F', '\u264B', '\u264F', '\u2653', '\u264D', '\u264E',  # 8

    '\u264C', '\u264F', '\u264E', '\u264D', '\u2648', '\u2649', '\u264B', '\u2652', '\u264F', '\u264C',  # 9

    '\u264D', '\u2650', '\u2652', '\u264B', '\u2649', '\u264C', '\u2648', '\u264F', '\u2653', '\u264A'  # 10
]


def p(x, y):
    global k
    k = 1


def write1(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.write("想一个一百以内的数字\n将该数字减去个位数字和十位数字\n准备好后请点击屏幕",
             font=('华文仿宋', 30, "normal"))


def write2(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.write("是否是下面的图案", font=('华文仿宋', 30, "normal"))


def qiu(x, y):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.color("purple", "purple")
    t3.begin_fill()
    t3.circle(200)
    t3.end_fill()


num = random.randint(0, 99)
turtle.tracer(False)
y = 300
shuzi = 1
for i in range(10):
    x = 0
    for j in range(1, 11):
        t2.penup()
        t2.goto(x, y)
        t2.pd()
        num2 = random.randint(0, 99)
        if (j + 10 * i) % 9 == 0:
            t2.write(symbol[num], font=('华文仿宋', 40, "normal"))
            t2.penup()
            t2.goto(x + 10, y - 20)
            t2.pendown()
            t2.write(shuzi, font=('华文仿宋', 20, "normal"))
            shuzi += 1
        else:
            t2.write(symbol[num2], font=('华文仿宋', 40, "normal"))
            t2.penup()
            t2.goto(x + 10, y - 20)
            t2.pendown()
            t2.write(shuzi, font=('华文仿宋', 20, "normal"))
            shuzi += 1
        x += 65
    y -= 80
k = 0
turtle.onscreenclick(p)
qiu(-400, -300)
while 1:
    write1(-600, 300)
    if k == 1:
        t1.clear()
        write2(-600, 300)
        t4.pu()
        t4.goto(-530, -250)
        t4.pd()
        t4.color("blue")
        t4.write(symbol[num], font=('华文仿宋', 200, "normal"))
        break
    else:
        continue
turtle.mainloop()
