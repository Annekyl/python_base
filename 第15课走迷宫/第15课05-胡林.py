#小球运动完后点击屏幕计时结束
from turtle import *
from time import *

go = [-300, 300, -200, 0, 200, -300, 300, -100, 100]
y = [300, -200]
fo = [200, 400]

game = Screen()
game.title("走迷宫")
game.bgcolor("black")
game.setup(1000, 800)

speed(20)
color("yellow")
penup()
goto(-300 ,300 )
pendown()
pensize(10)
forward(600)
penup()
goto(-300 ,-200 )
pendown()
forward(600)

def move_mi(a,b,c):
    penup()
    goto(a,b)
    pendown()
    forward(c)

seth(-90) 
for i in range (2 ):
     move_mi(go[i],y[0],fo[0])
for i in range (2 ,5 ):
     move_mi(go[i],y[0],fo[1])
seth(90)  
for j in range (5 ,7 ):
     move_mi(go[j],y[1],fo[0])
for j in range (7 ,9 ):
     move_mi(go[j],y[1],fo[1])

ball=Turtle() 
ball.goto(-310 ,50 )
ball.color("blue") 
ball.shape("circle") 
ball.penup()

def move_up():
     ball.sety(ball.ycor() +10 )
     check_collision()

def move_down():
     ball.sety(ball.ycor() -10 )
     check_collision()

def move_left():
      ball.setx(ball.xcor() -10 )
      check_collision()

def move_right():
      ball.setx(ball.xcor() +10 )
      check_collision()


def check_collision():
        x,y=round(ball.xcor()),round(ball.ycor())
        if ((300 > y > -100) and ((x == -220) or (x == -180) or (x == -20) or (x == 20) or (x == 180) or(x==220)))or((-200<y<200)and((x==-120 )or(x==-80 )or(x==80 )or(x==120 ))):
                ball.goto(-310, 50 )
        if y==-200 or y==300:
            ball.goto(-310,50)
game.listen()
game.onkeypress(move_up,"Up")
game.onkeypress(move_down,"Down")
game.onkeypress(move_left,"Left")
game.onkeypress(move_right,"Right")


tracer(5)
t1 = Turtle(visible=False) #设置绘制图形不可见
t2 = Turtle(visible=False)
t1.penup()
t2.penup()
t1.color("white")
t1.goto(-450 ,60 )
t1.write("计时器",font=("楷体",30))

add = 0.01
a = 0
k = 0

def p(x,y):
    global k
    k=1

onscreenclick(p)
while True:
    a += add
    t2.goto(-420 ,30 )
    t2.pencolor("white")
    t2.write("{:.2f}".format(a), font=("楷体",30))
    sleep(0.01)

    if k == 1:
        break

    t2.clear()

done()