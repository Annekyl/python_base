import turtle as t
import time
#载入画布
game=t.Screen()
t.bgcolor('black')
t.setup(800,600)
t.title('迷宫')
#制作小球
ball=t.Turtle(shape='circle')
ball.color('blue')
ball.shapesize(1)
game.listen()
ball.up()
ball.hideturtle()
ball.goto(-300,0)
ball.showturtle()
#def
def up():
    if (ball.ycor()==180 or (-320<ball.xcor()<-280 and ball.ycor()==30) or (-120<ball.xcor()<-80 and ball.ycor()==-120)
        or (80<ball.xcor()<120 and ball.ycor()==-120) or (280<ball.xcor()<320 and ball.ycor()==30)):
        pass
    else:
        ball.sety(ball.ycor()+5)
def down():
    if (ball.ycor()==-180 or (-320<ball.xcor()<-280 and ball.ycor()==-30) or (-220<ball.xcor()<-180 and ball.ycor()==120)
        or(-20<ball.xcor()<20 and ball.ycor()==120) or (180<ball.xcor()<220 and ball.ycor()==120) or
        (280<ball.xcor()<320 and ball.ycor()==-30)):
        pass
    else:
        ball.sety(ball.ycor()-5)
def left():
    if ((ball.xcor()==-280 and 30<ball.ycor()<180) or (ball.xcor()==-280 and -180<ball.ycor()<-30) or
        (ball.xcor()==-180 and -180<ball.ycor()<120) or (ball.xcor()==-80 and -120<ball.ycor()<180) or
        (ball.xcor()==20 and -180<ball.ycor()<120) or (ball.xcor()==120 and -120<ball.ycor()<180) or
        (ball.xcor()==220 and -180<ball.ycor()<120)) or(ball.xcor()==-300):
        pass
    else:
        ball.setx(ball.xcor()-5)
def right():
    if ((ball.xcor()==-220 and -180<ball.ycor()<120) or (ball.xcor()==-120 and -120<ball.ycor()<180) or
        (ball.xcor()==-20 and -180<ball.ycor()<120) or (ball.xcor()==80 and -120<ball.ycor()<180) or
        (ball.xcor()==180 and -180<ball.ycor()<120) or (ball.xcor()==280 and 30<ball.ycor()<180) or
        (ball.xcor()==280 and -180<ball.ycor()<-30)):
        pass
    else:
        ball.setx(ball.xcor()+5)
def goto(x,y):
    t1.up()
    t1.goto(x,y)
    t1.down()
#控制
game.onkeypress(up,'w')
game.onkeypress(down,'s')
game.onkeypress(left,'a')
game.onkeypress(right,'d')
#画墙
t1=t.Pen()
t1.color('yellow')
t1.pensize(20)
t1.speed(0)
t1.ht()
#上面
goto(-300,50)
t1.goto(-300,200)
t1.goto(300,200)
t1.goto(300,50)
goto(-100,200)
t1.goto(-100,-100)
goto(100,200)
t1.goto(100,-100)
#下面
goto(-300,-50)
t1.goto(-300,-200)
t1.goto(300,-200)
t1.goto(300,-50)
goto(-200,-200)
t1.goto(-200,100)
goto(200,-200)
t1.goto(200,100)
goto(0,-200)
t1.goto(0,100)
# 计时器
t2=t.Pen()
t2.up()
t2.goto(0,230)
t2.color('red')
t2.down()
t2.ht()

k=0.00
while(1):
    t2.write('{:.2f}'.format(k),font=('楷体',30,'bold'))
    t.tracer(100)
    time.sleep(0.01)
    t2.clear()
    k+=0.01
    if (ball.xcor()==300):
        break
t2.write('{:.2f}'.format(k),font=('楷体',30,'bold'))
if ball.xcor()==300:
    t1.clear()
    t2.clear()
    ball.ht()
    goto(-300,0)
    if (k>10):
        t1.write('你的用时为{:.2f},距离破10还需努力'.format(k),font=('楷体',30,'bold'))
    if (k<=10):
        t1.write('你的用时为{:.2f},实在是太牛逼了'.format(k),font=('楷体',30,'bold'))    
    if (k>24):
        t1.write('你的用时为{:.2f}'.format(k),font=('楷体',30,'bold'))
        





    




