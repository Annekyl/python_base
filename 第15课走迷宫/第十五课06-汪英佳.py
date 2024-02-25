import turtle as t
import time as e
t2=t.Pen()
t1=t.Pen()
t2.hideturtle()
x=[-500,-300,0,100,300]
y=[-300,100,0,300,-100,400]
d=28

def num(x,y):#x,y为坐标
    global n
    n=1
def move(x,y):
    maze.penup()
    maze.goto(x,y)
    maze.pendown()
def move1(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

Ball=t.Screen()
Ball.bgcolor('skyblue')#背景色
Ball.setup(1000,800)#面板大小

ball=t.Pen()#球体
ball.color('black')#球的颜色
ball.shape('circle')#球体形状
ball.pensize(16)
ball.penup()
ball.goto(-500,20)
ball.pendown()

ball.penup()#抬笔
#键盘操作
def move_up():
    if x[4]+d>ball.xcor()>x[0]-d and (y[0]-d<ball.ycor()<y[0] or y[5]-d<ball.ycor()<y[5]):
        ball.sety(ball.ycor()+0)
    else:
        ball.sety(ball.ycor()+7)
def move_down():
    if x[4]+2*d>ball.xcor()>x[0]-2*d and (y[0]-2*d<ball.ycor()<y[0]+d or y[5]<ball.ycor()<y[5]+d):
        ball.sety(ball.ycor()-0)
    else:
        ball.sety(ball.ycor()-7)

def move_right():
    if (x[0]-d/2<ball.xcor()<x[0] or x[4]-d/2<ball.xcor()<x[4]) and (y[5]+d>ball.ycor()>y[3]-d or y[2]+d>ball.ycor()>y[0]-d):
        ball.setx(ball.xcor()+0)
    elif (x[1]-d/2<ball.xcor()<x[1] or x[3]-d/2<ball.xcor()<x[3]) and y[5]+d>ball.ycor()>y[2]-d:
        ball.setx(ball.xcor()+0)
    elif x[2]-d/2<ball.xcor()<x[2] and y[3]+d>ball.ycor()>y[0]-d :
        ball.setx(ball.xcor()+0)
    else:
        ball.setx(ball.xcor()+7)

def move_left():
    if (x[0]<ball.xcor()<x[0]+d or x[4]<ball.xcor()<x[4]+d) and (y[5]+d>ball.ycor()>y[3]-d or y[2]+d>ball.ycor()>y[0]-d):
        ball.setx(ball.xcor()-0)
    elif (x[1]<ball.xcor()<x[1]+d/2 or x[3]<ball.xcor()<x[3]+d/2) and y[5]+d>ball.ycor()>y[2]-d:
        ball.setx(ball.xcor()-0)
    elif x[2]<ball.xcor()<x[2]+d/2 and y[3]+d>ball.ycor()>y[0]-d :
        ball.setx(ball.xcor()-0)
    else:
        ball.setx(ball.xcor()-7)
maze=t.Pen()#设立迷宫建图
maze.pensize(16)#画笔大小
maze.pencolor('yellow')
maze.speed(0)
move(-500,400)
maze.fd(800)
move(-500,400)
maze.seth(-90)
maze.fd(300)
move(-300,400)
maze.seth(-90)
maze.fd(500)
move(-100,400)
maze.seth(-90)
maze.fd(500)
move(100,400)
maze.seth(-90)
maze.fd(500)
move(300,400)
maze.seth(-90)
maze.fd(300)

move(-500,-300)
maze.seth(0)
maze.fd(800)
move(-500,-300)
maze.seth(90)
maze.fd(300)
move(-200,-300)
maze.seth(90)
maze.fd(600)
move(0,-300)
maze.seth(90)
maze.fd(600)
move(300,-300)
maze.seth(90)
maze.fd(300)
move(300,-300)
maze.seth(90)
maze.fd(300)
maze.hideturtle()

#感应键盘
Ball.listen()
t.onkeypress(move_up,'Up')
t.onkeypress(move_down,'Down')
t.onkeypress(move_right,'Right')
t.onkeypress(move_left,'Left')#点击即接收

t1.penup()
t1.goto(-700,400)
t1.pendown()
t1.write("您已用时：",font=('华文行楷',15))

begin=0.00#开始值
add=0.10#递增值
n=0
t.onscreenclick(num)#dead range
while(1):
    begin=begin+add
    t2.penup()
    t2.goto(-600,400)
    t1.pendown()
    t2.write("{:.2f}".format(begin),font=('华文行楷',16))
    e.sleep(0.01)
    if n==1:
        break
    t2.clear()

if -100<ball.ycor()<100 and ball.xcor()>=300:
    t2.speed(0)
    t2.penup()
    t2.goto(500,0)
    t2.pendown()
    t2.pencolor('red')
    t2.write("恭喜你获胜",font=('华文行楷',28))
