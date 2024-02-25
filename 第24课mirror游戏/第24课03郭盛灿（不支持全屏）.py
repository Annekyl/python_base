import turtle as t
import random


class Zdan(t.Turtle):  # 子弹的类
    def __init__(self):
        global ch
        t.Turtle.__init__(self)
        self.speed(0)
        self.x = random.randint(4, 10)
        self.seth(-90)
        self.penup()
        self.goto(random.randint(-480, 380), 400)
        self.shape("turtle")
        t.ontimer(self.move, 0)

    def move(self):
        global ch
        if ch == 1:
            return
        if (self.xcor() - x) ** 2 + (self.ycor() - y) ** 2 < 100 or (self.xcor() + x) ** 2 + (
                self.ycor() - y) ** 2 < 400:
            ch = 1
            return
        if self.xcor() < 0:
            self.color("black")
        if self.xcor() > 0:
            self.color("white")
        self.fd(self.x)
        if self.ycor() < -400:
            self.x = random.randint(4, 10)
            self.goto(random.randint(-480, 380), 400)
        t.update()
        t.ontimer(self.move, 10)


class huabi(t.Turtle):  # 鼠标操作画笔的类
    def __init__(self):
        global ch
        t.Turtle.__init__(self)
        ch = 0
        self.hideturtle()
        screen = t.Screen()
        screen.setup(1000, 800)
        canvas = screen.getcanvas()
        canvas.bind('<Motion>', self.motion)

    def motion(self, event):
        global x, y, ch
        if ch == 1:
            self.goto(0, 0)
            self.color("red")
            self.write(f"   游戏结束 \n 你坚持了{time_value}秒", align="center", font=("Arial", 40, "normal"))
            return
        x, y = ((event.x - 500) ** 2) ** 0.5, 400 - event.y
        self.clear()
        self.penup()
        self.goto(-x, y)
        self.dot(30)
        self.goto(x, y)
        self.dot(30, "red")


class Time(t.Turtle):  # 计时表的类
    def __init__(self):
        global time_value, ch
        t.Turtle.__init__(self)
        self.pen()
        self.goto(-400, 300)
        self.hideturtle()
        time_value = 1
        self.time()

    def time(self):
        global time_value, ch
        if ch == 1:
            return
        t.update()
        time_value += 1
        self.clear()
        self.write(time_value, align="center", font=("Arial", 20, "normal"))
        t.ontimer(self.time, 1000)


class Game():  # 总类
    def __init__(self):
        global x, y, ch, time_value
        t.begin_fill()
        t.speed(0)
        t.goto(0, 700)
        t.goto(1000, 700)
        t.goto(1000, -1000)
        t.goto(0, -1000)
        t.end_fill()
        x = 0
        y = 0
        ch = 0
        time_value = 1
        t.tracer(0)
        screen = t.Screen()
        screen.setup(1000, 800)
        t2 = huabi()
        A = {}
        for i in range(10):
            A[i] = Zdan()
        t3 = Time()
        screen.mainloop()


T1 = Game()
