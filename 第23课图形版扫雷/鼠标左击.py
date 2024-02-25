# import turtle
#
#
# def click_handler(x, y):
#     p1.clear()
#     p1.goto(-10, -100)
#     tr1 = 'x=' + str(x) + '   y=' + str(y)
#     p1.write(tr1, align="center", font=('Arial', 30, 'normal'))
#
#
# p1 = turtle.Pen()
# p1.shape("square")
# click_handler()
# 测试鼠标单击
import turtle


def click_handler(x, y):
    p1.clear()
    p1.goto(-10, -100)
    tr1 = 'x=' + str(x) + ' y=' + str(y)
    p1.write(tr1, align="center", font=("Arial", 30, "normal"))


p1 = turtle.Pen()
p1.shape("square")
turtle.tracer(0)
screen = turtle.Screen()
screen.onclick(click_handler)
turtle.done()
