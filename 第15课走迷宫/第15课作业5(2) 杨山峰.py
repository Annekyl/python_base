import turtle as t
import time

# 窗口设置
game = t.Screen()
game.title("走迷宫")
game.bgcolor("pink")
game.setup(800, 600)

# 物体
ball = t.Pen()
ball.color("purple")
ball.shape("circle")
ball.penup()
ball.goto(-300, 0)

# 迷宫初始化
t2 = t.Pen()
t2.color("yellow")
t2.hideturtle()
t2.pensize(15)
t2.speed(0)
t2.penup()
t2.goto(-200, 0)
t2.pendown()
lost_data = [[-300, 200], [300, 200], [-300, -200], [300, -200], [-200, 200], [-200, -100], [-100, 100], [-100, -200],
             [0, 200], [0, -100], [100, 100], [100, -200], [200, 200], [200, -100], [-300, 200], [-300, 50],
             [-300, -50], [-300, -200], [300, 200], [300, 50], [300, -50], [300, -200]]

# 计时器
t3 = t.Pen()
t3.penup()
t3.color("black")
t3.pensize(10)


def judge():
    x = ball.xcor()
    y = ball.ycor()
    if y == 200 or y == -200:
        return True
    if x == -300 and not -50 < y < 50:
        return True
    if x == 300 and not -50 < y < 50:
        return True
    for i in range(4, len(lost_data) - 1, 2):
        if lost_data[i][0] == x and lost_data[i][1] > y > lost_data[i + 1][1]:
            return True
    else:
        return False


def move_up():
    if judge():
        ball.clear()
        t2.clear()
        t3.clear()
        t2.goto(-200, 0)
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))

    else:
        ball.sety(ball.ycor() + 5)


def move_down():
    if judge():
        ball.clear()
        t2.clear()
        t3.clear()
        t2.goto(-200, 0)
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))
    else:
        ball.sety(ball.ycor() - 5)


def move_right():
    if judge():
        ball.clear()
        t2.clear()
        t3.clear()
        t2.goto(-200, 0)
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))
    else:
        ball.setx(ball.xcor() + 5)


def move_left():
    if judge():
        ball.clear()
        t2.clear()
        t3.clear()
        t2.goto(-200, 0)
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))
    else:
        ball.setx(ball.ycor() - 5)


def draw_lost():
    num = 0
    for i in range(11):
        t2.penup()
        t2.goto(lost_data[num][0], lost_data[num][1])
        t2.pendown()
        t2.goto(lost_data[num + 1][0], lost_data[num + 1][1])
        num += 2


# 键盘监测
game.listen()
game.onkeypress(move_up, 'Up')
game.onkeypress(move_down, 'Down')
game.onkeypress(move_right, 'Right')
game.onkeypress(move_left, 'Left')

# 绘制迷宫
draw_lost()

# 设置计时器
t3.penup()
t3.goto(-120, 220)
t3.pendown()
now_time = 0
while 1:
    t3.pu()
    now_time += 0.1
    t3.write("{:.1f}".format(now_time), font=("微软雅黑", 30, "normal"))
    time.sleep(0.1)
    t3.clear()
