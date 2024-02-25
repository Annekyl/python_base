# 载入库
import turtle as t

t.pensize(1)
t.speed(0)
t.hideturtle()


# 定义子函数
def block(a, b, x, y):
    t.color("black", "black")
    t.penup()
    t.goto(a, b)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.end_fill()


# 主程序
my_list = [[69, 15], [292, 10], [33, 8], [131, 10], [61, 5], [254, 10], [100, 15], [80, 25]]  # 数据参数
# 画框架
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

m = -350  # 定义初始横坐标
n = -200  # 定义初始纵坐标
for i in range(len(my_list)):  # 循环遍历(列表数量-1)次
    if i < len(my_list) - 1:  # 填充法绘制柱状图
        block(m, n, my_list[i][0], my_list[i][1])
        m += 50 + my_list[i + 1][1]  # 控制每个柱形的间距相等
    else:
        block(m, n, my_list[i][0], my_list[i][1])  #

t.mainloop()
