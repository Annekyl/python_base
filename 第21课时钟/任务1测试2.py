import turtle as t

t4 = t.Pen()
t4.pensize(3)

def draw_clock():
    for i in range(60):
        t.tracer(0)
        if i % 5 == 0:
            t4.color("red")
        else:
            t4.color("black")
        t4.penup()
        t4.seth(i * 6)
        t4.fd(100)
        t4.pendown()
        t4.fd(15)
        t4.penup()
        t4.goto(0, 0)


draw_clock()
t.mainloop()