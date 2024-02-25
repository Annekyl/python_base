import datetime as dt
import turtle as t

hour_time = dt.datetime.now().strftime("%H")  # 时
minute_time = dt.datetime.now().strftime("%M")  # 分
second_time = dt.datetime.now().strftime("%S")  # 秒
t.ht()
t1 = t.Pen()  # 写当前时间，时分秒
t1.penup()
t1.ht()
t4 = t.Pen()
t4.pensize(3)


def draw_clock():
    for i in range(60):
        t.tracer(0)
        if i % 5 == 0:
            t4.color("red")
        else:
            t4.color("black")
        t4.penup()
        t4.seth(i * 6)
        t4.fd(100)
        t4.pendown()
        t4.fd(15)
        t4.penup()
        t4.goto(0, 0)


def creat_pointer(length, width, name):
    t.reset()  # 清除t画笔已画的全部内容
    t.penup()
    t.begin_poly()  # 记录多边形
    t.forward(length * 1.1)
    t.end_poly()  # 停止记录
    t.register_shape(name, t.get_poly())  # 给多边形定义一个名字
    hand = t.Turtle()
    hand.shape(name)
    hand.shapesize(1, 1, width)
    return hand


def anto_renew():
    global an0
    t1.clear()
    t1.goto(0, -300)
    tm = dt.datetime.now().strftime("%H:%M:%S")  # 时分秒
    t.tracer(False)  # 防止时间闪烁
    t1.write(tm, align='center', font=('Courier', 14, 'bold'))
    t.update()
    t1.goto(0, -350)
    second.seth(an0)  # 设置箭头朝向
    an0 -= 6
    t.ontimer(anto_renew, 1000)  # 定时器，500毫秒后启动


def anto_minute():
    global an1
    minute.seth(an1)
    an1 -= 6
    t.ontimer(anto_minute, 1000 * 60)


def anto_hour():
    global an2
    hour.seth(an2)
    an2 -= 30
    t.ontimer(anto_hour, 1000 * 60 * 60)


# 画表盘
draw_clock()
# 画针
second = creat_pointer(90, 6, 'second')  # 秒针
an0 = 175 - int(second_time) * 6
minute = creat_pointer(70, 8, "minute")  # 分针
an1 = 175 - int(minute_time) * 6
hour = creat_pointer(50, 10, "hour")  # 时针
an2 = 175 - int(hour_time) * 30
anto_renew()
anto_minute()
anto_hour()
t.mainloop()
