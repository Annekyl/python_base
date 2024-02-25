import turtle


class Penx(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

    def move(self, x):
        return x + 5

    def move_f(self, x):
        self.pencolor("red")
        self.pensize(10)
        self.forward(x * 20)
        self.pencolor("black")
        self.pensize(1)


p = Penx()
p.move_f(10)
p.left(90)
p.forward(120)
turtle.mainloop()