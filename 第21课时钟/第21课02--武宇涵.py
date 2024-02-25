import turtle as t
import datetime as dt


class Penx(t.Turtle):
    def _init_(self):
        turtle.Turtle._init_(self)

    def move(self, dis):
        t.penup()
        t.forward(dis)
        t.pemdow()

    def create_pointer(self, length, width, name):
        t.reset()  # 清除画笔已画全部内容
        t.penup()
        t.hideturtle()
        t.begin_poly()  # 记录多边形
        t.forward(length * 1.1)
        t.end_poly()  # 停止记录多边形，生成图形
        t.register_shape(name, t.get_poly())  # 将记录的多边形注册，并命名为name
        hand = t.Turtle()
        hand.shape(name)
        hand.shapesize(1, 1, width)  # 垂直方向拉伸1（不拉伸），水平方向拉伸1
        return hand

    def auto_renew(self):
        global an0
        global an1
        global an2
        t.tracer(100)
        now = dt.datetime.today()  # 获取系统时间
        # now=dt.datetime.now()
        year = now.year  # 获取准确的年
        month = now.month  # 获取准确的月
        day = now.day  # 获取准确的天
        hour = now.hour  # 获取准确的时
        minute = now.minute  # 获取准确的分
        second = now.second  # 获取准确的秒
        tm = dt.datetime(year, month, day, hour, minute, second)
        t1.clear()
        t1.goto(0, 300)
        t1.write(tm, align="center", font=("Courier", 20, "bold"))
        '''
        t1.goto(0,-350)#打印年月日
        t1.write(tm.strftime("%Y-%m-%d"),align="center",font=("Courier",14,"bold"))
        '''
        t.seth(0)
        an0 -= 6
        s_p.setheading(an0)
        t.seth(0)
        an1 -= 6 / 60
        s_p1.setheading(an1)
        an2 -= 6 / 3600
        t.seth(0)
        s_p2.setheading(an2)
        t.ontimer(t2.auto_renew, 1000)  # 定时器每500毫秒后调用自己

    def draw_ke(self):
        t2 = t.Pen()
        t2.hideturtle()
        t2.pensize(5)
        t2.color("black")
        for i in range(60):
            t2.penup()
            t2.goto(0, 0)
            t2.seth(90 - i * 6)
            t2.forward(200)
            t2.pendown()
            t2.forward(5)
        t2.pensize(10)
        t2.color("red")
        for i in range(12):
            t2.penup()
            t2.goto(0, 0)
            t2.seth(60 - i * 30)
            t2.forward(200)
            t2.pendown()
            t2.forward(10)

    def draw_shu(self):
        t2 = t.Pen()
        t2.hideturtle()
        t2.penup()
        t2.goto(0, 0)
        t2.seth(90)
        t2.forward(214)
        t2.write(12, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(58)
        t2.forward(220)
        t2.write(1, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(26)
        t2.forward(222)
        t2.write(2, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-4)
        t2.forward(228)
        t2.write(3, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-33)
        t2.forward(235)
        t2.write(4, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-62)
        t2.forward(245)
        t2.write(5, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-90)
        t2.forward(245)
        t2.write(6, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-118)
        t2.forward(244)
        t2.write(7, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-147)
        t2.forward(240)
        t2.write(8, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-176)
        t2.forward(230)
        t2.write(9, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-206)
        t2.forward(230)
        t2.write(10, align="center", font=("Courier", 20, "bold"))
        t2.penup()
        t2.goto(0, 0)
        t2.seth(-238)
        t2.forward(220)
        t2.write(11, align="center", font=("Courier", 20, "bold"))


# ————————主程序部分————————
t.tracer(False)
t1 = Penx()
t2 = Penx()
# ————画出刻度————
# ——大和小隔刻度——
t1.draw_ke()
# ——画出刻度上的数字——
t1.draw_shu()
# ——获取准确系统时间——
now = dt.datetime.today()
hour = now.hour
minute = now.minute
second = now.second
s_p = t2.create_pointer(160, 1, "hour")  # 创建秒针
s_p1 = t2.create_pointer(120, 4, "minute")  # 创建分针
s_p2 = t2.create_pointer(80, 7, "minute")  # 创建时针
# 创建了一个画笔s_p.它继承了画笔的全部特征,但有改变:形状为自定义
t1 = t.Pen()
t1.penup()
t1.ht()
an0 = 180 - second * 6
an1 = 180 - minute * 6
an2 = 180 - hour * (360 / 12)
t.tracer(True)
t2.auto_renew()  # 此函数会自我调用，相当于死循环
t.mainloop()