import turtle as t
import datetime as dt


def creat_pointer(length, width, name):
    t.reset()  # 清除t画笔已画的全部内容
    t.penup()
    t.begin_poly()
    t.forward(length * 1.1)
    t.end_poly()
    t.register_shape(name, t.get_poly())
    hand = t.Turtle()
    hand.shape(name)
    hand.shapesize(1, 1, width)
    return hand


def anto_renew():
    global an0
    tm = dt.datetime.now().strftime("%H:%M:%S")
    t1.clear()
    t1.goto(0, -300)
    t.tracer(False)  # 防止时间闪烁
    t1.write(tm, align='center', font=('Courier', 14, 'bold'))
    t.update()
    t1.goto(0, -350)
    s_p.seth(an0)  # 设置箭头朝向
    an0 -= 6
    t.ontimer(anto_renew, 1000)  # 定时器，500毫秒后启动


s_p = creat_pointer(90, 7, 'hour')
t1 = t.Pen()
t1.penup()
t1.ht()
an0 = -6
anto_renew()
t.mainloop()
