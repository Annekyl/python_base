from turtle import *
from math import *

a=240*cos(pi/6)#方便画红球

dong=[[-380,175],[380,175],[-380,-185],[380,-185],[0,-180],[0,170]]#桌洞数据
tq=[[-180,-5],[-260,-5],[0,-5],[80,-5],[-180,75],[-180,-85],[320,-5]]#台球数据
hq=[[0,0],[a,120],[a/4,30],[a/2,60],[a*3/4,90],
    [a,-120],[a/4,-30],[a/2,-60],[a*3/4,-90],
    [a,0],[a,60],[a,-60],[a/2,0],[a*3/4,-30],[a*3/4,30]]#红球数据
ys=['orange','white','blue1','pink','green','yellow','black']#球的颜色

def xq(x,y,z):
    penup()
    goto(x,y)
    pensize(20)
    pendown()
    seth(0)
    pencolor(z)
    begin_fill()
    circle(5)
    end_fill()#设置小球的模组

speed(0)
hideturtle()
#设置基本信息

penup()
goto(-360,-200)
pensize(40)
pendown()
seth(0)
color('brown4','green3')
begin_fill()
for i in range(2):
    forward(720)
    circle(40,90)
    forward(320)
    circle(40,90)
end_fill()#画台球桌边
for i in range(6):
    penup()
    goto(dong[i][0],dong[i][1])
    pensize(40)
    pendown()
    seth(0)
    pencolor('gray')
    begin_fill()
    circle(5)
    end_fill()#画台球桌洞
penup()
goto(-180,-180)
pensize(1)
pencolor('black')
pendown()
seth(90)
forward(360)
penup()
goto(-180,-80)
seth(-180)
pendown()
circle(-80,180)#画球桌的分割线

for i in range(7):
    xq(tq[i][0],tq[i][1],ys[i])#画其他颜色的球
for i in range(15):
    xq(150+hq[i][0]/2,hq[i][1]/2-5,'red')#画红球


    


	
