
import turtle as t
from time import *

turtles = []#列表分别是画笔，盘子横坐标，盘子纵坐标，盘子长度
heng1=[]
shu1=[]
chang1=[]

a=-300#三个柱子参数
b=0
c=300

def column(x,y):#画柱子
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(90)
    t.fd(800)

def disk(b,e,i,o,p):
    t.tracer(False)
    turtles[i].pensize(30)
    turtles[i].pencolor('red')
    turtles[i].pu()
    turtles[i].goto(b+o,shu1[i]+p)
    turtles[i].pd()
    turtles[i].seth(0)
    turtles[i].fd(chang1[i])
    turtles[i].pu()
    turtles[i].goto(b+o,shu1[i]+p)
    turtles[i].pd()
    turtles[i].seth(180)
    turtles[i].fd(chang1[i])
    t.update()

def move(n,b,e):
    turtles[n].clear()
    for r in range(50): #纵向移动   
        disk(b,e,n,0,r*(int(340-shu1[i])/50))#y=340
        sleep(0.01)
        turtles[n].clear()
    disk(b,b,n,0,340-shu1[i])
    turtles[n].clear()

    for r in range(50):#横向移动
        disk(b,e,n,r*(int(e-b)/50),340)
        sleep(0.01)
        turtles[n].clear()
    disk(b,e,n,e-b,0)
    turtles[n].clear()

    for r in range(50): #纵向移动   
        disk(e,e,n,0,(50-r)*int(340-shu1[i])/50)#y=340
        sleep(0.01)
        turtles[n].clear()
    disk(e,e,n,0,0)
    
    

def hanoi(n, a, b, c):#汉诺塔主体  
    if n >= 0:
        s=n-1
        # 将前 n-1 个盘子从 a 移动到 b  
        hanoi(n-1, a, c, b)  
        # 将第 n 个盘子从 a 移动到 c(move)  
        move(n,a,c)
        sleep(0.5)
        # 将前 n-1 个盘子从 b 移动到 c  
        hanoi(n-1, b, a, c)



t.tracer(False)    
column(-300,-400)#a   
column(300,-400)#c
column(0,-400)#b
t.update()

for i in range(5):#为5个盘子设置好一系列参数
    t_ = t.Turtle()    
    turtles.append(t_)
    turtles[i].hideturtle()
    shu=300-150*i
    shu1.append(shu)
    chang=20*i+8
    chang1.append(chang)


for i in range(5):#把5个盘子画在第一个柱子上
    disk(a,a,i,0,0)
    sleep(0.01)
#------------汉诺塔，启动！-------------
#j=int(input("您要调动的汉诺塔层数："))

hanoi(4, a, b, c)

t.done()#不能不加啊
    
