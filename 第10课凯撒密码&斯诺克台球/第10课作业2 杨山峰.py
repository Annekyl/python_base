# ---------------------------初始化-------------------------
import turtle as t

t.tracer(False)
t.hideturtle()


# --------------------------子函数------------------------------
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(0)


def block(x, y, length1, length2, color):
    move(x, y)
    t.color(color, color)
    t.begin_fill()
    t.forward(length1)
    t.right(90)
    t.forward(length2)
    t.right(90)
    t.forward(length1)
    t.right(90)
    t.forward(length2)
    t.end_fill()


def circle(x, y, size, color):
    move(x, y)
    t.color(color, color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


# --------------------数据列表-----------------------

# 桌面数据
desk_data = [[-400, 220, 800, 440, "darkgrey"], [-350, 175, 700, 350, "green"], [-330, 220, 660, 45, "rosybrown"],
             [-330, -175, 660, 45, "rosybrown"], [-400, 150, 50, 300, "rosybrown"], [350, 150, 50, 300, "rosybrown"]]
desk_data2 = [[-200, 175, "black", -90, 350], [-200, 70, "black", 180, 70, 180]]
# 台球数据
billiards_data = [[-200, 55, 10, "olive"], [-200, -10, 10, "khaki"], [-200, -75, 10, "yellow"],
                  [-270, -10, 10, "white"], [-50, -10, 10, "blue"], [80, -10, 10, "khaki"],
                  [300, -10, 10, "black"]]

# -------------------------主程序---------------------------

# 桌面
block(desk_data[0][0], desk_data[0][1], desk_data[0][2], desk_data[0][3], desk_data[0][4])
block(desk_data[1][0], desk_data[1][1], desk_data[1][2], desk_data[1][3], desk_data[1][4])
block(desk_data[2][0], desk_data[2][1], desk_data[2][2], desk_data[2][3], desk_data[2][4])
block(desk_data[3][0], desk_data[3][1], desk_data[3][2], desk_data[3][3], desk_data[3][4])
block(desk_data[4][0], desk_data[4][1], desk_data[4][2], desk_data[4][3], desk_data[4][4])
block(desk_data[5][0], desk_data[5][1], desk_data[5][2], desk_data[5][3], desk_data[5][4])

# 球袋
n = 140
for i in range(2):
    m = -350
    for j in range(3):
        circle(m, n, 30, "gray")
        m += 350
    n -= 330

# 线条
move(desk_data2[0][0], desk_data2[0][1])
t.color(desk_data2[0][2])
t.seth(desk_data2[0][3])
t.forward(desk_data2[0][4])
move(desk_data2[1][0], desk_data2[1][1])
t.color(desk_data2[1][2])
t.seth(desk_data2[1][3])
t.circle(desk_data2[1][4], desk_data2[1][5])

# 台球
draw = 5
p = 250
q = 30
for i in range(5):
    for j in range(draw):
        circle(p, q, 10, "darkred")
        q -= 20
    p -= 20
    q += 20 * (draw - 1) + 10
    draw -= 1

circle(billiards_data[0][0], billiards_data[0][1], billiards_data[0][2], billiards_data[0][3])
circle(billiards_data[1][0], billiards_data[1][1], billiards_data[1][2], billiards_data[1][3])
circle(billiards_data[2][0], billiards_data[2][1], billiards_data[2][2], billiards_data[2][3])
circle(billiards_data[3][0], billiards_data[3][1], billiards_data[3][2], billiards_data[3][3])
circle(billiards_data[4][0], billiards_data[4][1], billiards_data[4][2], billiards_data[4][3])
circle(billiards_data[5][0], billiards_data[5][1], billiards_data[5][2], billiards_data[5][3])
circle(billiards_data[6][0], billiards_data[6][1], billiards_data[6][2], billiards_data[6][3])

t.mainloop()
