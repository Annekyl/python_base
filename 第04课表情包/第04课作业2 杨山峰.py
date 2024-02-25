#  ---------------载入库---------------
import turtle as t

t.speed(0)
t.hideturtle()


# ---------------模块---------------
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


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


def rectangle1(x, y):
    t.pensize(3)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("orange", "white")
    t.begin_fill()
    t.forward(90)
    t.circle(-5, 90)
    t.forward(20)
    t.circle(-5, 90)
    t.forward(90)
    t.circle(-5, 90)
    t.forward(20)
    t.circle(-5, 90)
    t.end_fill()


def rectangle2(x, y):
    t.pensize(3)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red", "white")
    t.begin_fill()
    t.forward(85)
    t.circle(-5, 90)
    t.forward(35)
    t.circle(-5, 90)
    t.forward(85)
    t.circle(-5, 90)
    t.forward(35)
    t.circle(-5, 90)
    t.end_fill()


def black(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(-17, 360)
    t.end_fill()


def half_circle(x, y):
    move(x, y)
    t.seth(-90)
    t.color("black", "black")
    t.begin_fill()
    t.circle(20, 180)
    t.end_fill()


# ---------------主程序---------------
# 左上笑脸
face(-200, 100)
eye1(-250, 300)  # 左眼大
eye2(-250, 300)  # 左眼小
eye1(-150, 300)  # 右眼大
eye2(-150, 300)  # 右眼小
t.seth(75)  # 设置绝对方向
smile(-120, 200, -150)  # 画微笑

# 右上哭脸
face(100, 100)
eye1(50, 300)  # 左眼大
eye2(50, 300)  # 左眼小
eye1(150, 300)  # 右眼大
eye2(150, 300)  # 右眼小
t.seth(103)  # 设置绝对方向
smile(180, 170, 150)  # 画哭泣

# 左下表情
face(-250, -300)  # 脸部
rectangle1(-365, -90)  # 左眼
half_circle(-340, -90)
t.seth(0)
rectangle1(-210, -90)  # 右眼
half_circle(-195, -90)
t.seth(0)
t.color("orange")
move(-270, -150)  # 嘴
t.forward(50)

# 右下表情
face(150, -300)  # 脸部
rectangle2(35, -90)  # 左眼
black(80, -95)
rectangle2(180, -90)  # 右眼
black(220, -95)
t.seth(-30)  # 微笑
smile(110, -200, 60)

t.mainloop()
