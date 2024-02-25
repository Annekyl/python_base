import turtle as t
import datetime as dt

hour = dt.datetime.now().strftime("%H")  # 时
minute = dt.datetime.now().strftime("%M")  # 分
second = dt.datetime.now().strftime("%S")  # 秒
t1 = t.Turtle()  # 时针
t2 = t.Turtle()  # 分针
t3 = t.Turtle()  # 秒针
t4 = t.Turtle()  # 显示时间，画表盘
t1.hideturtle()
t2.ht()
t3.ht()
t4.ht()


def draw_clock():
    t.tracer(False)
    t4.penup()
    t4.goto(0, -130)
    t4.pendown()
    t4.circle(140)
    t.tracer(True)


draw_clock()
while 1:
    t1.reset()
    t2.reset()
    t3.reset()
    t.tracer(False)
    tm = dt.datetime.now().strftime("%H:%M:%S")  # 时分秒
    t4.write(tm, align="center", font=("Courier", 14, 'bold'))
    t1.seth(90 - int(hour) * 30)
    t1.forward(30)
    t2.seth(90 - int(minute) * 6)
    t2.forward(50)
    t3.seth(90 - int(second) * 6)
    t3.forward(70)
    t.update()
    t1.clear()
    t2.clear()
    t3.clear()
