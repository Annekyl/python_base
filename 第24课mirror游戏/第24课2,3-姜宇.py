import turtle as t
import random as ra
import threading
import time


class Map:
    def __init__(self):
        self.game = t.Screen()
        self.game.title('wirror')  # 窗口命名
        self.game.setup(800, 600)  # 调整窗口大小
        self.tu1 = t.Pen()
        self.tu1.speed(0)
        self.tu1._tracer(0.5, 0.5)
        self.tu2 = t.Pen()
        self.tu2.speed(0)
        self.tu2._tracer(1, 0.5)
        self.draw()
        while True:
            try:
                screen = t.Screen()
                canvas = screen.getcanvas()
                canvas.bind('<Motion>', self.motion)
                break
            except Exception as result:
                pass

    def draw(self):  # 画背景
        self.bg = t.Pen()
        self.bg.ht()
        self.bg.speed(0)
        self.bg.color('black', 'black')
        self.bg.pu()
        self.bg.goto(0, 450)
        self.bg.pendown()
        self.bg.begin_fill()
        for i in range(4):
            self.bg.right(90)
            self.bg.fd(900)
        self.bg.end_fill()

    def motion(self, event):
        self.x, self.y = event.x, event.y
        self.tu1.pu()
        self.tu1.shape('circle')
        self.tu2.shape('circle')
        self.tu1.goto(-self.x + 650, -self.y + 400)
        self.tu2.pu()
        self.tu2.goto(self.x - 650, -self.y + 400)
        if self.x <= 400:
            self.tu1.color('red')
            self.tu2.color('blue')
        else:
            self.tu1.color('blue')
            self.tu2.color('red')


class Pen(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.create_pointer()
        self.shape('name')
        self.shapesize(10, 10, 20)
        self.pen1()
        self.Time()

    def create_pointer(self):
        t.penup()
        t.begin_poly()  # 记录多变形
        t.fd(8)
        t.end_poly()  # 停止
        t.register_shape('name', t.get_poly())  # 注册记录的多变形并取名name

    def pen1(self):  # 画笔
        a1 = ra.randint(1, 5)
        a2 = ra.randint(-500, 500)
        if a2 <= 0:
            self.color('white')
        else:
            self.color('black')
        self.ht()
        self.penup()
        self.goto(a2, 800)
        self.clear()
        self.st()
        while (1):
            for i in range(220):
                self.yy = int(a1 * i)
                self.pu()
                self.goto(a2, 400 - self.yy)
                if 500 - self.yy <= -300:
                    break
            break
        self.pen1()

    def Time(self):
        self.t2 = t.Pen()
        high = 0  # 初始值
        add = 0.01  # 增加值
        while (1):
            high += add
            self.t2.penup()
            self.t2.goto(300, 300)
            self.t2.write('{:.2f}'.format(high), font=('宋体', 30))
            time.sleep(0.01)


class Range(Pen):
    def __init__(self):
        threads = []
        for _ in range(7):
            thread = threading.Thread(target=Pen)
            thread.start()
            threads.append(thread)


a = Map()
b = Range()
a.game.mainloop()
