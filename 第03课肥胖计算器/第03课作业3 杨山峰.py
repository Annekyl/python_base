# ——————载入库——————
import turtle as t

t.pensize(3)
t.speed(10)
t.hideturtle()


# ——————模块化设计——————
def flag():  # 旗帜
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.end_fill()


def big_star():  # 大星星
    t.color("yellow", "yellow")
    t.begin_fill()
    t.penup()
    t.goto(-260, 120)
    t.pendown()
    t.right(90)
    t.forward(120)
    t.right(144)
    t.forward(120)
    t.right(144)
    t.forward(120)
    t.right(144)
    t.forward(120)
    t.right(144)
    t.forward(120)
    t.end_fill()


def move(x, y):  # 移动箭头
    t.penup()
    t.goto(x, y)
    t.pendown()


def star_left():  # 小星星（起笔向左）
    t.color("yellow", "yellow")
    t.begin_fill()
    t.forward(40)
    t.left(144)
    t.forward(40)
    t.left(144)
    t.forward(40)
    t.left(144)
    t.forward(40)
    t.left(144)
    t.forward(40)
    t.end_fill()


def star_right():  # 小星星（起笔向右）
    t.color("yellow", "yellow")
    t.begin_fill()
    t.forward(40)
    t.right(144)
    t.forward(40)
    t.right(144)
    t.forward(40)
    t.right(144)
    t.forward(40)
    t.right(144)
    t.forward(40)
    t.end_fill()


# ——————主程序——————
t.color("red", "red")  # 移动画笔
t.begin_fill()
t.penup()
t.goto(-300, 200)
t.pendown()
# 国旗旗帜
flag()
# 大五角星
big_star()
# 小五角星1
t.left(6)
move(-80, 160)
star_left()
# 小五角星2
t.left(6)
move(-80, 120)
star_right()
# 小五角星3
t.right(155)
move(-80, 65)
star_right()
# 小五角星4
t.left(10)
move(-80, 20)
star_left()
