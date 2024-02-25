import turtle, random, time, threading


class Mouse(turtle.Pen):
    def __init__(self):
        super().__init__()

    def motion1(self, event):
        turtle.tracer(0)
        t1.up()
        t1.shape('circle')
        t2.up()
        t2.shape('circle')
        y, x = event.x, event.y
        if t1.xcor() > 0:
            t1.color('white')
            t2.color('black')
        elif t2.xcor() > -2:
            t2.color('white')
            t1.color('black')
        t1.goto(-y + 420, -(x - 400))
        t2.goto(y - 425, -(x - 400))
        turtle.tracer(1, 0.1)


class Background(turtle.Pen):
    def _init_(self):
        turtle.Pen().__init__()

    def window(self):
        global n
        n = 0
        self.ht()
        turtle.tracer(0)
        self.seth(90)
        self.begin_fill()
        self.fd(800)
        self.right(90)
        self.fd(800)
        self.right(90)
        self.fd(1600)
        self.right(90)
        self.fd(800)
        self.right(90)
        self.fd(800)
        self.end_fill()
        turtle.tracer(1)

    def colur(self):
        if t1.xcor() > 7:
            t1.color('white')
            t1.color('black')
        elif t2.xcor() > 5:
            t2.color('white')
            t2.color('black')

    def when(self):  # 计时函数
        global n
        self.up()
        self.speed(100000)
        self.goto(-400, 350)
        n += 1
        self.clear()
        self.write(n, font=('微软雅黑', 30, 'normal'))
        turtle.ontimer(self.when, 1000)


class Object(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.up()
        self.speed(0)
        self.obstructs()

    def obstructs(self):
        while True:
            a = (random.randint(-450, 450))
            self.x = a
            self.y = 400
            b = random.randint(1, 10)
            if a > 0:
                self.color('white')
            elif a < -0:
                self.color('black')
            turtle.tracer(0)
            self.goto(a, 400)
            turtle.tracer(1, 0.5)
            self.seth(-90)
            self.pensize(10)
            while self.ycor() > -400:
                self.fd(b)
                self.y = self.y - b
                if (t2.xcor() - self.x) ** 2 + (t2.ycor() - self.y) ** 2 <= 250:
                    print(f'游戏结束了，你坚持了{n}秒')
                    turtle.bye()
                elif (t1.xcor() - self.x) ** 2 + (t1.ycor() - self.y) ** 2 <= 250:
                    print(f'游戏结束了，你坚持了{n}秒')
                    turtle.bye()
                time.sleep(0.0001)
                if self.ycor() <= -400:
                    break


class Play:
    def __init__(self):
        global t1, t2, t3, t4
        t1 = Mouse()
        t2 = Mouse()
        t3 = Background()
        t4 = Background()
        t3.window()
        t3.color()
        t4.when()

    @staticmethod
    def progress():
        # 运用多线程解决turtle中不能并发的问题
        ls = [0 for i in range(6)]
        for i in ls:
            i = threading.Thread(target=Object)
            i.setDaemon(True)
            i.start()

    @staticmethod
    def mouse_move():
        while True:
            try:
                screen = turtle.Screen()
                canvas = screen.getcanvas()
                canvas.bind('<Motion>', t1.motion1)
                screen.exitonclick()
                break

            except Exception:
                pass


play = Play()
play.progress()
play.mouse_move()
