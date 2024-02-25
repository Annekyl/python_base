import turtle as t
import time
game=t.Screen()
game.title("迷宫")
game.bgcolor("pink")
game.setup(800,600)
ball=t.Pen()
ball.color('white')
ball.shape('circle')

def move_up():
    if(ball.ycor()==180)or(ball.ycor()==-180):
        ball.sety(ball.ycor()+0)
    else:
        ball.sety(ball.ycor()+10)
def move_down():
    if(ball.ycor()==180)or(ball.ycor()==-180):
        ball.sety(ball.ycor()-0)
    else:
        ball.sety(ball.ycor()-10)
def move_left():
    if(ball.xcor()==-100 and 130<=ball.ycor()<=180)or(ball.xcor()==-100 and -180<=ball.ycor()<=70):
        ball.setx(ball.xcor()-0)
    elif(ball.xcor()==0 and -30<=ball.ycor()<=180)or(ball.xcor()==0 and -180<=ball.ycor()<=-90):
        ball.setx(ball.xcor()-0)
    elif(ball.xcor()==100 and 130<=ball.ycor()<=180)or(ball.xcor()==100 and -180<=ball.ycor()<=70):
        ball.setx(ball.xcor()-0)
    else:
        ball.setx(ball.xcor()-10)
def move_right():
    if(ball.xcor()==-100 and 130<=ball.ycor()<=180)or(ball.xcor()==-100 and -180<=ball.ycor()<=70):
        ball.setx(ball.xcor()+0)
    elif(ball.xcor()==0 and -30<=ball.ycor()<=180)or(ball.xcor()==0 and -180<=ball.ycor()<=-90):
        ball.setx(ball.xcor()+0)
    elif(ball.xcor()==100 and 130<=ball.ycor()<=180)or(ball.xcor()==100 and -180<=ball.ycor()<=70):
        ball.setx(ball.xcor()+0)
    else:
        ball.setx(ball.xcor()+10)

game.listen()
game.onkey(move_up,'Up')
game.onkey(move_down,'Down')
game.onkey(move_left,'Left')
game.onkey(move_right,'Right')

t1=t.Pen()
t1.color('yellow')
t1.pensize(10)
t1.hideturtle()
t1.speed(0)

ball.penup()
ball.goto(-200,0)

def move(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()

move(-200,30)
t1.setheading(90)
t1.forward(150)
t1.right(90)
t1.forward(400)
t1.right(90)
t1.forward(220)
move(200,-100)
t1.forward(80)
t1.right(90)
t1.forward(400)
t1.right(90)
t1.forward(150)

t1.setheading(-90)
move(-100,180)
t1.forward(50)
move(-100,70)
t1.forward(250)
move(0,180)
t1.forward(210)
move(0,-90)
t1.forward(90)
t1.setheading(-90)
move(100,180)
t1.forward(50)
move(100,70)
t1.forward(250)


q=0
g=0.1
t2=t.Pen()
t2.penup()
t2.hideturtle()
while(1):
    t2.pu()
    q=q+g
    t2.goto(310,270)
    t2.write(q,font=("微软雅黑",30,"normal"))
    time.sleep(0.02)
    t2.clear()
    if(t2.xcor()==300 and t2.ycor()==0):
        break
    t2.write(q,font=("微软雅黑",30,"normal"))
