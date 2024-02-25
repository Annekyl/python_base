import turtle
import time

game=turtle.Screen() #创建窗体
game.title("走迷宫") #窗体标题
game.bgcolor("black") #设置背景色
game.setup(800,700) #设置窗体大小

ball=turtle.Pen() #创建一个画笔
ball.pu()
ball.color('aqua')
ball.shape('circle') #笔的形状为一个圆
ball.speed(0)
ball.goto(-350,0)

t=turtle.Pen()
t._tracer(10)
t.ht()
t.pu()
t.goto(-90,280)
t.color('blue')
def num():
    n=0
    while 1:
        time.sleep(0.01)
        n+=0.01
        t.write('{:.2f}'.format(n),font=('楷体',50))
        t.clear()
turtle.ontimer(num,100)

r=[[-310,-290,20,260],#定义墙的范围[min_x,man_x,min_y,max_y]
   [-310,-290,-260,-20],
   [-290,290,240,260],
   [-290,290,-260,-240],
   [-220,-190,-270,170],
   [-20,10,-270,170],
   [180,210,-270,170],
   [290,310,20,260],
   [290,310,-260,-20],
   [-110,-90,-170,240],
   [90,110,-170,240]]

def move(x,y):
    mg.pu()
    mg.goto(x,y)
    mg.pd()

mg=turtle.Pen()
mg.pensize(20)
mg.color('yellow')
mg.speed(0)
mg.ht()
move(-300,30)
mg.goto(-300,250)
mg.goto(300,250)
mg.goto(300,30)
move(300,-30)
mg.goto(300,-250)
mg.goto(-300,-250)
mg.goto(-300,-30)
for i in range(6):
    move(-200+100*i,(-(-1)**i)*250)
    mg.goto(-200+100*i,((-1)**i)*150)

def ce():
    for i in range(len(r)):
        if r[i][0]<=ball.xcor() and r[i][1]>=ball.xcor() and r[i][2]<=ball.ycor() and r[i][3]>=ball.ycor():
            ball.goto(-350,0)#使球撞墙后回到起点

def move_up():
    ce()
    ball.sety(ball.ycor()+10)
def move_down():
    ce()
    ball.sety(ball.ycor()-10)
def move_left():
    ce()
    ball.setx(ball.xcor()-10)
def move_right():
    ce()
    ball.setx(ball.xcor()+10)

game.listen() #开启球的键盘监听功能
game.onkeypress(move_up, 'Up')
game.onkeypress(move_down, 'Down')
game.onkeypress(move_left, 'Left')
game.onkeypress(move_right, 'Right')
turtle.mainloop()