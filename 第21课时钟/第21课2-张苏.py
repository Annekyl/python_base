import turtle as t
import datetime as dt


class Penx(t.Turtle):
    def _init_(self):
        turtle.Turtle._init_(self)

    def create_pointer(self, length, width, name):  # 创建指针对象用的包，特点是可以自定义形状
        # 三个参数前后分别为长，宽，图像名
        t.reset()
        t.penup()
        t.hideturtle()  #
        t.begin_poly()  # 创建一个形状
        t.fd(length * 1.1)  # 这是指针的形状
        t.end_poly()  # 结束创建
        t.register_shape(name, t.get_poly())  # 注册这个形状
        hand = t.Turtle()  # 创建一个箭头
        hand.shape(name)  # 将箭头变成这个形状
        hand.shapesize(1.1, 1, width)  # 设置宽的参数
        return hand

    def auto_renew(self):  # 秒针
        global an
        tm = dt.datetime.today()  # 获取系统时间
        t.tracer(100)  # 不设会闪
        t2.clear()
        t2.goto(0, -350)
        t2.write(tm.strftime('%Y-%m-%d'), align='center', font=('Courier', 14, 'bold'))  # 截取年月日
        s_p.seth(an)
        an -= 5  # 每次走的度数
        t.ontimer(t2.auto_renew, 1000)  # 每隔一秒执行自己一次

    def auto_renew1(self):  # 分针
        global an1
        s_p1.seth(an1)
        an1 -= 5 / 60  # 走的度数
        t.ontimer(t2.auto_renew1, 1000)

    def auto_renew2(self):  # 时针
        global an2
        s_p2.seth(an2)
        an2 -= 5 / 3600
        t.ontimer(t2.auto_renew2, 1000)

    def go1(self, x, y):
        t1.pu()
        t1.goto(x, y)
        t1.pd()

    def bz(self):
        t1.speed(0)
        t1.pensize(10)
        t1.color("red")
        t1.pu()
        t1.fd(200)
        t1.pd()
        t1.fd(10)
        t1.go1(0, 0)

    def bz1(self):
        t1.speed(0)
        t1.pensize(3)
        t1.color("black")
        t1.pu()
        t1.fd(200)
        t1.pd()
        t1.fd(1)
        t1.go1(0, 0)


t1 = Penx()
t1.hideturtle()
t2 = Penx()
n = 0
t1.seth(90)
t.tracer(False)
for i in range(12):
    t1.seth(90 - n * 6)
    t1.bz()
    n += 1
    t1.seth(90 - n * 6)
    t1.bz1()
    n += 1
    t1.seth(90 - n * 6)
    t1.bz1()
    n += 1
    t1.seth(90 - n * 6)
    t1.bz1()
    n += 1
    t1.seth(90 - n * 6)
    t1.bz1()
    n += 1
m = 0
t1.seth(60)
t1.speed(0)
t1.color("black")
for i in range(12):
    t1.seth(60 - m * 30)
    t1.pu()
    t1.fd(230)
    t1.pd()
    t1.write(f"{i + 1}", font=("微软雅黑", 20, "normal"))
    t1.go1(0, 0)
    m += 1
t.tracer(True)
s_p = t2.create_pointer(160, 2, '123')
s_p1 = t2.create_pointer(140, 5, '12')
s_p2 = t2.create_pointer(90, 7, '1')
tm = dt.datetime.today()
a = tm.strftime('%H')  # 索取时
if int(a) >= 12:
    x = int(a) - 12
else:
    x = int(a)
b = tm.strftime('%M')  # 索取分
c = tm.strftime('%S')  # 索取秒
an = -(int(c) - 15) * 6 + 90
an1 = -(int(b) - 15) * 6 + 90
an2 = -((int(x) - 3) * 30 + (int(b) / 60) * 30) + 90
t2.auto_renew()
t2.auto_renew1()
t2.auto_renew2()
t.mainloop()