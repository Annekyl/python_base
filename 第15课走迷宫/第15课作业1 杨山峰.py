import turtle

game = turtle.Screen()  # 创建窗体
game.title("走迷宫")  # 给窗体命名
game.bgcolor("pink")  # 设置背景颜色
game.setup(800, 600)  # 设置窗体大小

ball = turtle.Pen()
ball.color("purple")
ball.shape("turtle")
ball.penup()
ball.goto(-300, 0)
ball.turtlesize(2)

while True:
    ball.goto(ball.xcor() + 1, ball.ycor() + 1)
