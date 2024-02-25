# 载入库
import turtle as t

t.tracer(False)  # 隐藏作图轨迹


# 定义函数
def cir():  # 太阳
    t.color('red', 'red')
    t.begin_fill()
    t.penup()
    t.goto(250, 200)
    t.pendown()
    t.circle(50)
    t.end_fill()


def line(x1, y1, x2, y2, x3, y3):  # 飞机
    t.color('black', 'blue')
    t.pensize(3)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()


def line2(x1, y1, x2, y2):  # 线条
    t.penup()
    t.pensize(4)
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


# 主程序
my_list = [[0, 0], [100, 50], [-300, 150], [-300, 150], [-50, -50], [-125, -125], [-50, -50],
           [-85, -85], [-30, -125]]  # 飞机参数
my_list2 = [[75, 25], [200, 0], [50, -5], [250, -30], [10, -80],
            [100, -150], [-80, -125], [120, -200]]  # 线条参数
cir()  # 画太阳
# 画飞机
line(my_list[0][0], my_list[0][1], my_list[1][0], my_list[1][1], my_list[2][0], my_list[2][1])
line(my_list[3][0], my_list[3][1], my_list[4][0], my_list[4][1], my_list[5][0], my_list[5][1])
line(my_list[6][0], my_list[6][1], my_list[7][0], my_list[7][1], my_list[8][0], my_list[8][1])
# 画线条
line2(my_list2[0][0], my_list2[0][1], my_list2[1][0], my_list2[1][1])
line2(my_list2[2][0], my_list2[2][1], my_list2[3][0], my_list2[3][1])
line2(my_list2[4][0], my_list2[4][1], my_list2[5][0], my_list2[5][1])
line2(my_list2[6][0], my_list2[6][1], my_list2[7][0], my_list2[7][1])
line2(-80, -125, 120, -200)
line2(0, 0, -30, -125)
line2(0, 0, -30, -125)
t.mainloop()
