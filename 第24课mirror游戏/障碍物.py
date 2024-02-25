import turtle
import threading
import random


class Obstacle(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("red")
        self.shapesize(1, 2)  # 设置障碍物的大小
        self.penup()
        self.speed(0)

    def move(self):
        self.goto(random.randint(-200, 200), 200)  # 随机生成初始位置
        speed = random.randint(10, 100)
        if self.xcor() > 0:
            self.color("red")
        if self.xcor() <= 0:
            self.color("black")
        while self.ycor() > -200:  # 当障碍物还没落到屏幕底部时
            self.sety(self.ycor() - 10)  # 向下移动一定距离
            turtle.delay(speed)  # 控制障碍物下落的速度
        return self.move()


# 创建游戏界面
screen = turtle.Screen()
screen.setup(500, 500)
screen.title("下落的障碍物")

# 创建障碍物
obstacle = Obstacle()

# 创建线程用于控制障碍物下落
thread = threading.Thread(target=obstacle.move)
thread.start()

# 启动turtle事件循环
turtle.mainloop()
