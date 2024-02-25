# 任务2：面向对象的时钟（改造，定义类）
import time
import turtle as t
import datetime
import math

weeks = ['  星期一', '  星期二', '  星期三', '  星期四', '  星期五', '  星期六', '  星期日']


# ----------------clock类-------------
class clock:
    def __init__(self):  # 调用clock时会自动运行
        self.draw_clock_face()
        self.timee()

    # 创建画笔x1
    def create_penx1(self, lenght, name, wideth):
        self.pen = t.Pen()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.begin_poly()
        self.pen.fd(lenght)
        self.pen.end_poly()
        self.pen.getscreen().register_shape(name, self.pen.get_poly())
        self.penx = t.Pen()
        self.penx.shape(name)
        self.penx.shapesize(1, 1, wideth)
        return self.penx

    # 创建画笔x2
    def create_penx2(self):
        self.penx = t.Pen()
        self.penx.penup()
        self.penx.hideturtle()
        return self.penx

    # 画表盘
    def draw_clock_face(self):
        t.tracer(0)
        self.pen1 = self.create_penx2()
        self.pen1.left(60)
        for i in range(60):
            x = 200 * math.sin(i / 30 * math.pi)
            y = 200 * math.cos(i / 30 * math.pi)
            self.pen1.goto(x, y)
            self.pen1.dot(7)
        self.pen1.pensize(10)
        for i in range(1, 13):  # 画长的线段，表示时刻，共12个
            x = 200 * math.sin(i / 6 * math.pi)
            y = 200 * math.cos(i / 6 * math.pi)
            self.pen1.goto(x, y)
            self.pen1.pendown()
            self.pen1.fd(20)
            self.pen1.penup()
            x = 250 * math.sin(i / 6 * math.pi)
            y = 250 * math.cos(i / 6 * math.pi)  # 半径改为250，防止字与图重合
            self.pen1.goto(x - 10, y - 10)
            self.pen1.write(i, font=('楷体', 20, 'normal'))
            self.pen1.right(30)
        t.tracer(1)

    # 画指针
    def create_zhizhen(self):
        self.pen3 = self.create_penx1(120, 'shi', 10)
        self.pen4 = self.create_penx1(150, 'fen', 5)
        self.pen5 = self.create_penx1(180, 'miao', 2)

    # 循环更新
    def timee(self):
        t.tracer(0)
        self.pen2 = self.create_penx2()
        self.pen2.goto(-200, -400)
        self.create_zhizhen()
        t.tracer(1)

        while True:
            t.tracer(0)
            self.today = datetime.datetime.now()
            a = int(self.today.strftime('%S'))
            c = int(self.today.strftime('%M'))
            d = int(self.today.strftime('%H'))
            e = int(self.today.weekday())
            b = self.today.strftime('%Y.%m.%d %H:%M:%S') + weeks[e]
            self.pen2.clear()
            self.pen2.write(b, font=('宋体', 30, 'normal'))
            self.pen5.setheading(180 - a * 6)
            self.pen4.setheading(180 - c * 6)
            self.pen3.setheading(270 - d * 6)
            t.tracer(1)
            time.sleep(1)


# ------------主函数-----------------------
draw1 = clock()
