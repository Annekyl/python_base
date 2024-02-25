# --------------载入库---------------
import turtle as t

t.speed(0)
t.hideturtle()


# --------------模块-----------------
def roundness(a, b):  # 圆
    t.color("white", a)
    t.begin_fill()
    t.circle(b)
    t.end_fill()


def move(x, y):  # 画笔移动到（x,y）位置处
    t.penup()
    t.goto(x, y)
    t.pendown()


def star():  # 五角星
    t.color("white", "white")
    t.begin_fill()
    t.forward(110)
    t.right(144)
    t.forward(110)
    t.right(144)
    t.forward(110)
    t.right(144)
    t.forward(110)
    t.right(144)
    t.forward(110)
    t.end_fill()


# ----------------主程序---------------
# 画左侧美国队长标志
move(-200, -100)
roundness("red", 150)  # 最大的红色圆圈
move(-200, -70)
roundness("white", 120)  # 第二个白色圆圈
move(-200, -40)
roundness("red", 90)  # 第三个红色圆圈
move(-200, -10)
roundness("blue", 60)  # 最后一个蓝色圆圈
move(-255, 68)
star()  # 画五角星
# 画右侧搞笑美国队长标志
t.seth(0)
move(200, -100)
roundness("red", 150)  # 最大的红色圆圈
move(200, -70)
roundness("white", 120)  # 第二个白色圆圈
move(200, -40)
roundness("red", 90)  # 第三个红色圆圈
move(200, -10)
roundness("blue", 60)  # 最后一个蓝色圆圈
move(145, 68)
star()  # 画五角星
# 搞笑元素
move(215, 75)  # 黄色圆圈
roundness("yellow", 25)
move(192, 65)  # 左眼大
roundness("white", 6)
move(192, 62)  # 左眼小
roundness("black", 4)
move(215, 65)  # 右眼大
roundness("white", 6)
move(215, 62)  # 右眼小
roundness("black", 4)

t.color("black")
t.pensize(2)

t.seth(160)  # 左眉毛
move(195, 65)
t.forward(10)
t.seth(20)  # 右眉毛
move(208, 65)
t.forward(10)
t.seth(0)  # 嘴
move(200, 40)
roundness("gray", 5)
t.mainloop()
