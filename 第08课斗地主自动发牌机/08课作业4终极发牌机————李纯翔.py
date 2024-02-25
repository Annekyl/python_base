#字符集代号
ch1='\u2665'   #红心
ch2='\u2660'   #黑桃
ch3='\u2666'   #方角
ch4='\u2663'   #梅花
ch5=''
#引入库
import random as r
import turtle as t
import time
t.bgcolor('gray')
#列表内容
pl=['red','black','red','black','red','black','red' \
    ,'black','red','black','red','black','red','black','red','black', \
    'red','black','red','black','red','black','red','black','red','black', \
    'red','black','red','black','red','black','red','black','red','black','red','black','red','black' \
    ,'red','black','red','black','red','black','red','black','red','black','red','black','red','black']

pk=['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4',
    '5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8',
    '9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q',
    'K','K','K','K', '大\n王','小\n王']
pc=[ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1 \
    ,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2 \
    ,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4 \
    ,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch5,ch5]

#常用模块
def star(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#牌形模块
def move(x,y):
    t.begin_fill()
    t.color('black','white')
    t.seth(0)
    star(x,y)
    t.fd(100)
    t.seth(-90)
    t.fd(120)
    t.seth(180)
    t.fd(100)
    t.seth(90)
    t.fd(120)
    t.end_fill()
#nm1的手牌
t.hideturtle()
for i in range(0,17):
    t.color('black')
    t.tracer(False)
    time.sleep(0.1)
    a=r.randint(0,53-i)
    b=i*60-420
    move(b,0)
    t.seth(-90)
    t.fd(30)
    t.seth(0)
    t.penup()
    t.fd(10)
    t.pendown()
    t.write(pk[a])
    t.seth(-90)
    t.penup()
    t.fd(10)
    t.penup()
    t.color(pl[a])
    t.write(pc[a])
    t.seth(180)
    t.penup()
    t.fd(10)
    t.seth(-90)
    t.fd(100)
    t.pendown()
    t.write(pc[a],font=("微软雅黑",100,"normal"))
    del pk[a]
    del pc[a]
    t.tracer(True)
#nm2的手牌
for i in range(0,17):
    t.color('black')
    t.tracer(False)
    time.sleep(0.1)
    a=r.randint(0,36-i)
    b=i*60-420
    move(b,-120)
    t.seth(-90)
    t.fd(30)
    t.seth(0)
    t.penup()
    t.fd(10)
    t.pendown()
    t.write(pk[a])
    t.seth(-90)
    t.penup()
    t.fd(10)
    t.penup()
    t.color(pl[a])
    t.write(pc[a])
    t.seth(180)
    t.penup()
    t.fd(10)
    t.seth(-90)
    t.fd(100)
    t.pendown()
    t.write(pc[a],font=("微软雅黑",100,"normal"))
    del pk[a]
    del pc[a]
    t.tracer(True)
#地主手牌
for i in range(0,20):
    t.color('black')
    t.tracer(False)
    time.sleep(0.1)
    a=r.randint(0,19-i)
    b=i*60-420
    move(b,120)
    t.seth(-90)
    t.fd(30)
    t.seth(0)
    t.penup()
    t.fd(10)
    t.pendown()
    t.write(pk[a])
    t.seth(-90)
    t.penup()
    t.fd(10)
    t.penup()
    t.color(pl[a])
    t.write(pc[a])
    t.seth(180)
    t.penup()
    t.fd(10)
    t.seth(-90)
    t.fd(100)
    t.pendown()
    t.write(pc[a],font=("微软雅黑",100,"normal"))
    del pk[a]
    del pc[a]
    t.tracer(True)