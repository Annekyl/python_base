#  载入库
import turtle as t

t.speed(0)
t.hideturtle()


# 模块
def face(x, y):  # 脸部
    t.pensize(3)
    t.seth(0)
    t.color("orange", "yellow")
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(150)
    t.end_fill()


def eye1(x, y):  # 大眼
    t.pensize(2)
    t.color("orange", "white")
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(30)
    t.end_fill()


def eye2(x, y):  # 小眼
    t.pensize(1)
    t.color("black", "black")
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(18)
    t.end_fill()


def smile(x, y, z):  # 弧度
    t.pensize(3)
    t.color("orange")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(80, z)


# 主程序
face(-200, -100)  # 画左侧笑脸
eye1(-250, 100)
eye2(-250, 100)
eye1(-150, 100)
eye2(-150, 100)
t.seth(75)
smile(-120, 0, -150)
face(100, -100)  # 画右侧哭脸
eye1(50, 100)
eye2(50, 100)
eye1(150, 100)
eye2(150, 100)
t.seth(103)
smile(180, -30, 150)
t.mainloop()
