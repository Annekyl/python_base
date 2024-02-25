import turtle
import threading


class Mouse(turtle.Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.shapesize(1)
        self.penup()
        self.speed(0)
        self.x = 0
        self.y = 0

    def motion(self, event):
        self.x, self.y = event.x - 430, 400 - event.y
        self.goto(self.x, self.y)

    def symmetric_motion(self, event):
        self.x, self.y = event.x, event.y
        self.goto(-(self.x - 430), -(400 - self.y))

    def bound(self, method):
        canvas = self.screen.getcanvas()
        canvas.bind('<Motion>', method)


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.t1 = Mouse("black")
        self.t1.bound(self.t1.motion)  # 绑定鼠标移动事件
        self.t2 = Mouse("grey")
        # self.t2.bound(self.t2.symmetric_motion)

    def update_t2_position(self):
        while True:
            self.t2.goto(-self.t1.x, self.t1.y)

    def start(self):
        thread = threading.Thread(target=self.update_t2_position)
        thread.start()
        self.screen.mainloop()


game = Game()
game.start()
