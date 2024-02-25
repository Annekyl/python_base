import turtle,time
ball=turtle.Pen()
game=turtle.Screen()
game.title('走迷宫')
game.bgcolor('black')
game.setup(800,600)
ball.color('white')
ball.shape('circle')
ball.pensize()
ball.up()
t1=turtle.Turtle()
t1.hideturtle
t1.up()
t1.goto(-100,240)
t1.pencolor('red')
turtle.tracer(2)    
    

def move_up():
    if(ball.ycor()>190 or ((-205<ball.xcor()<-195 or -5<ball.xcor()<5 or 195<ball.xcor()<205) and -110<ball.ycor())):
        ball.sety(ball.ycor())
    else:
        ball.sety(ball.ycor()+10)
def move_down():
    if(-125>ball.ycor() or ((-105<ball.xcor()<-95 or 95<ball.xcor()<105) and 180>ball.ycor())):
         ball.sety(ball.ycor())
    else:
        ball.sety(ball.ycor()-10)
        
def move_left():
    if((ball.xcor()==-190 or ball.xcor()==10 or ball.xcor()==210) and -100<ball.ycor()):
        ball.setx(ball.xcor())
    elif((ball.xcor()==-90 or ball.xcor()==110) and ball.ycor()<170):
        ball.setx(ball.xcor())
    elif(ball.xcor()==-280 and (ball.ycor()>60 or ball.ycor()<30)):
        ball.setx(ball.xcor())
    else:
        ball.setx(ball.xcor()-10)
def move_right():
    if((ball.xcor()==-210 or ball.xcor()==-10 or ball.xcor()==190) and -100<ball.ycor()):
        ball.setx(ball.xcor())
    elif((ball.xcor()==-110 or ball.xcor()==90) and ball.ycor()<170):
        ball.setx(ball.xcor())
    elif(ball.xcor()==280 and (ball.ycor()>60 or ball.ycor()<30)):
        ball.setx(ball.xcor())
    else:
        
        ball.setx(ball.xcor()+10)

    

    
    
game.listen()
game.onkey(move_up,'w')
game.onkey(move_down,'s')    
game.onkey(move_left,'a')
game.onkey(move_right,'d')



t2=turtle.Turtle()
t2.color('yellow')

t2.pensize(10)
t2.speed(0)
def move(x,y,m,n):
    t2.penup()
    t2.goto(x,y)
    t2.pendown()
    t2.seth(m)
    t2.fd(n)
move(-300,60,90,150)
move(-300,210,0,600)
move(300,210,-90,150)
for i in range(3):
    move(-200+200*i,210,-90,300)
move(-300,10,-90,150)
move(-300,-140,0,600)
move(300,-140,90,150)
for i in range(2):
    move(-100+200*i,-140,90,300)
#--以上的程序均是在作业的基础上进行的补充
ball.goto(-300,35)
k=0
#--定义计时器------------------
while(1):
    k+=0.02
    t1.write("{:.2f}".format(k),font=('楷体',60))
    time.sleep(0.01)
    t1.clear()


    
