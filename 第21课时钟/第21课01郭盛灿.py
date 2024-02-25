import turtle as t

t1 = t.Turtle()
t.pensize(4)


def move(x):
    t.penup()
    t.goto(0, 0)
    t.seth(90 - 30 * x)
    t.fd(100)
    t.pendown()
    t.fd(20)
    t.penup()


t.hideturtle()
t1.hideturtle()
t.tracer(0)
t1.penup()
t1.goto(0, 120)
t1.pendown()


def sz(x):
    t1.pendown()
    if x == 0:
        x = 12
    t1.write(f'{x}', align="center", font=("宋体", 14, "bold"))
    t1.penup()
    t1.circle(-130, 30)


for i in range(12):
    move(i)
    sz(i)
import datetime as sj

tm = sj.datetime.today()
date = tm.strftime("%Y-%m-%d")  # 年月日
t2 = t.Turtle()
t2.penup()
t2.goto(0, -30)
t2.write(f'{date}', align="center", font=("宋体", 9, "bold"))
t2.hideturtle()
t3 = t.Turtle()
t3.hideturtle()
t3.speed(100)
t.tracer(1000)


def shi(x):
    t3.home()
    t3.clear()
    t3.pensize(11)
    t3.seth(90 - 30 * x)
    t3.fd(50)


t4 = t.Turtle()
t4.hideturtle()
t4.speed(100)


def fenz(x):
    t4.home()
    t4.clear()
    t4.pensize(8)
    t4.seth(90 - 6 * x)
    t4.fd(70)


t5 = t.Turtle()
t5.hideturtle()
t5.speed(100)


def miaoz(x):
    t5.home()
    t5.clear()
    t5.pensize(5)
    t5.seth(90 - 6 * x)
    t5.fd(90)


def kais():
    tm = sj.datetime.today()
    H = int(tm.strftime("%H"))
    F = int(tm.strftime("%M"))
    S = int(tm.strftime("%S"))
    miaoz(S)
    fenz(F)
    shi(H + F / 60)
    t.update()
    t.ontimer(kais, 250)


kais()
t.done()
