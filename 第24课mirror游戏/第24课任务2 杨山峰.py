import turtle
import threading
import time
import random


class Mouse(turtle.Turtle):
    """画笔类"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.speed(0)
        self.x = 0
        self.y = 0

    def check_collision(self, obstacle):
        if self.distance(obstacle) < 20:  # 设置碰撞的距离阈值
            return True
        else:
            return False


class Obstacle(turtle.Turtle):
    """障碍物类"""

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)  # 设置障碍物的大小
        self.penup()
        self.speed(0)
        self.move()

    def move(self):
        self.goto(random.randint(-200, 200), 400)  # 随机生成初始位置
        speed = random.randint(10, 100)
        if self.xcor() > 0:
            self.color("black")
        if self.xcor() <= 0:
            self.color("red")
        while self.ycor() > -400:  # 当障碍物还没落到屏幕底部时
            a = self.ycor() - speed
            self.goto(self.xcor(), a)
            time.sleep(0.1)
        return self.move()


class Time:
    """计时器"""

    def __init__(self):

        self.time_pen = turtle.Turtle()
        self.time_pen.hideturtle()  # 隐藏画笔
        self.time_pen.pensize(10)
        self.time_pen.penup()
        self.time_pen.goto(0, -200)
        self.time_pen.color("black")

        self.start_time = None  # 计时器起始时间

    def start_timer(self):
        # 起始时间
        self.start_time = time.time()

    def get_elapsed_time(self):
        # 经历的时间
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            return round(elapsed_time, 2)  # 四舍五入得到2位小数的浮点数
        else:
            return 0.0

    def update_time_display(self):
        """计时器方法"""
        self.start_timer()
        elapsed_time = self.get_elapsed_time()  # 获取经过的时间
        self.time_pen.clear()  # 先清空原来显示的内容
        self.time_pen.write(f"{elapsed_time}", align="center", font=("Arial", 16, "normal"))  # 显示新的经过时间

        # 每隔0.05秒更新一次经过时间的显示
        turtle.ontimer(self.update_time_display, 50)


class Game:
    def __init__(self):
        """初始化游戏"""
        self.screen = turtle.Screen()  # 设置画布
        self.screen.bgcolor('pink')  # 设置背景颜色
        self.screen.title("Mirror游戏")  # 设置窗口名

        self.t1 = Mouse()  # 跟随鼠标的画笔
        self.t2 = Mouse()  # 对称画笔

        self.screen.listen()
        canvas = self.screen.getcanvas()
        canvas.bind('<Motion>', self.motion)

    def motion(self, event):
        self.t1.x, self.t1.y = event.x, event.y
        self.t2.x, self.t2.y = event.x, event.y
        if event.x > 0:
            self.t1.color("red")
            self.t2.color("black")
        else:
            self.t1.color("black")
            self.t2.color("red")
        self.t1.goto(self.t1.x - 430, 400 - self.t1.y)
        self.t2.goto(430 - self.t2.x, 400 - self.t2.y)

    def start(self):
        # 游戏主程序
        obstacles = []  # 创建障碍物列表
        threads = []
        for _ in range(7):  # 创建7个障碍物加入列表
            obstacle = Obstacle()
            thread = threading.Thread(target=obstacle.move())
            obstacles.append(obstacle)
            threads.append(thread)

        for thread in threads:
            thread.start()

        while True:
            for obstacle in obstacles:  # 循环检查每个障碍物
                if self.t1.check_collision(obstacle):
                    print("游戏失败")
                    return


game = Game()
game.start()
