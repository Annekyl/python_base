import turtle

wolf = turtle.Turtle()  # 狼
sheep = turtle.Turtle()  # 羊
food = turtle.Turtle()  # 菜
t4 = turtle.Turtle()  # 画河流
ship = turtle.Turtle()  # 画船
turtle.hideturtle()
print(turtle.getshapes())
turtle.register_shape("狼.gif")
turtle.register_shape("羊.gif")
turtle.register_shape("菜.gif")
turtle.register_shape("船.gif")
wolf.shape("狼.gif")
sheep.shape("羊.gif")
food.shape("菜.gif")
ship.shape("船.gif")
print(turtle.shape())


def river(x, y):
    t4.penup()
    t4.goto(x, y)
    t4.pendown()
    t4.color('lightskyblue', 'lightskyblue')
    t4.begin_fill()
    t4.forward(300)
    t4.right(90)
    t4.forward(1000)
    t4.right(90)
    t4.forward(300)
    t4.right(90)
    t4.forward(1000)
    t4.end_fill()


# def move():


position = [[-600, 350], [-600, 0], [-600, -350], [600, 350], [600, 0], [600, -350]]
turtle.tracer(False)
river(-200, 500)
wolf.pu()
sheep.pu()
food.pu()
wolf.goto(position[0][0], position[0][1])
sheep.goto(position[1][0], position[1][1])
food.goto(position[2][0], position[2][1])

turtle.tracer(True)
wolf.goto(position[3][0], position[3][1])

turtle.mainloop()
