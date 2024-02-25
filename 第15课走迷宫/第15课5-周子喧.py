import turtle as t
import time

list1=[[-600,0],[250,300],[-250,600]]
list2=[[-600,600],[450,-450],[-350,-100],[300,150]]
def f():
    global t
    t=1

def k():
    global t
    t=2
    
def move_up():
    if ball.ycor()<210 and ball.xcor()!=-600 and ball.xcor()!=-300 and ball.xcor()!=0 and ball.xcor()!=300 and ball.xcor()!=600 :
        ball.sety(ball.ycor()+10)
    if ball.xcor()==-600 and ball.ycor()<-45:
        ball.sety(ball.ycor()+10)
    if ball.xcor()==-300 and ball.ycor()<-290:
        ball.sety(ball.ycor()+10)
    if ball.xcor()==0 and ball.ycor()<-290:
        ball.sety(ball.ycor()+10)
    if ball.xcor()==300 and ball.ycor()<-290:
        ball.sety(ball.ycor()+10)
    if ball.xcor()==600 and ball.ycor()<-45:
        ball.sety(ball.ycor()+10)
        
        
def move_down():
    if ball.ycor()>-305 and ball.xcor()!=-600 and ball.xcor()!=-450 and ball.xcor()!=-150 and ball.xcor()!=150 and ball.xcor()!=450 :
        ball.sety(ball.ycor()-10)
    if ball.xcor()==-600 and ball.ycor()>-55:
        ball.sety(ball.ycor()-10)
    if ball.xcor()==-450 and ball.ycor()>195:
        ball.sety(ball.ycor()-10)
    if ball.xcor()==-150 and ball.ycor()>195:
        ball.sety(ball.ycor()-10)
    if ball.xcor()==150 and ball.ycor()>195:
        ball.sety(ball.ycor()-10)
    if ball.xcor()==450 and ball.ycor()>195:
        ball.sety(ball.ycor()-10)
    if ball.xcor()==600 and ball.ycor()>-55:
        ball.sety(ball.ycor()-10)
        
    

def move_left():
    if ball.xcor()!=-570 and ball.xcor()!=-420 and ball.xcor()!=-270 and ball.xcor()!=-120 and ball.xcor()!=30 and ball.xcor()!=180 and ball.xcor()!=330 and ball.xcor()!=480 and ball.xcor()!=630 :
        ball.setx(ball.xcor()-10)
    if ball.xcor()==-570 and -55<ball.ycor()<-45:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==630 and -55<ball.ycor()<-45:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==-420 and 195<ball.ycor()<210:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==-270 and -310<ball.ycor()<-285:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==-120 and 195<ball.ycor()<210:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==30 and -310<ball.ycor()<-285:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==180 and 195<ball.ycor()<210:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==330 and -310<ball.ycor()<-285:
        ball.setx(ball.xcor()-10)
    if ball.xcor()==480 and 195<ball.ycor()<210:
        ball.setx(ball.xcor()-10)
    


def move_right():
    if ball .xcor()!=-630 and ball.xcor()!=-480 and ball.xcor()!=-330 and ball.xcor()!=-180 and ball.xcor()!=-30 and ball.xcor()!=120 and ball.xcor()!=270 and ball.xcor()!=420 and ball.xcor()!=570  :
        ball.setx(ball.xcor()+10)
    if ball .xcor()==-630 and -55<ball.ycor()<-45:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==570 and -55<ball.ycor()<-45:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==-480 and 195<ball.ycor()<205:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==-330 and -310<ball.ycor()<-285:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==-180 and 195<ball.ycor()<205:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==-30 and -310<ball.ycor()<-285:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==120 and 195<ball.ycor()<205:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==270 and -310<ball.ycor()<-285:
        ball.setx(ball.xcor()+10)
    if ball.xcor()==420 and 195<ball.ycor()<205:
        ball.setx(ball.xcor()+10)
    
def yx():
    t2=t.Pen()
    t2.ht()
    t2.pu()
    t2.color('red')
    t2.goto(-300,300)
    t2.write("请穿过迷宫走到终点！",font=('楷书',50))
    

def migong():
    t1=t.Pen()
    t1.speed(0)
    t1.pensize(30)
    t1.color('white')
    t1.pu()
    t1.goto(list1[0][0],list1[0][1])
    t1.pd()
    t1.goto(list1[0][0],list1[1][0])
    for i in range(1,4):
        t1.goto(list1[0][0]+i*list1[1][1],list1[1][0])
        t1.goto(list1[0][0]+i*list1[1][1],list1[2][0])
        t1.goto(list1[0][0]+i*list1[1][1],list1[1][0])
    t1.goto(list1[2][1],list1[1][0])
    t1.goto(list1[2][1],list1[0][1])

    t1.pu()
    t1.goto(list2[0][0],list2[2][1])
    t1.pd()
    t1.goto(list2[0][0],list2[2][0])
    t1.goto(list2[1][1],list2[2][0])
    for i in range(1,4):
        t1.goto(list2[1][1]+(i-1)*list2[3][0],list2[3][1])
        t1.goto(list2[1][1]+(i-1)*list2[3][0],list2[2][0])
        t1.goto(list2[1][1]+i*list2[3][0],list2[2][0])
    t1.goto(list2[1][0],list2[3][1])
    t1.goto(list2[1][0],list2[2][0])
    t1.goto(list2[0][1],list2[2][0])
    t1.goto(list2[0][1],list2[2][1])


#1.创建窗体
game=t.Screen()
game.title('迷宫游戏')
game.bgcolor('black')          #设置窗体颜色
game.setup(1700,800)        #设置窗体大小

#2.创建一个运动物体
ball=t.Pen()
t.register_shape('机器人.gif')
ball.shape('机器人.gif')
ball.goto(-700,-50)
ball.up()

#4.画迷宫
yx()
migong()



#3.让球动起来  
game.listen()
game.onkeypress(move_up,'Up')
game.onkeypress(move_down,'Down')
game.onkeypress(move_left,'Left')
game.onkeypress(move_right,'Right')



#5.定时间
t3=t.Pen()
t3.ht()
m=0
add=0.12
t=0
game.onkey(f,'Up')
game.onkey(f,'Down')
game.onkey(f,'Left')
game.onkey(f,'Right')
game.onkey(k,'Q')
while(True):
    if t==1:
        m+=add
        t3.pu()
        t3.goto(400,300)
        t3.color('green')
        t3.write("{:.2f}".format(m),font=('楷书',40))
        time.sleep(0.03)
    if t==2:
        break
    t3.clear()


t.mainloop()
       

