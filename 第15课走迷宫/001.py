import turtle

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
ball.turtlesize(3)
# 3.让物体动起来
while True:
    ball.goto(ball.xcor() + 1, ball.ycor() + 1)

# turtle.mainloop()
