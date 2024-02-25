import turtle as t
import random
class Zdan(t.Turtle):
    def __init__(self):
        t.Turtle.__init__(self)
        self.speed(0)
        self.x = random.randint(4, 10)
        self.seth(-90)
        self.penup()
        self.goto(random.randint(-480, 380), 400)
        self.shape("turtle")
    def move(self):
        global ch
        if ch==1:
            return
        if (self.xcor()-x)**2+(self.ycor()-y)**2<100 or (self.xcor()+x)**2+(self.ycor()-y)**2<400:
            ch=1
            return
        if self.xcor()<0:
            self.color("black")
        if self.xcor()>0:
            self.color("white")
        self.fd(self.x)
        if self.ycor() < -400:
            self.x = random.randint(4, 10)
            self.goto(random.randint(-480, 380), 400)
        t.update()
        t.ontimer(self.move, 10)  # 调整这个延迟时

t1 = t.Turtle()
t1.hideturtle()
t.speed(0)
t.seth(90)
t.begin_fill()
t.fd(1000)
t.seth(0)
t.fd(900)
t.seth(270)
t.fd(2000)
t.seth(180)
t.fd(900)
t.end_fill()
t1.speed(0)
t.tracer(0)
t2 = t.Turtle()
t2.penup()
t2.goto(-400, 300)
t2.hideturtle()
time_value = 0  # 数字时间
ch=0
def time1():
    global time_value
    if ch==1:
        return
    time_value += 1
    t2.clear()
    t2.write(time_value, align="center", font=("Arial", 20, "normal"))
    t.ontimer(time1, 1000)
time1()
x=0
y=0
def motion(event):
    global x,y
    if ch==1:
        t2.goto(0,0)
        t2.color("red")
        t2.write(f"   游戏结束 \n 你坚持了{time_value}秒", align="center", font=("Arial", 40, "normal"))
        return
    x, y = event.x - 500,  400 - event.y
    t1.clear()
    t1.penup()
    t1.goto(-x, y)
    t1.dot(30)
    t1.goto(x, y)
    t1.dot(30, "white")


screen = t.Screen()
screen.setup(1000, 800)
canvas = screen.getcanvas()
canvas.bind('<Motion>', motion)
t5= Zdan()
t6= Zdan()
t7= Zdan()
t8= Zdan()
t9= Zdan()
t10= Zdan()
t.ontimer(t5.move,0)
t.ontimer(t6.move,0)
t.ontimer(t7.move,0)
t.ontimer(t8.move,0)
t.ontimer(t9.move,0)
t.ontimer(t10.move,0)

screen.mainloop()
