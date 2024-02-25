import turtle as t

game = t.Screen()  # 创建窗口
game.title("迷宫冒险")
game.bgcolor("black")
game.setup(800, 600)
ls1 = [[-200, 100], [-100, -100], [0, 100], [100, -100], [200, 100]]


def to2(x, y, s):
    go2(x, y)
    t2.seth(s)
    t2.fd(150)


def move_up():
    if (-210 <= t1.xcor() <= -190 and t1.ycor() == -60) or (-10 <= t1.xcor() <= 10 and t1.ycor() == -60) or (
            190 <= t1.xcor() <= 210 and t1.ycor() == -60) or (-310 <= t1.xcor() <= -290 and t1.ycor() == 30) or (
            290 <= t1.xcor() <= 310 and t1.ycor() == 30) or (-310 <= t1.xcor() <= 310 and 90 <= t1.ycor() <= 100) or (
            -310 <= t1.xcor() <= 310 and -110 <= t1.ycor() <= -100):
        t1.sety(t1.ycor())
    else:
        t1.sety(t1.ycor() + 10)


def move_down():
    if (-110 <= t1.xcor() <= -90 and t1.ycor() == 60) or (90 <= t1.xcor() <= 110 and t1.ycor() == 60) or (
            -310 <= t1.xcor() <= -290 and t1.ycor() == -30) or (290 <= t1.xcor() <= 310 and t1.ycor() == -30) or (
            -310 <= t1.xcor() <= 310 and 100 <= t1.ycor() <= 110) or (
            -310 <= t1.xcor() <= 310 and -100 <= t1.ycor() <= -90):
        t1.sety(t1.ycor())
    else:
        t1.sety(t1.ycor() - 10)


def move_right():
    if (-210 <= t1.xcor() <= -200 and -60 <= t1.ycor() <= 100) or (
            -110 <= t1.xcor() <= -100 and -100 <= t1.ycor() <= 60) or (
            -10 <= t1.xcor() <= 0 and -60 <= t1.ycor() <= 100) or (
            90 <= t1.xcor() <= 100 and -100 <= t1.ycor() <= 60) or (
            190 <= t1.xcor() <= 200 and -60 <= t1.ycor() <= 100) or (
            -310 <= t1.xcor() <= -300 and 30 <= t1.ycor() <= 100) or (
            -310 <= t1.xcor() <= -300 and -100 <= t1.ycor() <= -30) or (
            290 <= t1.xcor() <= 300 and -100 <= t1.ycor() <= -30) or (
            290 <= t1.xcor() <= 300 and 30 <= t1.ycor() <= 100):
        t1.setx(t1.xcor())
    else:
        t1.setx(t1.xcor() + 10)


def move_left():
    if (-200 <= t1.xcor() <= -190 and -60 <= t1.ycor() <= 100) or (
            -100 <= t1.xcor() <= -90 and -100 <= t1.ycor() <= 60) or (
            -0 <= t1.xcor() <= 10 and -60 <= t1.ycor() <= 100) or (
            100 <= t1.xcor() <= 110 and -100 <= t1.ycor() <= 60) or (
            200 <= t1.xcor() <= 210 and -60 <= t1.ycor() <= 100) or (
            -300 <= t1.xcor() <= -290 and 30 <= t1.ycor() <= 100) or (
            -300 <= t1.xcor() <= -290 and -100 <= t1.ycor() <= -30) or (
            300 <= t1.xcor() <= 310 and -100 <= t1.ycor() <= -30) or (
            300 <= t1.xcor() <= 310 and 30 <= t1.ycor() <= 100):
        t1.setx(t1.xcor())
    else:
        t1.setx(t1.xcor() - 10)


def go1(x, y):
    t1.pu()
    t1.goto(x, y)
    t1.pd()


def go2(x, y):
    t2.pu()
    t2.goto(x, y)
    t2.pd()


t1 = t.Pen()
t2 = t.Pen()
t2.pensize(10)
t1.color("white")
t2.color("red")
t1.shape('turtle')
t1.shapesize(1, 1)  # 改变箭头大小，分别为长，宽
t1.pu()
game.listen()  # 键盘监听功能
game.onkey(move_up, 'Up')
game.onkey(move_down, 'Down')
game.onkey(move_right, 'Right')
game.onkey(move_left, 'Left')
go1(-330, 0)
t1.pu()
t2.hideturtle()
t.tracer(False)
go2(-300, 30)
t2.seth(90)
t2.fd(70)
t2.seth(0)
t2.fd(600)
t2.seth(-90)
t2.fd(70)
go2(-300, -30)
t2.seth(-90)
t2.fd(70)
t2.seth(0)
t2.fd(600)
t2.seth(90)
t2.fd(70)
for i in range(5):
    to2(ls1[i][0], ls1[i][1], ((-1) ** (i + 1)) * 90)
t.tracer(True)

t.mainloop()
