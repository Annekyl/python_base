# 载入库
import turtle as t
import random

t.screensize(bg="gray")
t.tracer(False)
t.hideturtle()
ch1 = '\u2665'  # 红心
ch2 = '\u2660'  # 黑桃
ch3 = '\u2666'  # 方块
ch4 = '\u2663'  # 梅花


def move(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(z)


def block(x, y):
    move(x, y, 0)
    t.color("black", "white")
    t.begin_fill()
    t.forward(45.6)
    t.right(90)
    t.forward(70.4)
    t.right(90)
    t.forward(45.6)
    t.right(90)
    t.forward(70.4)
    t.end_fill()


def draw(x1, y1, x2, y2, x3, y3, x4, y4, num, little_flower, big_flower, pencolor):
    move(x1, y1, -90)
    t.write(num, font=("微软雅黑", 12, "normal"))
    move(x2, y2, -90)
    t.color(pencolor)
    t.write(little_flower, font=("微软雅黑", 12, "normal"))
    move(x3, y3, 0)
    t.write(big_flower, font=("微软雅黑", 30, "normal"))
    move(x4, y4, 0)


pk = ["A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "J\nO\nK\nE\nR.", "J\nO\nK\nE\nR"]
color = [ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1,
         ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2,
         ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3,
         ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4,
         "", ""]
pen_color = ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red",
             "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
             "black",
             "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red",
             "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
             "black", "red", "black"]

total = 54
x = -400
y = 200

for j in range(2):
    for i in range(17):
        send = random.randint(0, total - 1 - i)
        if pk[send] == "J\nO\nK\nE\nR.":
            block(x, y)
            move(x + 5, y - 70, 0)
            t.color("red")
            t.write(pk[send], font=("微软雅黑", 7, "normal"))
            x += 20
            del pk[send]
            del color[send]
        elif pk[send] == "J\nO\nK\nE\nR":
            block(x, y)
            move(x + 5, y - 70, 0)
            t.color("black")
            t.write(pk[send], font=("微软雅黑", 7, "normal"))
            x += 20
            del pk[send]
            del color[send]
        else:
            block(x, y)
            draw(x + 5, y - 20, x + 3, y - 35, x + 10, y - 60, x, y, pk[send], color[send], color[send],
                 pen_color[send])
            x += 20
            del pk[send]
            del color[send]
    x = 100
    total -= 17
x = -200
y = -100
for i in range(20):
    send = random.randint(0, total - 1 - i)
    if pk[send] == "J\nO\nK\nE\nR.":
        block(x, y)
        move(x + 5, y - 70, 0)
        t.color("red")
        t.write(pk[send], font=("微软雅黑", 7, "normal"))
        x += 20
        del pk[send]
        del color[send]
    elif pk[send] == "J\nO\nK\nE\nR":
        block(x, y)
        move(x + 5, y - 70, 0)
        t.color("black")
        t.write(pk[send], font=("微软雅黑", 7, "normal"))
        x += 20
        del pk[send]
        del color[send]
    else:
        block(x, y)
        draw(x + 5, y - 20, x + 3, y - 35, x + 10, y - 60, x, y, pk[send], color[send], color[send],
             pen_color[send])
        x += 20
        del pk[send]
        del color[send]
t.tracer(True)
t.mainloop()
