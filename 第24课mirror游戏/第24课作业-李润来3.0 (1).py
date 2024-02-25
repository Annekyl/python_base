import turtle as t
import random
import threading
import time
t.tracer(1, 0.5)
t.speed(0)
class Pen(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('circle')
        self.x = 0
        self.y = 0

    def motion(self, event):
        self.x, self.y = event.x, event.y
        t.goto(self.x - 855, -self.y + 470)
        self.goto(855 - self.x, -self.y + 470)
        if 858 - event.x > 0:
            self.color('blue')
            t.color('red')
        else:
            self.color('red')
            t.color('blue')

class Boundary(t.Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(5)
        self.ht()
        self.pu()
        self.goto(0, 600)
        self.pd()
        self.seth(-90)
        self.fd(1200)


class Time(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-600,400)


    def show_time(self, x, y, time_value):
        global time1
        self.goto(x, y)
        self.pencolor('black')
        time1 = round(time_value, 2)
        self.write(time1, font=('楷体', 20))
        time.sleep(0.01)
        self.clear()
        t.ontimer(lambda: self.show_time(x, y, time_value + 0.01), 1)


#障碍物
class Barrage(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.right(90)
        self.shape('turtle')
        self.x = 0
        self.barrage()

    def barrage(self):
        self.y = 600
        speed = random.randint(2, 6)
        point = random.randint(-830, 830)
        self.x = point
        self.pu()
        self.goto(point, 600)
        self.clear()
        self.color('black')
        while True:
            self.fd(speed)
            self.clear()
            self.y = self.y-speed
            if ((pen1.x-855-self.x)**2 + (470-pen1.y-self.y)**2 <= 250) or ((855 - pen1.x-self.x)**2 + (470-pen1.y-self.y)**2 <= 250):
                t.bye()
            t.time.sleep(0.01)
            if self.ycor() <= -600:
                break
        self.barrage()
class Game(t.Turtle):
    def __init__(self):
        global pen1
        time2 = Time()
        time2.show_time(-600, 400, 0)
        pen1 = Pen()
        pen1.shape('circle')
        t.pu()
        t.shape('circle')
        self.boundary = Boundary()
        self.mouse()


    def mouse(self):
        threads = []
        for _ in range(7):
            thread = threading.Thread(target=Barrage)
            thread.start()
            threads.append(thread)
        while True:
            try:
                screen = t.Screen()
                canvas = screen.getcanvas()
                canvas.bind('<Motion>', pen1.motion)
                screen.exitonclick()
                break
            except Exception as result:
                pass


game = Game()