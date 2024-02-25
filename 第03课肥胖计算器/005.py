#——————载入库————————
import turtle as t
t.pensize(1)
t.speed(0)
t.hideturtle()
#——————模块——————
#旗帜
def flag(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","red")
    t.begin_fill()
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.end_fill()
#大星星
def big_star(a,b):
    t.color("yellow","yellow")
    t.begin_fill()
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.right(90)
    t.forward(60)
    t.right(144)
    t.forward(60)
    t.right(144)
    t.forward(60)
    t.right(144)
    t.forward(60)
    t.right(144)
    t.forward(60)
    t.end_fill()
#小星星(左)
def star_left(m,n,k):        
    t.color("yellow","yellow")
    t.begin_fill()
    t.penup()
    t.goto(m,n)
    t.pendown()
    t.left(k)
    t.forward(20)
    t.left(144)
    t.forward(20)
    t.left(144)
    t.forward(20)
    t.left(144)
    t.forward(20)
    t.left(144)
    t.forward(20)
    t.end_fill()
#小星星(右)
def star_right(m,n,k):      
    t.color("yellow","yellow")
    t.begin_fill()
    t.penup()
    t.goto(m,n)
    t.pendown()
    t.left(k)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.end_fill()
#画整个国旗
def draw(x,y):
    flag(x,y)
    big_star(x+20,y-40)
    star_left(x+110,y-20,6)
    star_right(x+110,y-40,6)
    star_right(x+110,y-67.5,205)
    star_left(x+110,y-90,10)


#——————主程序——————

draw(-400,300)
t.right(11)
draw(100,300)
t.right(11)
draw(-400,-100)
t.right(11)
draw(100,-100)








