import random
import turtle as t

ch1='\u2665'  #红心
ch2='\u2660'  #黑桃
ch3='\u2666'  #方块
ch4='\u2663'  #梅花

ps=["red","red","red","red","red","red","red","red","red","red","red","red",
    "red","red","red","red","red","red","red","red","red","red","red","red",
    "red","red","red","black","black","black","black","black","black","black",
    "black","black","black","black","black","black","black","black","black",
    "black","black","black","black","black","black","black","black","black",
    "black","black"]

hs=[ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch1,ch3,ch3,ch3,ch3,ch3,
    ch3,ch3,ch3,ch3,ch3,ch3,ch3,ch3,"王",ch2,ch2,ch2,ch2,ch2,ch2,ch2,ch2,ch2,
    ch2,ch2,ch2,ch2,ch4,ch4,ch4,ch4,ch4,ch4,ch4,ch4,ch4,ch4,ch4,ch4,ch4,"王"]

pk=['A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6',
    '7','8','9','10','J','Q','K','大','A','2','3','4','5','6','7','8','9','10',
    'J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','小']
    



t.tracer(False)   
t.pensize(2)

def fk(x,y,z):
    t.penup()
    t.goto(x,y)
    t.seth(0)
    t.pendown()
    t.color('black','white')
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(70)
    t.end_fill()
    t.penup()
    t.goto(x+3,y+50)
    t.seth(0)
    t.pendown()
    t.pencolor(ps[z])
    t.write(pk[z],font=("微软雅黑",13,"normal"))  #20点表示的是字体尺寸，normal是字体样式
    t.penup()
    t.goto(x+3,y+30)
    t.seth(0)
    t.pendown()
    t.write(hs[z],font=("微软雅黑",13,"normal"))
    t.penup()
    t.goto(x+20,y+5)
    t.seth(0)
    t.pendown()
    t.write(hs[z],font=("微软雅黑",20,"normal"))

t.seth(0)
t.penup()
t.goto(-400,-80)
t.pendown()
t.color('grey','grey')
t.begin_fill()
t.forward(1000)
t.left(90)
t.forward(300)
t.left(90)
t.forward(1000)
t.left(90)
t.forward(300)
t.end_fill()

for i in range(17):
    a=random.randint(0,53-i)
    fk(-350+20*i,100,a)
    del pk[a]
    del hs[a]
    del ps[a]

for i in range(17):
    a=random.randint(0,36-i)
    fk(200+20*i,100,a)
    del pk[a]
    del hs[a]
    del ps[a]

for i in range(20):
    a=random.randint(0,19-i)
    fk(-100+20*i,-60,a)
    del pk[a]
    del hs[a]
    del ps[a]

