import random as r
import turtle as t
#————————————————数据部分————————
        #----------牌的形状
ch1='\u2665'#--红桃--
ch2='\u2660'#--黑桃--
ch3='\u2666'#--方块--
ch4='\u2663'#--梅花--

        #———形状的颜色库
ys=["red","black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black"]

        #——————形状库————
hs=[ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,"王","王"]

        #——————牌库——————
pk=['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4',
    '5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8',
    '9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q',
    'K','K','K','K','大','小']

#————————定义部分——————
    #-----定义一个牌的模样

def one_square(x,y,z,j,k):
    t.penup()
    t.goto(x,y)
    t.seth(0)
    t.pendown()
    t.pencolor("black")
    for i in range(2):
        t.forward(j)
        t.left(90)
        t.forward(k)
        t.left(90)
    t.penup()
    t.goto(x+5,y+5)
    t.seth(0)
    t.pendown()
    t.pencolor(ys[z])
    t.write(hs[z],font=("微软雅黑",12,"normal"))
    t.penup()
    t.goto(x+5,y+40)
    t.seth(0)
    t.pendown()
    t.write(pk[z],font=("微软雅黑",12,"normal")) 
#————————主程序部分——————————
t.setup(920,800)
t.tracer(False)#————————隐藏画面
t.ht()
t.penup()
t.pensize(2)
t.pencolor("black")
            #-----农民1牌---
for i in range(10):
    a=r.randint(0,53-i)
    one_square(-600+50*i,50,a,40,60)
    del pk[a]
    del hs[a]
    del ys[a]
    #————分段牌上10下7————
for i in range(7):
    a=r.randint(0,53-10-i)
    one_square(-600+50*i,-10,a,40,60)
    del pk[a]
    del hs[a]
    del ys[a]
    

            #------农民2牌---
for i in range(10):
    a=r.randint(0,53-17-i)
    one_square(100+50*i,50,a,40,60)
    del pk[a]
    del hs[a]
    del ys[a]
    #————分段牌上10下7————
for i in range(7):
    a=r.randint(0,53-17-10-i)
    one_square(100+50*i,-10,a,40,60)
    del pk[a]
    del hs[a]
    del ys[a]

            #-----地主牌---
for i in range(20):
    a=r.randint(0,53-34-i)
    one_square(-600+60*i,-200,a,60,80)
    del pk[a]
    del hs[a]
    del ys[a]
t.tracer(True)#————————显示画面    
a=input()








