#——————载入库——————
import turtle as t
t.pensize(3)
t.speed(0)
t.hideturtle()

#——————模块化设计——————
def move(x,y):      #移动画笔
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def flag():     #旗帜
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
    
def big_star(x,y):     #大星星
    t.color("yellow","yellow")
    t.begin_fill()
    t.penup()
    t.goto(x,y)
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
    
def star_left():        #小星星（起笔向左）
    t.color("yellow","yellow")
    t.begin_fill()
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
    
def star_right():       #小星星（起笔向右）
    t.color("yellow","yellow")
    t.begin_fill()
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
    
def draw_start(x,y):
    #旗帜
    move(x,y)
    flag()
    t.right(90)
    #大五角星
    big_star(x+20,y-40)
    #小五角星1
    t.left(6)
    move(x+90,y-20)
    star_left()
    #小五角星2
    t.left(6)
    move(x+110,y-40)
    star_right()
    #小五角星3
    t.right(156)
    move(x+110,y-67.5)
    star_right()
    #小五角星4
    t.left(10)
    move(x+110,y-90)
    star_left()
    t.right(10)

    
#——————主程序——————




draw_start(-400,300)
draw_start(100,300)
draw_start(-400,-100)
draw_start(100,-100)






