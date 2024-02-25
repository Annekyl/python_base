from turtle import *
from time import *

g = Screen()
g.title("走迷宫")
g.bgcolor("black")
g.setup(800, 600)

b = Pen()
b.color("blue")
b.shape("circle")
b.pu()
b.goto(-350, 0)

b1 = Pen()
b1.color("red")
b1.shape("circle")
b1.shapesize(2)
b1.pu()
b1.goto(350, 0)

b2 = Pen()
b2.color("green")
b2.shape("circle")
b2.shapesize(1)
b2.pu()
b2.goto(350, 0)

W = [[-350, 200], [-350, 40], [-250, 200], [-250, -120], [-50, 200], [-50, -120], [150, 200], [150, -120], [350, 200],
     [350, 40],
     [-350, -200], [-350, -40], [-150, -200], [-150, 120], [50, -200], [50, 120], [250, -200], [250, 120], [350, -200],
     [350, -40]]

w = Turtle()
w.speed(0)
w.hideturtle()
w.pencolor("yellow")
w.pensize(20)
w.pu()
w.goto(-350, 40)
w.pd()
for a in (1, 11):
    w.pu()
    w.goto(W[a][0], W[a][1])
    w.pd()
    w.goto(W[a - 1][0], W[a - 1][1])
    for i in range(1, 8, 2):
        w.pu()
        w.goto(W[a - 2 + i][0], W[a - 2 + i][1])
        w.pd()
        w.goto(W[a + i][0], W[a + i][1])
        w.goto(W[a + 1 + i][0], W[a + 1 + i][1])


def move_up():
    flat = 0
    for i in range(len(W) - 1):
        if b.ycor() == W[i][1] - 20 and b.xcor() == W[i][0]:
            flat = 1
            break
    if b.ycor() == 180 or b.ycor() == -220:
        flat = 1
    if flat == 0:
        b.sety(b.ycor() + 20)
        if b.ycor() == 0 and b.xcor() == 350:
            b.hideturtle()
            b1.hideturtle()
            w.clear()
            goto(-300, 0)
            color("red")
            write("You,Win!!!!!!!", font=("楷体", 100))
    update()


def move_down():
    flat = 0
    for i in range(len(W) - 1):
        if b.ycor() == W[i][1] + 20 and b.xcor() == W[i][0]:
            flat = 1
            break
    if b.ycor() == 220 or b.ycor() == -180:
        flat = 1
    if flat == 0:
        b.sety(b.ycor() - 20)
        if b.ycor() == 0 and b.xcor() == 350:
            b.hideturtle()
            b1.hideturtle()
            w.clear()
            goto(-300, 0)
            color("red")
            write("You,Win!!!!!!!", font=("楷体", 100))
    update()


def move_left():
    flat = 0
    for i in range(len(W) - 1):
        for c in range(W[i][1], W[i + 1][1] + 1):
            if b.ycor() == c and b.xcor() == W[i][0] + 20:
                flat = 1
                break
    if b.xcor() == -350:
        flat = 1
    if flat == 0:
        b.setx(b.xcor() - 20)
        if b.ycor() == 0 and b.xcor() == 350:
            b.hideturtle()
            b1.hideturtle()
            w.clear()
            goto(-300, 0)
            color("red")
            write("You,Win!!!!!!!", font=("楷体", 100))
    update()


def move_right():
    flat = 0
    for i in range(len(W) - 1):
        for c in range(W[i][1], W[i + 1][1] + 1):
            if b.ycor() == c and b.xcor() == W[i][0] - 20:
                flat = 1
                break
    if b.xcor() == 330 and b.ycor() != 20 and b.ycor() != 0 and b.ycor() != -20:
        flat = 1
    if flat == 0:
        b.setx(b.xcor() + 20)
        if b.ycor() == 0 and b.xcor() == 350:
            b.hideturtle()
            b1.hideturtle()
            w.clear()
            goto(-300, 0)
            color("red")
            write("You,Win!!!!!!!", font=("楷体", 100))
    update()


g.listen()
g.onkeypress(move_up, 'Up')
g.onkeypress(move_down, 'Down')
g.onkeypress(move_left, 'Left')
g.onkeypress(move_right, 'Right')

tracer(100)
jc = 0
add = 0.01
color("white")
hideturtle()
pu()

while (True):
    goto(-100, 200)
    clear()
    if b.xcor() != -350:
        jc += add
        write("{:.2f}".format(jc), font=('楷体', 60))
        sleep(0.01)
    if b.ycor() == 0 and b.xcor() == 350:
        break
