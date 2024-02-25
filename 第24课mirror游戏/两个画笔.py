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
        self.motion_handler = None

    def motion(self, event):
        self.x, self.y = event.x, event.y
        self.goto(self.x - 430, 400 - self.y)

    def symmetric_motion(self, event):
        self.x, self.y = event.x, event.y
        self.goto(-(self.x - 430), -(400 - self.y))


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.t1 = Mouse("black")
        self.t1.motion_handler = self.t1.motion
        self.t2 = turtle.Turtle()
        self.t2.shape("circle")
        self.t2.color("grey")
        self.t2.goto(-self.t1.x, self.t1.y)  # 设置t2的位置为t1位置的对称点

    def motion2(self):
        self.t2.goto(-self.t1.x, self.t1.y)  # 设置t2的位置为t1位置的对称点

    @staticmethod
    def bound(method):
        screen = turtle.Screen()
        canvas = screen.getcanvas()
        canvas.bind('<Motion>', method)
        screen.mainloop()

    def start(self):
        self.bound(self.t1.motion)
        thread1 = threading.Thread(target=self.motion2)
        thread1.start()
        self.screen.mainloop()


game = Game()
game.start()
