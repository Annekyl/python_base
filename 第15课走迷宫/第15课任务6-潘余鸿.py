# 想不明白怎么按键触发计时器
# 本程序计时每分钟误差不超过1s
import turtle as t
import time

game = t.Screen()  # 设幕布，标题，笔色
game.title("走迷宫")
game.bgcolor("black")
game.setup(800, 600)
t.color('blue', 'blue')
# ------------------------------------------------------------
t.speed(0)  # t画墙体 t1移动小球 t2写提示语 t3跳动计数
t1 = t.Pen()
t2 = t.Pen()
t3 = t.Pen()
t1.color('yellow')
t2.color('red')
t3.color('red')
t1.shape('circle')
t.hideturtle()
t2.hideturtle()
t3.hideturtle()
t1.pu()
t2.pu()
t3.pu()


def zhu(x, y, le, wi):  # 一个矩形区域，左下角起始坐标x,y,横轴长le,纵轴长wi
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(le)
        t.left(90)
        t.fd(wi)
        t.left(90)
    t.end_fill()


# ----------------------
t2.goto(-200, 260)
t2.write('请您穿越迷宫，到达绿色方块吧！', font=("宋体", 20))
# ----------------------
t1.goto(-320, 0)
# t1.goto(280,0)
# ------------------------
zhu(-300, 200, 600, 10)  # 1(-300,200)(300,210)
zhu(-300, -210, 600, 10)  # 2(-300,-210)(300,-200)
# ------------------------
zhu(-300, 50, 10, 150)  # 3(-300,50)(-290,200)
zhu(-205, -100, 10, 300)  # 4(-205,-100)(-195,200)
zhu(-5, -100, 10, 300)  # 5(-5,-100)(5,200)
zhu(195, -100, 10, 300)  # 6(195,-100)(205,200)
zhu(290, 50, 10, 150)  # 7(290,50)(300,200)
# -------------------------
zhu(-300, -200, 10, 150)  # 8(-300,-200)(-290,-50)
zhu(-105, -200, 10, 300)  # 9(-105,-200)(-95,100)
zhu(95, -200, 10, 300)  # 10(95,-200)(105,100)
zhu(290, -200, 10, 150)  # 11(290,-200)(300,-50)
# -------------------------
t.color('green', 'green')
zhu(310, -10, 20, 20)  # 特殊(310,-10)(330,10)
x1 = [-300, -300, -300, -205, -5, 195, 290, -300, -105, 95, 290]
x2 = [300, 300, -290, -195, 5, 205, 300, -290, -95, 105, 300]
y1 = [200, -210, 50, -100, -100, -100, 50, -200, -200, -200, -200]
y2 = [210, -200, 200, 200, 200, 200, 200, -50, 100, 100, -50]
second = 0.00
k = 0


def start():
    game.listen()  # 监视键盘
    game.onkey(move1, "Up")
    game.onkey(move2, "Down")
    game.onkey(move3, "Left")
    game.onkey(move4, "Right")


def stop():  # 中止监视
    game.onkey(None, "Up")
    game.onkey(None, "Down")
    game.onkey(None, "Left")
    game.onkey(None, "Right")


def big_judge():  # 判断球是否处于11道墙体以及终点矩形范围内
    global u
    global k
    m = t1.xcor()
    n = t1.ycor()
    for r in range(11):  # 撞到墙体
        if x2[r] >= (m - 12) and (m + 12) >= x1[r] and y2[r] >= (n - 12) and (n + 12) >= y1[r]:
            t1.color('red')
            stop()
            t2.clear()
            t2.goto(-200, 260)
            t2.write('不小心碰壁了,您可以重新开始！', font=("宋体", 20))
            k = 1
        else:  # 正常情况
            u = 1
    if 330 >= (m - 12) and (m + 12) >= 310 and 10 >= (n - 12) and (n + 12) >= -10:  # 终点
        t1.color('white')
        stop()
        t2.clear()
        t2.goto(-140, 240)
        t2.write('恭喜您到达终点！！！\n您的最终用时:%.2fs' % second, font=("宋体", 20))
        k = 1


def move1():  # 上
    big_judge()
    if u == 1:
        t1.sety(t1.ycor() + 8)


def move2():  # 下
    big_judge()
    if u == 1:
        t1.sety(t1.ycor() - 8)


def move3():  # 左
    big_judge()
    if u == 1:
        t1.setx(t1.xcor() - 8)


def move4():  # 右
    big_judge()
    if u == 1:
        t1.setx(t1.xcor() + 8)


# ------------------------主程序--------------------------
start()
while (k == 0):  # 计时器
    second += 0.061
    t3.goto(-35, 225)
    t3.write("{:.2f}".format(second), font=('宋体', 25))
    time.sleep(0.01)
    t3.clear()

t.mainloop()
