from turtle import *
from time import *
from random import *

ch1='\u2665'
ch2='\u2660'
ch3='\u2666'
ch4='\u2663'

ys=["red","black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black"]

hs=[ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4]

pk=['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4',
    '5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8',
    '9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q',
    'K','K','K','K']

def pkp(x,y,z):
    t1.penup()
    t1.goto(x,y)
    t1.seth(0)
    t1.pendown()
    t1.color('black','white')
    t1.begin_fill()
    for i in range(2):
        t1.forward(90)
        t1.left(90)
        t1.forward(120)
        t1.left(90)
    t1.end_fill()
    t1.penup()
    t1.goto(x+3,y+65)
    t1.seth(0)
    t1.pendown()
    t1.pencolor(ys[z])
    t1.write(hs[z],font=("黑体",20,"normal"))
    t1.penup()
    t1.goto(x+7,y+85)
    t1.seth(0)
    t1.pendown()
    t1.write(pk[z],font=("黑体",25,"normal"))
    t1.penup()
    t1.goto(x+13,y+30)
    t1.seth(0)
    t1.pendown()
    t1.pencolor(ys[z])
    t1.write(hs[z],font=("黑体",60,"normal"))
tracer(100)
t1=Pen()
t2=Pen()
t1.hideturtle()
t2.hideturtle()
t1.pu()
t2.pu()
b=1
c=3

while(True):
    if b==1:
        t1.pu()
        t1.clear()
        t1.goto(-200,200)
        t1.pencolor('black')
        t1.write('记忆大比拼',font=('楷体',60))
        a=randint(0,51)
        pkp(-200,20,a)
        a=randint(0,51)
        pkp(100,20,a)
        a=randint(0,51)
        pkp(-200,-200,a)
        a=randint(0,51)
        pkp(100,-200,a)
        b=2
    if b==2:
        t2.goto(-20,-20)
        t2.write(c,font=("黑体",60,"normal"))
        c-=1
        sleep(1)
        t2.clear()
        if c==0:
            b=3
            c=10
    if b==3:
        t1.clear()
        t1.pu()
        t1.goto(-300,200)
        t1.pencolor('black')
        t1.write('请快速回忆牌色',font=('楷体',60))
        t2.goto(-20,-20)
        t2.write(c,font=("黑体",60,"normal"))
        c-=1
        sleep(1)
        t2.clear()
        if c==0:
            b=1
            c=3
        
        
        
        

