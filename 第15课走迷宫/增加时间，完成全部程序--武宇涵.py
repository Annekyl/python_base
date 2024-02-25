# ————————————————————函数定义部分————————————
def wall():
    global k
    x = ball.xcor()
    y = ball.ycor()
    for r in range(13):
        if (X1[r] < (x - 10) and X2[r] > (x + 10) and Y1[r] > (y + 10) and Y2[r] < (y - 10)):
            k = 1
    if (280 < (x - 10) and 310 > (x + 10) and 130 > (y + 10) and 40 < (y - 10)):
        k = 2


def peng():
    qiang.hideturtle()
    qiang.color("blue")
    qiang.goto(-400, -300)
    qiang.write("您已经碰到边界，请重新开始", font=("微软黑体", 40, "normal"))
    time.sleep(2)
    qiang.clear()


def victory():
    qiang.hideturtle()
    qiang.color("blue")
    qiang.goto(-200, -250)
    qiang.write("恭喜您到达终点！！！\n您的最终用时:%.2fs" % second, font=("宋体", 40, "normal"))
    time.sleep(100)


def move_up():
    global k
    wall()
    if (k == 1):
        ball.sety(ball.ycor() + 5)
    elif (k == 2):
        victory()
    else:
        t.tracer(False)
        ball.goto(-350, 75)
        t.tracer(True)
        peng()
    k -= 1


def move_down():
    global k
    wall()
    if (k == 1):
        ball.sety(ball.ycor() - 5)
    elif (k == 2):
        victory()
    else:
        t.tracer(False)
        ball.goto(-350, 75)
        t.tracer(True)
        peng()
    k -= 1


def move_right():
    global k
    wall()
    if (k == 1):
        ball.setx(ball.xcor() + 5)
    elif (k == 2):
        victory()
    else:
        t.tracer(False)
        ball.goto(-350, 75)
        t.tracer(True)
        peng()
    k -= 1


def move_left():
    global k
    wall()
    if (k == 1):
        ball.setx(ball.xcor() - 5)
    elif (k == 2):
        victory()
    else:
        t.tracer(False)
        ball.goto(-350, 75)
        t.tracer(True)
        peng()
    k -= 1


def start():
    global u
    game.listen()  # 监视键盘
    game.onkeypress(move_up, "Up")
    game.onkeypress(move_down, "Down")
    game.onkeypress(move_left, "Left")
    game.onkeypress(move_right, "Right")
    u = 1


# —————————————————————————————导入程序——————————————————————————————
import turtle as t
import time

'''
print("(请选择除了方向键以为的键来设置移动键)")
W=input("请设置向上移动的键:")
S=input("请设置向下移动的键:")
A=input("请设置向左移动的键:")
D=input("请设置向右移动的键:")
'''
# ————设置背景————
game = t.Screen()
game.title("走迷宫")
game.bgcolor("black")
game.setup(1200, 900)
# ————————————创建一支画笔来画迷宫——————————
t.tracer(False)
line = t.Pen()
line.pensize(10)
line.color("red")

line.penup()
line.goto(-300, 125)
line.seth(90)
line.pendown()
line.forward(125)
line.seth(0)
line.forward(600)
line.seth(-90)
line.forward(135)
for i in range(3):
    line.penup()
    line.goto(-200 + i * 200, 250)
    line.seth(-90)
    line.pendown()
    line.forward(250)
line.penup()
line.goto(-300, 25)
line.seth(-90)
line.pendown()
line.forward(125)
line.seth(0)
line.forward(600)
line.seth(90)
line.forward(135)
for j in range(2):
    line.penup()
    line.goto(-100 + j * 200, -100)
    line.seth(90)
    line.pendown()
    line.forward(250)
# 密封迷宫入口
line.penup()
line.goto(-300, 125)
line.pendown()
line.seth(180)
line.forward(100)
line.seth(270)
line.forward(100)
line.seth(0)
line.forward(100)
t.tracer(True)

# ————设置一个终点的画笔————
t.tracer(False)
zd = t.Pen()
zd.penup()
zd.color("purple")
zd.shape("square")
zd.shapesize(2)
zd.penup()
zd.goto(320, 75)
t.tracer(True)

# ————创建一个球————
t.tracer(False)
ball = t.Pen()
ball.color("white")
ball.shape("circle")
ball.shapesize(1)
ball.penup()
ball.goto(-350, 75)
t.tracer(True)

# ————设置一个碰墙触发的画笔————
qiang = t.Pen()
qiang.penup()
qiang.goto(-400, -300)

# ————设置按键来控制球————
X1 = [-395, -295, -295, -195, -195, -95, -95, 5, 5, 105, 105, 205, 205]
X2 = [-205, -205, -105, -105, -5, -5, 95, 95, 195, 195, 295, 295, 325]
Y1 = [120, 245, -5, 245, 245, 245, -5, 245, 245, 245, -5, 245, 120]
Y2 = [30, -95, -95, -95, 155, -95, -95, -95, 155, -95, -95, -95, 30]
k = 0

# ————用自己设置的键来控制移动方向————
'''
game.listen()    
game.onkeypress(move_up,W)
game.onkeypress(move_down,S)
game.onkeypress(move_right,D)
game.onkeypress(move_left,A)
'''
# ————方向键来控制移动————
#

# ——————编出时间的程序——————
u = 0
t3 = t.Turtle()
t3._tracer(5)
print(t3._tracer())
t3.penup()
t3.hideturtle()
t3.color("orange")
start()
second = 0
while (u == 1):
    t3.clear()
    second += 0.02
    t3.goto(-35, 320)
    t3.write("{:.2f}".format(second), font=('宋体', 40))
    time.sleep(0.01)
