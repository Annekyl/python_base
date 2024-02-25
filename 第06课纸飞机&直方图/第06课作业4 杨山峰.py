# ——————载入库——————
import turtle as t

t.pensize(3)
t.speed(10)
t.hideturtle()
t.tracer(False)


# ——————模块化设计——————
def flag(x, y):  # 旗帜
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('red', 'red')
    t.begin_fill()
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.end_fill()


def big_star(x, y):  # 大星星
    t.color("yellow", "yellow")
    t.begin_fill()
    t.penup()
    t.goto(x, y)
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


def star_left(x, y):  # 小星星（起笔向左）
    t.penup()
    t.goto(x, y)
    t.pendown()
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


def star_right(x, y):  # 小星星（起笔向右）
    t.penup()
    t.goto(x, y)
    t.pendown()
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
my_list = [[-300, 200], [-260, 120], [-80, 160], [-80, 120], [-80, 65], [-80, 20]]  # 旗帜与星星位置
my_list2 = [6, 6, 155, 10]  # 转动角度
# 国旗旗帜
flag(my_list[0][0], my_list[0][1])
# 大五角星
big_star(my_list[1][0], my_list[1][1])
# 小五角星1
t.left(my_list2[0])
star_left(my_list[2][0], my_list[2][1])
# 小五角星2
t.left(my_list2[1])
star_right(my_list[3][0], my_list[3][1])
# 小五角星3
t.right(my_list2[2])
star_right(my_list[4][0], my_list[4][1])
# 小五角星4
t.left(my_list2[3])
star_left(my_list[5][0], my_list[5][1])

t.mainloop()
