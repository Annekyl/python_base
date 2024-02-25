import turtle


def show(x, y):
    print(x, y)


wn = turtle.Screen()
wn.listen()
wn.onscreenclick(show)
turtle.done()