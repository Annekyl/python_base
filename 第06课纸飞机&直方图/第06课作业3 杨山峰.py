# 载入库
import turtle as t

t.pensize(1)
t.speed(0)


# 定义子函数
def line(x, y, length):  # 线条 (x,y)为线条的起点，length为线条的长度
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(90)
    t.forward(length)


# 主程序
my_list = [[69, 15], [292, 10], [33, 8], [131, 10], [61, 5], [254, 10], [100, 15], [80, 25]]  # 数据参数
# 框架
t3 = t.Turtle()
t3.penup()
t3.goto(-400, -200)
t3.pendown()
t2 = t3.clone()
t2.pensize(3)
t3.pensize(3)
t3.forward(800)
t2.seth(90)
t2.forward(400)
x = -350  # 初始横坐标
for num in range(len(my_list)):  # 循环柱状次数
    for i in range(my_list[num][1]):  # 每条柱的宽度
        line(x, -200, my_list[num][0])
        x += 1
    x += 50  # 控制每个柱之间的距离相等
t.mainloop()
