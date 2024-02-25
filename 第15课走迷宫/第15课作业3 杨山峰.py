import turtle

lost_data = [[-300, 200], [300, 200], [-300, -200], [300, -200], [-200, 200], [-200, -100], [-100, -200], [-100, 100],
             [0, 200], [0, -100], [100, -200], [100, 100], [200, 200], [200, -100], [-300, 200], [-300, 50],
             [-300, -50], [-300, -200], [300, 200], [300, 50], [300, -50], [300, -200]]


def draw_lost():
    num = 0
    for i in range(11):
        t2.penup()
        t2.goto(lost_data[num][0], lost_data[num][1])
        t2.pendown()
        t2.goto(lost_data[num + 1][0], lost_data[num + 1][1])
        num += 2


def move_up():
    ball.sety(ball.ycor() + 5)


def move_down():
    ball.sety(ball.ycor() - 5)


def move_right():
    ball.setx(ball.xcor() + 5)


def move_left():
    ball.setx(ball.xcor() - 5)


# 1.创建窗口
game = turtle.Screen()  # 创建窗口
game.title("走迷宫")  # 给窗口命名
game.bgcolor("pink")  # 设置背景颜色
game.setup(800, 600)  # 设置窗口大小

# 2.创建物体
ball = turtle.Pen()
ball.color("purple")
ball.shape("turtle")
ball.penup()
ball.goto(-300, 0)
ball.turtlesize(2)

# 3.让物体动起来
game.listen()
game.onkeypress(move_up, 'Up')
game.onkeypress(move_down, 'Down')
game.onkeypress(move_right, 'Right')
game.onkeypress(move_left, 'Left')
# 画迷宫
turtle.tracer(False)
t2 = turtle.Pen()
t2.color("yellow")
t2.hideturtle()
t2.pensize(15)
draw_lost()
turtle.tracer(True)

turtle.mainloop()

