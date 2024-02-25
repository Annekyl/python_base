import turtle as t
import datetime as dt


# ---------------定义对象----------------------
class Penx(t.Pen):
    def __init__(self):
        t.Pen.__init__(self)

    def make_bs(self, x):
        t.tracer(False)
        self.pensize(7)
        self.hideturtle()
        for i in range(60):
            self.up()
            self.fd(x)
            self.down()
            if (i % 5 == 0):
                self.fd(25)
                if (self.ycor() < 0 and i / 5 + 3 <= 12):
                    self.up()
                    self.goto(self.xcor(), self.ycor() - 20)
                    self.write(int(i / 5 + 3), font=('宋体', 20))
                    self.goto(self.xcor(), self.ycor() + 20)
                    self.down()
                elif (i / 5 + 3 <= 12):
                    self.up()
                    self.goto(self.xcor() - 5, self.ycor())
                    self.write(int(i / 5 + 3), font=('宋体', 20))
                    self.goto(self.xcor() + 5, self.ycor())
                    self.down()
                else:
                    self.up()
                    self.goto(self.xcor() - 5, self.ycor())
                    self.write(int(i / 5 - 9), font=('宋体', 20))
                    self.goto(self.xcor() + 5, self.ycor())
                self.up()
                self.fd(-x - 25)
                self.down()
            else:
                self.dot(3)
                self.up()
                self.fd(-x)
                self.down()
            self.rt(6)
        t.tracer(True)

    def biaozhen(self, l, name):
        self.begin_poly()
        self.up()
        self.forward(l)
        self.end_poly()
        self.getscreen().register_shape(name, self.get_poly())
        self.goto(0, 0)

    def csh(self, x, y):
        self.shape(x)
        self.pencolor(y)


def settime():
    tm = dt.datetime.today()
    t1.clear()
    t1.up()
    t1.goto(-100, 250)
    t1.write(str(tm)[0:10], font=('Courite', 40))


t1 = t.Pen()
t1.hideturtle()
settime()
t1.penup()


# -----------定义指针偏转角度模块----------
def time():
    global s, f, m
    tm = dt.datetime.today()
    f = tm.strftime('%H')
    m = tm.strftime('%M')
    s = tm.strftime('%S')


# ---------画指针模块--------------------------
def tick():
    global s, f, m
    tm = dt.datetime.today()
    time()
    s = int(s)
    f = int(f)
    m = int(m)
    mz.seth(180 - s * 6)
    fz.seth(180 - (m + s / 60) * 6)
    sz.seth(180 - (f + m / 60) * 30)
    t.up()
    t.ontimer(tick, 0)


# ------------主函数--------------------------
t1 = Penx()
t1.make_bs(160)
t2 = Penx()
t2.biaozhen(70, 'shizhen')
t2.biaozhen(90, 'fenzhen')
t2.biaozhen(120, 'miaozhen')
sz = Penx()
sz.csh('shizhen', 'red')
fz = Penx()
fz.csh('fenzhen', 'blue')
mz = Penx()
mz.csh('miaozhen', 'green')
tick()
