# --------------载入库---------------
import turtle
import time

#  ---------------初始化画笔--------------------
t1 = turtle.Pen()
t2 = turtle.Pen()
t1.pensize(15)
t2.pensize(15)
t2.color("pink")
t1.speed(0)
t1.hideturtle()
t2.hideturtle()
# ---------------------数据准备---------------------
tower_data = [[-350, -100], [-100, -100], [150, -100]]
plate_data = [[-320, -80], [-50, -80], [180, -80]]
a = [3, 2, 1]
b = []
c = []


def tower(x, y):
    t1.seth(0)
    t1.pu()
    t1.goto(x, y)
    t1.pd()
    t1.forward(150)
    t1.seth(180)
    t1.forward(75)
    t1.seth(90)
    t1.forward(200)


def plates(x, y, my_list):
    t2.pu()
    t2.goto(x, y)
    t2.pd()
    t2.seth(0)
    for i in range(len(my_list)):
        t2.forward(my_list[i] * 30)
        x += 15
        y += 20
        t2.penup()
        t2.goto(x, y)
        t2.pendown()


def total_plates():
    t2.clear()
    turtle.tracer(False)
    plates(plate_data[0][0], plate_data[0][1], a)
    plates(plate_data[1][0], plate_data[1][1], b)
    plates(plate_data[2][0], plate_data[2][1], c)
    turtle.tracer(True)
    time.sleep(2)


def hannuota(i, a, b, c):
    if i == 1:
        c.append(a[len(a) - 1])
        del a[len(a) - 1]
        print(a, b, c)
        total_plates()
    else:
        hannuota(i - 1, a, c, b)
        c.append(a[len(a) - 1])
        del a[len(a) - 1]
        print(a, b, c)
        total_plates()
        hannuota(i - 1, b, a, c)


for m in range(len(tower_data)):
    tower(tower_data[m][0], tower_data[m][1])
total_plates()
hannuota(3, a, b, c)
turtle.mainloop()
