#------------------载入库-------------
import turtle as t
import time
#------------------数据库-------------
s=[[-200,50],[-200,200],[-100,-100],[-100,200],[0,-100],[0,200],[100,-100],[100,200],[200,50],[200,200]]
x=[[-200,-50],[-200,-200],[-50,100],[-50,-200],[50,100],[50,-200],[200,-50],[200,-200]]
zd=[[220,-20],[220,20],[260,20],[260,-20],[220,-20]]
#------------------模块化-------------
def up():
    if -215<=t1.xcor()<=215 and t1.ycor()==-215 \
    or -215<=t1.xcor()<=215 and t1.ycor()==185  \
    or -210<=t1.xcor()<=-190 and t1.ycor()==35  \
    or -110<=t1.xcor()<=-90 and t1.ycor()==-115 \
    or -10<=t1.xcor()<=10 and t1.ycor()==-115   \
    or 90<=t1.xcor()<=110 and t1.ycor()==-115   \
    or 190<=t1.xcor()<=210 and t1.ycor()==35:
        t1.sety(t1.ycor())
    else:
        t1.sety(t1.ycor()+5)
def down():
    if -215<=t1.xcor()<=215 and t1.ycor()==-185 \
    or -215<=t1.xcor()<=215 and t1.ycor()==215  \
    or -210<=t1.xcor()<=-190 and t1.ycor()==-35 \
    or -60<=t1.xcor()<=-40 and t1.ycor()==115   \
    or 40<=t1.xcor()<=60 and t1.ycor()==115     \
    or 190<=t1.xcor()<=210 and t1.ycor()==-35:
        t1.sety(t1.ycor())
    else:
        t1.sety(t1.ycor()-5)
def fd():
    if t1.xcor()==-215 and 35<=t1.ycor()<=215\
    or t1.xcor()==-215 and -215<=t1.ycor()<=-35\
    or t1.xcor()==-115 and -115<=t1.ycor()<=200\
    or t1.xcor()==-15 and -115<=t1.ycor()<=200\
    or t1.xcor()==-65 and -200<=t1.ycor()<=110\
    or t1.xcor()==35 and -200<=t1.ycor()<=110\
    or t1.xcor()==85 and -115<=t1.ycor()<=200\
    or t1.xcor()==185 and 35<=t1.ycor()<=200\
    or t1.xcor()==185 and -200<=t1.ycor()<=-35:
        t1.setx(t1.xcor())
    else:
        t1.setx(t1.xcor()+5)
def back():
    if t1.xcor()==-185 and 35<=t1.ycor()<=215\
    or t1.xcor()==-185 and -215<=t1.ycor()<=-35\
    or t1.xcor()==-85 and -115<=t1.ycor()<=200\
    or t1.xcor()==-35 and -200<=t1.ycor()<=110\
    or t1.xcor()==15 and -115<=t1.ycor()<=200\
    or t1.xcor()==65 and -200<=t1.ycor()<=110\
    or t1.xcor()==115 and -115<=t1.ycor()<=200\
    or t1.xcor()==215 and 35<=t1.ycor()<=200\
    or t1.xcor()==215 and -200<=t1.ycor()<=-35:
        t1.setx(t1.xcor())
    else:
        t1.setx(t1.xcor()-5)
#------------------主函数-------------
t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t2.pensize(10)
t2.color('yellow')
g=t.Screen()
g.bgcolor('blue')
g.title("走迷宫")
g.setup(1000,800)
t2.hideturtle()
t3.hideturtle()     #窗口

g.listen()          #键盘控制
g.onkeypress(up,'w')
g.onkeypress(down,'s')
g.onkeypress(fd,'d')
g.onkeypress(back,'a')
t1.color('white')
t1.shape('circle')
t1.pu()
t1.goto(-220,0)
t2.speed(0)
for i in range(0,10,2):     #迷宫
    t2.pu()
    t2.goto(s[i][0],s[i][1])
    t2.pd()
    t2.goto(s[i+1][0],s[i+1][1])
    t2.setx(100)
for i in range(0,8,2):
    t2.pu()
    t2.goto(x[i][0],x[i][1])
    t2.pd()
    t2.goto(x[i+1][0],x[i+1][1])
    t2.setx(100)
s=0                                     #计时器
t3.pu()
t3.goto(300,250)
t3.pd()
while 1:
    s+=0.1
    t3.write("{:.1f}".format(s),font=('楷体',60))
    time.sleep(0.1)
    t3.clear()
    
    















    
    
    
    
