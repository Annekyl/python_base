#------------载入函数---------
import turtle as t
t.pensize(1)
t.speed(0)
t.pensize(5)
t.hideturtle()                         #隐藏鼠标
#------------打包模块--------
def move(x,y):                         #移动
    t.penup()                          
    t.goto(x,y)                  
    t.pendown()
def c(a,b):                            #画圆
    t.circle(a,b)
def C(x,y,a,b):                        #带移动的画圆
    t.begin_fill()
    move(x,y)
    c(a,b)
    t.end_fill()
def start(x):                          #星星
    t.color('white','white')
    t.begin_fill()
    t.forward(x)                      #星星长
    t.right(144)
    t.forward(x)
    t.right(144)
    t.forward(x)
    t.right(144)
    t.forward(x)
    t.right(144)
    t.forward(x)
    t.end_fill()
def dz(a,b):                            #队长
    t.color('red','red')                #红外圈
    t.begin_fill()
    C(a,b,200,360)
    t.end_fill()
    t.color('white','white')            #白内圈 
    t.begin_fill()
    C(a,b+30,170,360)
    t.color('red','red')                #红内圈
    t.begin_fill()
    C(a,b+60,140,360)
    t.begin_fill()
    t.color('blue','blue')              #蓝底色
    t.begin_fill()
    C(a,b+90,110,360)
    move(a-105,b+232)
    start(210)                          #星星
def big_happy(a,b):                     #大笑脸
    t.color('orange','yellow')          #脸
    C(a,b,70,360)                       #70=180
    t.seth(-90)
    move(a-62,b+70)
    t.color('orange','white')           #嘴
    t.begin_fill()
    t.circle(70*8/9,180)
    t.left(90)
    t.forward(140*8/9)
    t.end_fill()
    t.seth(-90)                         #牙齿
    move(a-40,b+70)
    t.forward (120*7/18)
    move(a-20,b+70)
    t.forward (150*7/18)
    move(a,b+70)
    t.forward (160*7/18)
    move(a+20,b+70)
    t.forward (150*7/18)
    move(a+40,b+70)
    t.forward (120*7/18)
    t.seth(60)
    t.color('black','')                 #笑眼
    t.pensize (10)
    move(a-40,b+90)
    t.circle(-15,120)
    t.seth(60)
    move(a+10,b+90)
    t.circle(-15,120)
#-----------主函数------------
dz(-210,-230)                          #盾牌
t.seth(0)
dz(210,-230)                           #盾牌
t.seth(0)
big_happy(210,-100)                    #笑脸
a=input()                              #防闪退
    






