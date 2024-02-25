import turtle
import time
import random

t1 = turtle.Pen()  # 写标题
t2 = turtle.Pen()  # 计时
t3 = turtle.Pen()  # 画扑克牌
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()


def write():
    t1.penup()
    t1.goto(-200, 200)
    t1.pendown()
    t1.write("记忆大比拼", font=("华文仿宋", 50, "normal"))


def move(x, y, z):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.seth(z)


def block(x, y):
    move(x, y, 0)
    t3.color("black", "white")
    t3.begin_fill()
    t3.forward(45.6)
    t3.right(90)
    t3.forward(70.4)
    t3.right(90)
    t3.forward(45.6)
    t3.right(90)
    t3.forward(70.4)
    t3.end_fill()


def draw(x1, y1, x2, y2, x3, y3, x4, y4, num, little_flower, big_flower, pencolor):
    move(x1, y1, -90)
    t3.write(num, font=("微软雅黑", 12, "normal"))
    move(x2, y2, -90)
    t3.color(pencolor)
    t3.write(little_flower, font=("微软雅黑", 12, "normal"))
    move(x3, y3, 0)
    t3.write(big_flower, font=("微软雅黑", 30, "normal"))
    move(x4, y4, 0)


ch1 = '\u2665'  # 红心
ch2 = '\u2660'  # 黑桃
ch3 = '\u2666'  # 方块
ch4 = '\u2663'  # 梅花
pk = ["A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      ]
color = [ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1,
         ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2,
         ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3,
         ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4,
         ]
pen_color = ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red",
             "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
             "black",
             "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red",
             "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
             "black", ]

while 1:
    write()
    x = -200
    y = 100
    for i in range(4):
        turtle.tracer(False)
        send = random.randint(0, 51)
        block(x, y)
        draw(x + 5, y - 20, x + 3, y - 35, x + 10, y - 60, x, y, pk[send], color[send], color[send],
             pen_color[send])
        turtle.tracer(True)
        x += 100
    t2.penup()
    t2.goto(-100, -150)
    t2.pendown()
    num = 3
    for i in range(4):
        t2.write(num, font=("华文仿宋", 50, "normal"))
        time.sleep(1)
        num -= 1
        t2.clear()
    t1.clear()
    t3.clear()
    t1.penup()
    t1.goto(-200, 200)
    t1.pendown()
    t1.write("请回忆扑克牌", font=("华文仿宋", 50, "normal"))
    num = 10
    for i in range(11):
        t2.write(num, font=("华文仿宋", 50, "normal"))
        time.sleep(1)
        num -= 1
        t2.clear()
    t1.clear()
