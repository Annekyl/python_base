import turtle
from time import sleep

lost_data = [[-300, 200], [300, 200], [-300, -200], [300, -200], [-200, 200], [-200, -100], [-100, 100], [-100, -200],
             [0, 200], [0, -100], [100, 100], [100, -200], [200, 200], [200, -100], [-300, 200], [-300, 50],
             [-300, -50], [-300, -200], [300, 200], [300, 50], [300, -50], [300, -200]]


def show_time():
    t3 = turtle.Pen()
    t3.hideturtle()
    t3.penup()
    t3.goto(-120, 220)
    t3.pendown()
    turtle.tracer(0)
    time = 0
    add = 0.1
    while 1:
        t3.write("您已使用{:.1f}秒".format(time), font=("华文仿宋", 30, "normal"))
        sleep(0.1)
        time += add
        t3.clear()


def draw_lost():
    num = 0
    for i in range(11):
        t2.penup()
        t2.goto(lost_data[num][0], lost_data[num][1])
        t2.pendown()
        t2.goto(lost_data[num + 1][0], lost_data[num + 1][1])
        num += 2


def judge():
    x = ball.xcor()
    y = ball.ycor()
    if y == 170 or y == -170:
        return True
    if x == -300 and not -50 < y < 50:
        return True
    if x == 300 and not -50 < y < 50:
        return True
    for i in range(4, len(lost_data) - 1, 2):
        if lost_data[i][0] - 30 == x and lost_data[i][1] - 30 > y > lost_data[i + 1][1] + 30:
            return True
    else:
        return False


def move_up():
    if judge():
        ball.clear()
        t2.clear()
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))

    else:
        ball.sety(ball.ycor() + 5)


def move_down():
    if judge():
        ball.clear()
        t2.clear()
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))

    else:
        ball.sety(ball.ycor() - 5)


def move_right():
    if judge():
        ball.clear()
        t2.clear()
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))

    else:
        ball.setx(ball.xcor() + 5)


def move_left():
    if judge():
        ball.clear()
        t2.clear()
        t2.write("游戏失败", font=("华文仿宋", 80, "normal"))

    else:
        ball.setx(ball.ycor() - 5)


def success_way():
    t2.penup()
    t2.goto(300, -20)
    t2.pendown()
    t2.color("green", "green")
    t2.begin_fill()
    t2.circle(20)
    t2.end_fill()


def is_success():
    x = ball.xcor()
    y = ball.ycor()
    if x == 300 and y == -20:
        ball.clear()
        t2.clear()
        t2.write("游戏成功", font=("华文仿宋", 80, "normal"))


# 创建窗口
game = turtle.Screen()  # 创建窗口
game.title("走迷宫")  # 给窗口命名
game.bgcolor("pink")  # 设置背景颜色
game.setup(800, 600)  # 设置窗口大小

# 创建物体
ball = turtle.Pen()
ball.color("purple")
ball.shape("turtle")
ball.penup()
ball.goto(-300, 0)
ball.turtlesize(2)

# 画迷宫
turtle.tracer(False)
t2 = turtle.Pen()
t2.color("yellow")
t2.hideturtle()
t2.pensize(15)
draw_lost()
t2.penup()
t2.goto(-200, 0)
t2.pendown()
# turtle.tracer(True)

# 让物体动起来
game.listen()
game.onkeypress(move_up, 'Up')
game.onkeypress(move_down, 'Down')
game.onkeypress(move_right, 'Right')
game.onkeypress(move_left, 'Left')
success_way()
is_success()
show_time()

turtle.mainloop()
