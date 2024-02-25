import turtle as t


def click(x, y):
    global k
    k = 1


k = 0
t.onscreenclick(click)
