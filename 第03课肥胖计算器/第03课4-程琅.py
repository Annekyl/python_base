#------------载入库---------
import  turtle                 #载入载入库
turtle.pensize(1)              #设定画笔大小
turtle.speed(0)                #设定画笔速度

#-----------模块----------
#旗帜模块
def flag(a,b):
    turtle.color('red','red')  #设定旗帜颜色
    turtle.begin_fill()
    turtle.penup()             
    turtle.goto(a,b)     #旗帜起点
    turtle.pendown()
    turtle.forward(150)        #旗帜长度
    turtle.left(90)
    turtle.forward(100)        #旗帜宽度
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.hideturtle()


#小星星模块1
def move(x,y):
    turtle.color('yellow','yellow')    #小星星颜色
    turtle.begin_fill() 
    turtle.penup()
    turtle.goto(x,y)               #小星星位置
    turtle.pendown()

#小星星模块2
def star():         
    turtle.forward(10)              #小星星大小
    turtle.right(180-36)
    turtle.forward(10)
    turtle.right(180-36)
    turtle.forward(10)
    turtle.right(180-36)
    turtle.forward(10)
    turtle.right(180-36)
    turtle.forward(10)
    turtle.end_fill()

#大星星模块
def  bigstar(c,d):
    turtle.color('yellow','yellow')     #大星星颜色
    turtle.begin_fill() 
    turtle.penup()
    turtle.goto(c,d)                  #大星星位置
    turtle.left(90)
    turtle.pendown()
    turtle.forward(30)                  #大星星大小
    turtle.right(180-36)
    turtle.forward(30)
    turtle.right(180-36)
    turtle.forward(30)
    turtle.right(180-36)
    turtle.forward(30)
    turtle.right(180-36)
    turtle.forward(30)
    turtle.right(180-36)
    turtle.end_fill()



#-----------------主程序-------------------

#第一面国旗-------------------------
#旗帜
flag(-150,-100)

#大星星
bigstar(-130,-30)

#小星星1
move(-90,-15)           #小星星1位置
turtle.right(180-25)     #小星星1旋转角度
star()

#小星星2
move(-85,-28)            #小星星2位置
turtle.right(180-10)     #小星星2旋转角度
star()

#小星星3
move(-85,-35)             #小星星3位置
turtle.right(180-80)     #小星星3旋转角度
star() 

#小星星4
move(-90,-48)            #小星星4位置
turtle.right(180-30)     #小星星4旋转角度
star()


#第二面国旗---------------------
turtle.right(1)
#旗帜
flag(50,-100)

#大星星
bigstar(70,-30)

#小星星1
move(110,-15)           #小星星1位置
turtle.right(180-25)     #小星星1旋转角度
star()

#小星星2
move(115,-28)            #小星星2位置
turtle.right(180-10)     #小星星2旋转角度
star()

#小星星3
move(115,-35)             #小星星3位置
turtle.right(180-80)     #小星星3旋转角度
star() 

#小星星4
move(110,-48)            #小星星4位置
turtle.right(180-30)     #小星星4旋转角度
star()


#第三面国旗---------------------
turtle.right(1)
#旗帜
flag(50,100)

#大星星
bigstar(70,170)

#小星星1
move(110,185)           #小星星1位置
turtle.right(180-25)     #小星星1旋转角度
star()

#小星星2
move(115,172)            #小星星2位置
turtle.right(180-10)     #小星星2旋转角度
star()

#小星星3
move(115,165)             #小星星3位置
turtle.right(180-80)     #小星星3旋转角度
star() 

#小星星4
move(110,152)            #小星星4位置
turtle.right(180-30)     #小星星4旋转角度
star()

#第四面国旗---------------------
turtle.right(1)
#旗帜
flag(-150,100)

#大星星
bigstar(-130,170)

#小星星1
move(-90,185)           #小星星1位置
turtle.right(180-25)     #小星星1旋转角度
star()

#小星星2
move(-85,172)            #小星星2位置
turtle.right(180-10)     #小星星2旋转角度
star()

#小星星3
move(-85,165)             #小星星3位置
turtle.right(180-80)     #小星星3旋转角度
star() 

#小星星4
move(-90,152)            #小星星4位置
turtle.right(180-30)     #小星星4旋转角度
star()
