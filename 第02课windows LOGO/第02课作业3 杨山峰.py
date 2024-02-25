import turtle

turtle.pensize(3)
turtle.speed(0)
while 1:
    turtle.color("red", "white")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()

    turtle.forward(100)  # 直走

    turtle.left(80)
    turtle.forward(100)  # 上1

    turtle.right(160)
    turtle.forward(160)  # 下1

    turtle.left(160)
    turtle.forward(200)  # 上2

    turtle.right(160)
    turtle.forward(250)  # 下2

    turtle.left(155)
    turtle.forward(200)  # 上3

    turtle.right(150)
    turtle.forward(160)  # 下3

    turtle.left(140)
    turtle.forward(90)  # 上直

    turtle.right(65)
    turtle.forward(100)

    turtle.clear()
