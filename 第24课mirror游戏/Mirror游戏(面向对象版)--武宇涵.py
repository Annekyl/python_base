# 面向对象版游戏
import turtle as t
import threading as th  # 导入多线程库
import time as ti
import random as r


# ————————————————————————知识点—————————————————————————
# super库的主要用途是在子类中调用父类的方法或属性，而不需要显式地引用父类的名称。它返回一个临时对象，
# 该对象绑定到父类，并允许你调用父类的方法或属性。这个库特别有用在多重继承的情况下，当你需要在子类中同时调用多个父类的方法或属性时。

# ————————————————————————画笔对象————————————————————————
class draw_Pen(t.Pen):  # 操作的画笔
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        t.penup()
        t.shape('circle')
        self.penup()
        self.shape('circle')

    def motion(self, event):  # 经过分隔线时画笔变化颜色
        self.x, self.y = event.x, event.y
        if 400 - self.x > 0:
            t.color('white')
            self.color('black')
        else:
            t.color('black')
            self.color('white')
        t.goto(400 - self.x, 300 - self.y)
        self.goto(self.x - 400, 300 - self.y)


# ——————————————————————————————弹幕对象————————————————————————
class Barrage(t.Pen):  # 弹幕对象
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('turtle')
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.seth(-90)

    def end(self):  # 结束演出
        p = t.Pen()
        p.hideturtle()
        p.penup()
        p.color('red')
        t.hideturtle()
        p.goto(-200, -100)
        self.shapesize(stretch_wid=8, stretch_len=8)
        self.color('blue')
        p.write('你输了', font=('微软雅黑', 100))
        t.time.sleep(2)
        t.bye()

    def move_barrage(self):  # 弹幕移动
        while True:
            self.st()
            a = r.randint(-400, 400)
            self.speed(0)
            self.goto(a, 280)
            b = r.randint(2, 10)
            if a >= 0:
                self.color('white')
            else:
                self.color('black')
            c = int(650 / b)
            for i in range(c):
                self.forward(b)
                x = t.xcor()
                y = t.ycor()
                x2 = -x
                x3 = self.xcor()
                y3 = self.ycor()
                if -30 <= x - x3 <= 30 and -30 <= y - y3 <= 30:
                    self.end()
                    break
                elif -30 <= x2 - x3 <= 30 and -30 <= y - y3 <= 30:
                    self.end()
                    break
                t.time.sleep(0.01)
            self.hideturtle()


# ——————————————————————————————地图对象————————————————————————
class Map(t.Pen):  # 地图对象
    def __init__(self):
        super().__init__()
        t.setup(width=800, height=600)
        self.speed(0)
        self.ht()
        self.color('black')
        self.begin_fill()
        self.goto(0, 300)
        self.goto(400, 300)
        self.goto(400, -300)
        self.goto(0, -300)
        self.goto(0, 300)
        self.end_fill()


# ——————————————————————————————计时对象————————————————————————
class Time(t.Pen):  # 计时对象
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(-350, 230)
        global n
        n = 0

    def start(self):  # 计时进程
        global n
        while True:
            n += 1
            self.clear()
            self.write(n, font=('微软雅黑', 40, 'normal'))
            time.sleep(1)


# ———————————————————————————————运行对象————————————————————————
class Run:  # 整合运行程序
    def __init__(self):
        t.tracer(1, 0.5)
        ti.sleep(0.1)
        self.pens = draw_Pen()
        lists = [0 for _ in range(10)]  # 更改王八数量,200个左右就完全不行了
        for _ in lists:
            i = Barrage()
            i.thread = th.Thread(target=i.move_barrage)
            i.thread.start()
        self.map = Map()
        self.when = Time()
        thread = th.Thread(target=self.when.start)
        thread.start()
        screen = t.Screen()
        canvas = screen.getcanvas()
        canvas.bind('<Motion>', self.pens.motion)
        screen.exitonclick()
        t.mainloop()


all_run = Run()
