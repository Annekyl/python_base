import turtle

turtle.tracer(False)
# 隐藏绘图过程
t1 = turtle.Turtle()
t1.hideturtle()
t1.color('black', 'black')
t1.begin_fill()
t1.goto(-10, 0)
t1.goto(-10, 350)
t1.goto(0, 350)
t1.goto(0, 0)
t1.end_fill()

t2 = turtle.Turtle()
t2.hideturtle()
for a in range(30):

    t2.begin_fill()
    for i in range(2):  # 应用循环画旗面
        t2.color('red', 'red')
        t2.forward(300)
        t2.left(90)
        t2.forward(200)
        t2.left(90)

    t2.end_fill()
    # 画一个旗面
    t2.pu()
    t2.goto(20, 155 + a * 5)
    t2.pd()
    t2.color('yellow', 'yellow')
    t2.begin_fill()

    i = 1

    while i <= 5:
        t2.fd(30)
        t2.right(144)
        i = i + 1
    t2.end_fill()

    # 画一个大星星
    for i in range(4):
        t2.pu()
        t2.goto(20, 155 + a * 5)
        t2.setheading(28)
        # 设定当前朝向28度
        t2.right(23 * i)
        t2.fd(45)
        t2.pd()
        t2.begin_fill()

        for i in range(5):
            t2.fd(15)
            t2.left(144)
            i = i + 1
        t2.end_fill()
        t2.setheading(0)
        # 画四个小星星

    turtle.update()
    turtle.time.sleep(0.5)
    t2.clear()
    t2.penup()
    t2.goto(0, a * 5)
    t2.pendown()

t3 = turtle.Turtle()
t3.hideturtle()
t3.goto(0, 150)
t3.begin_fill()
for i in range(2):  # 应用循环画旗面
    t3.color('red', 'red')
    t3.forward(300)
    t3.left(90)
    t3.forward(200)
    t3.left(90)

t3.end_fill()
# 画一个旗面
t3.pu()
t3.goto(20, 305)
t3.pd()
t3.color('yellow', 'yellow')
t3.begin_fill()

i = 1

while i <= 5:
    t3.fd(30)
    t3.right(144)
    i = i + 1
t3.end_fill()

# 画一个大星星
for i in range(4):
    t3.pu()
    t3.goto(20, 305)
    t3.setheading(28)
    # 设定当前朝向28度
    t3.right(23 * i)
    t3.fd(45)
    t3.pd()
    t3.begin_fill()

    for i in range(5):
        t3.fd(15)
        t3.left(144)
        i = i + 1
    t3.end_fill()
    t3.setheading(0)

turtle.done()
