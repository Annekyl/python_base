import turtle
import turtle as t
from random import randint
import threading
from time import sleep

class BetterPen(t.Turtle):
    def __init__(self, color):
        super().__init__()
        self.speed(0)
        self.color(color, color)
        self.begin_poly()
        self.begin_fill()
        self.circle(15)
        self.end_fill()
        self.end_poly()
        self.clear()
        t.register_shape("ball", self.get_poly())
        self.shape('ball')
        self.penup()
        self.flag = True  # 添加标志属性

class Bullet(t.Turtle):
    def __init__(self, mouse_x, mouse_y):
        super().__init__()
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.bullet()

    def bullet(self):
        self.hideturtle()
        self.speed(0)
        sleep(randint(0, 25) / 10)
        self.penup()
        self.setheading(-90)
        self.shape('triangle')
        self.goto(randint(-300, 300), 300)
        self.showturtle()
        self.speed(randint(2, 3))
        while True:
            self.detect()
            self.forward(5)
            t.update()
            if self.ycor() < -350:
                break
        self.hideturtle()
        self.sety(300)
        self.showturtle()
        self.bullet()

    def detect(self):
        y = self.ycor()
        x = self.xcor()
        if y - 10 < self.mouse_y < y + 10 and x - 20 < self.mouse_x < x + 20:
            turtle.bye()
        if y - 10 < self.mouse_y < y + 10 and x - 20 < -self.mouse_x < x + 20:
            turtle.bye()

def background():
    t1 = t.Pen()
    t1.hideturtle()
    t1.speed(0)
    t1.color('red', 'red')
    t1.begin_fill()
    t1.sety(500)
    t1.setx(-400)
    t1.sety(-500)
    t1.setx(0)
    t1.end_fill()
    t1.color('blue', 'blue')
    t1.begin_fill()
    t1.sety(500)
    t1.setx(400)
    t1.sety(-500)
    t1.setx(0)
    t1.end_fill()

def create_bullet_threads(num_threads, mouse_x, mouse_y):
    threads = []
    for _ in range(num_threads):
        bullet_thread = threading.Thread(target=Bullet, args=(mouse_x, mouse_y))
        threads.append(bullet_thread)
        bullet_thread.start()
    return threads

class Game:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.listen()
        canvas = self.screen.getcanvas()
        canvas.bind('<Motion>', self.detect_and_move)

        self.pen_one = BetterPen('red')
        self.pen_two = BetterPen('blue')

        self.pen_one.flag = True
        self.pen_two.flag = True

    def detect_and_move(self, event):
        x, y = event.x - self.screen.window_width() // 2 - 15, self.screen.window_height() // 2 - event.y
        mouse_x, mouse_y = x, y
        if x >= 0:
            if self.pen_one.flag:
                self.pen_one.flag = False
                self.pen_one.goto(x, y)
                self.pen_two.goto(-x, y)
                self.pen_one.flag = True
        else:
            if self.pen_two.flag:
                self.pen_two.flag = False
                self.pen_one.goto(-x, y)
                self.pen_two.goto(x, y)
                self.pen_two.flag = True

    def start_game(self):
        background()
        t.hideturtle()
        num_threads = 5
        threads = create_bullet_threads(num_threads, 0, 0)
        t.mainloop()

if __name__ == '__main__':
    game = Game()
    game.start_game()
