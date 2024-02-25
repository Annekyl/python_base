import turtle as t
import random

#------------画背景图--------------------------
t.tracer(False)
t.pensize(10)
t.begin_fill()
t.goto(0, 400)
t.goto(500,400)
t.goto(500,-400)
t.goto(0,-400)
t.goto(0,0)
t.end_fill()
t.tracer(True)
t.hideturtle()
t1=t.Pen()
t1.hideturtle()
t2=t.Pen()
t2.hideturtle()
t.tracer(5)
#-----------------------下落的障碍物-----------------------
class Pen(t.Pen):
    def __init__(self):
        t.Pen.__init__(self)
        self.x=random.randint(2,8)           #每次移动的长度不一样，使每个长条落下的速度不同
        self.penup()
        self.goto(random.randint(-450,450),420)
        self.setheading(-90)
        self.shape("turtle")
        t.ontimer(self.move,0)
    def move(self):
        global pd
        if pd==1:
            return
        if (self.xcor()-x)**2+(self.ycor()-y)**2<100 or (self.xcor()+x)**2+(self.ycor()-y)**2<400:
            pd=1
            return
        if self.xcor()<0:
            self.color("black")
        if self.xcor()>0:
            self.color("white")

        self.forward(self.x)

        if self.ycor()<-400:
            self.x = random.randint(4, 10)
            self.goto(random.randint(-450, 450), 420)
        t.update()
        t.ontimer(self.move, 20)  # 每10毫秒运行一次move



pd=0              #pd变为1则游戏结束
x=0
y=0
def motion(event):           #小球和鼠标一起运动
    global x,y
    if pd==1:
        t2.goto(-5,0)
        t2.pencolor("red")
        t2.write("游戏结束 ", align="center", font=("Arial", 40))
        return
    x, y = ((event.x - 500) ** 2) ** 0.5, 400 - event.y
    #t.tracer(False)
    t1.clear()
    t1.penup()
    t1.goto(-x, y)
    t1.dot(30)
    t1.goto(x, y)
    t1.dot(30,'white')
    #t.tracer(True)

screen = t.Screen()
screen.title('mirror')
screen.setup(1000, 800)
canvas = screen.getcanvas()
canvas.bind('<Motion>', motion)

t3=Pen()
t4=Pen()
t5=Pen()
t6=Pen()
t7=Pen() 
t8=Pen()
t9=Pen()
t10=Pen()
t.ontimer(t3.move,0)
t.ontimer(t4.move,0)
t.ontimer(t5.move,0)
t.ontimer(t6.move,0)
t.ontimer(t7.move,0)
t.ontimer(t8.move,0)
t.ontimer(t9.move,0)
t.ontimer(t10.move,0)

t.mainloop()
