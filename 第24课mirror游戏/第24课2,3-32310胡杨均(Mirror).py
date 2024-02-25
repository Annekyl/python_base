import turtle as t
import threading as th
import time
import random as r


# 已知不足之处:1.退出后仍然会出现一个莫名其妙的弹窗.
# 2.要在pycharm中退出程序,需要退出两次.
# 3.静止不动时,程序会频闪,王八越多越闪,移动时会极大缓解.
# 4.不能全屏,会导致画笔和光标位置不对


class Pens(t.Pen):  # 操作对象
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        t.pu()
        t.shape('circle')
        self.pu()
        self.shape('circle')

    def motion(self, event):  # 颜色转换
        self.x, self.y = event.x, event.y
        if 400 - self.x > 0:
            t.color('white')
            self.color('black')
        else:
            t.color('black')
            self.color('white')
        t.goto(400 - self.x, 300 - self.y)
        self.goto(self.x - 400, 300 - self.y)


class Barrage(t.Pen):  # 弹幕对象
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.shape('turtle')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.seth(-90)

    def over(self):  # 结束演出
        p = t.Pen()
        p.ht()
        p.pu()
        p.color('red')
        p.goto(-200, -100)
        self.shapesize(stretch_wid=7, stretch_len=7)
        self.color('yellow')
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
                self.fd(b)
                x = t.xcor()
                y = t.ycor()
                x2 = -x
                x3 = self.xcor()
                y3 = self.ycor()
                if -20 <= x - x3 <= 20 and -20 <= y - y3 <= 20:
                    self.over()
                elif -20 <= x2 - x3 <= 20 and -20 <= y - y3 <= 20:
                    self.over()
                t.time.sleep(0.01)
            self.ht()


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


class When(t.Pen):  # 计时对象
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(-350, 230)
        global n
        n = 0

    def start(self):  # 计时进程
        global n
        while 1:
            n += 1
            self.clear()
            self.write(n, font=('微软雅黑', 40, 'normal'))
            time.sleep(1)


class All:  # 整合运行
    def __init__(self):
        t.tracer(10)
        self.pens = Pens()
        lists = [0 for _ in range(5)]  # 更改王八数量,200个左右就完全不行了
        for _ in lists:
            i = Barrage()
            i.thread = th.Thread(target=i.move_barrage)
            i.thread.start()
        self.map = Map()
        self.when = When()
        thread = th.Thread(target=self.when.start)
        thread.start()
        screen = t.Screen()
        canvas = screen.getcanvas()
        canvas.bind('<Motion>', self.pens.motion)
        screen.exitonclick()
        t.mainloop()


all_start = All()
