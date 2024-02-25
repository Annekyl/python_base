import turtle as t
game=t.Screen()
game.title("迷宫")
game.bgcolor("black")
game.setup(1200,900)
t2=t.Turtle()
t2.penup()
t2.goto(-500,0)
t2.color("white")
t2.shape("circle")
t3=t.Turtle()
t3.penup()
t3.goto(500,-100)
t3.color("red")
t3.shape("circle")
def move_w():
    t2.sety(t2.ycor()+3*3)
def move_s():
    t2.sety(t2.ycor()-3*3)
def move_a():
    t2.setx(t2.xcor()-3*3)
def move_d():
    t2.setx(t2.xcor()+3*3)
game.listen() #开启球的键盘监听功能
game.onkeypress(move_w, 'Up') #按下向上键并松开，立即启动move_up()函数
game.onkeypress(move_s, 'Down')
game.onkeypress(move_a, 'Left')
game.onkeypress(move_d, 'Right')
s1=[[-350,250,350,250],[-350,-250,350,-250],[-350,80,-350,250,],[-350,-250,-350,-80],
    [350,80,350,250],[350,-250,350,-80],[-350*0.6,-80,-350*0.6,250],
    [-350*0.2,-250,-350*0.2,80],[350*0.2,-80,350*0.2,250],[350*0.6,-250,350*0.6,80]]
#画墙
t3=t.Turtle()
t3.color("green")
t3.pensize(15)
def move(x,y,z,q):
    t3.penup()
    t3.goto(x,y)
    t3.pendown()
    t3.goto(z,q)
t3._tracer(0)
for i in range (len(s1)):
    move(s1[i][0],s1[i][1],s1[i][2],s1[i][3])
t3._tracer(1)
def move(x, y, z, q):
    t3.penup()
    t3.goto(x, y)
    t3.pendown()
    t3.goto(z, q)
t3._tracer(0)
for i in range(len(s1)):
    move(s1[i][0], s1[i][1], s1[i][2], s1[i][3])
t3._tracer(1)
n = 0
t4 = t.Turtle()
t4.hideturtle()
def home():#回到原点
    w=15
    l=9
    if t2.ycor() ** 2 > 250 * 250 or t2.xcor() ** 2 > 600 * 600:
        t2.goto(-500, 0)#界
    for i in range(len(s1)):
        if s1[i][0] - w<t2.xcor()<s1[i][2] +w and s1[i][1]-l<t2.ycor()<s1[i][3]+l:
            t2.goto(-500, 0)#墙
while (1):
    t.tracer(10000)#至关重要
    home()
    game.update()
    n+=0.005
    b=float(n)
    t4.clear()
    t4.penup()
    t4.goto(500, 0)
    t4.pendown()
    t4.color("white")
    t4.write("{:.2f}".format(n), align="center", font=("Arial", 24, "normal"))
    t.time.sleep(0.001)
    if t2.distance(500,-100) < 30 :
        break
t4.penup()
t2.hideturtle()
t3.hideturtle()
t4.goto(0,0)
t4.pendown()
t4.color("white")
t4.write("游戏结束了\n 用时{:.2f}秒".format(n),align="center", font=("Arial", 50, "normal"))







