import turtle


def move_up():
    ball.sety(ball.ycor() + 5)


def move_down():
    ball.sety(ball.ycor() - 5)


def move_right():
    ball.setx(ball.xcor() + 5)


def move_left():
    ball.setx(ball.xcor() - 5)


# 1.创建窗体
game = turtle.Screen()  # 创建窗体
game.title("走迷宫")  # 给窗体命名
game.bgcolor("pink")  # 设置背景颜色
game.setup(800, 600)  # 设置窗体大小

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

turtle.mainloop()
