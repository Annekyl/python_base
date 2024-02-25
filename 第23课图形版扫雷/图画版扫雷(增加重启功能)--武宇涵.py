# ——————函数定义部分——————
class Mine:
    def __init__(self, x, y):
        self.x = x  # 行号,需要外界给定值
        self.y = y  # 列号,需要外界给定值
        self.txt = '■'  # 显示内容，初值为■表示未翻开
        self.stat = False  # 是否为雷,初始值为False表示无雷
        self.minecount = 0  # 邻居雷数,初始为0
        self.blank = 0  # 成片的空白区号,初值为0不属于任何一个区
        self.is_fan = 0  # 用于检测板块是否被翻开,初值为0是就是未被翻开

    def __str__(self):
        return ("mine%d%d" % (self.x, self.y))

    def click(self):
        global Game
        if self.stat == True:  # 雷被错误挖开了,炸了
            Game = 1
            return
        if self.minecount != 0:  # 不是雷,且此处邻居有雷
            self.txt = " " + str(self.minecount)
            self.is_fan = 1  # 用于检测板块是否被翻开,值为1是就是已翻开
        else:
            self.txt = "□"  # 显示□
            self.is_fan = 1


# ————用于翻开成片的空白区————
def fan(x, y):
    global Game
    if mines[x][y].stat != True:
        mines[x][y].click()
        if x + 1 < 10 and mines[x + 1][y].is_fan == 0:
            if mines[x + 1][y].blank == mines[x][y].blank:
                if mines[x + 1][y].minecount == 0:  # 对下方的物块判断
                    fan(x + 1, y)
            elif mines[x + 1][y].minecount > 0:
                mines[x + 1][y].click()
        if y + 1 < 10 and mines[x][y + 1].is_fan == 0:
            if mines[x][y + 1].blank == mines[x][y].blank:
                if mines[x][y + 1].minecount == 0:  # 对下方的物块判断
                    fan(x, y + 1)
            elif mines[x][y + 1].minecount > 0:
                mines[x][y + 1].click()
        if y - 1 >= 0 and mines[x][y - 1].is_fan == 0:
            if mines[x][y - 1].blank == mines[x][y].blank:
                if mines[x][y - 1].minecount == 0:
                    fan(x, y - 1)
            elif mines[x][y - 1].minecount > 0:
                mines[x][y - 1].click()
        if x - 1 > 0 and mines[x - 1][y].is_fan == 0:
            if mines[x - 1][y].blank == mines[x][y].blank:
                if mines[x - 1][y].minecount == 0:
                    fan(x - 1, y)
            elif mines[x - 1][y].minecount > 0:
                mines[x - 1][y].click()
    elif mines[x][y].stat == True:
        Game = 1
        return


# ————用于判断四周是否为空白块————
def find_blank(n, x, y):
    global flag
    if (mines[x][y].minecount == 0) and (mines[x][y].blank == 0):  # 看其是否为空白快
        mines[x][y].blank = n  # 是空白块就填上空白区号
        flag = 1
        if y + 1 < 10:  # 考察右边是否为空白块
            find_blank(n, x, y + 1)
        if x + 1 < 10:  # 考察下边是否为空白块
            find_blank(n, x + 1, y)
        if y - 1 >= 0:  # 考察左边是否为空白块
            find_blank(n, x, y - 1)
        if x - 1 >= 0:  # 考察上边是否为空白块
            find_blank(n, x - 1, y)


def click_handler(x, y):  # 寻找坐标
    p1.clear()
    p1.goto(-10, -300)
    tri = "x=" + str(x) + "    y=" + str(y)
    p1.write(tri, align="center", font=("Arial", 30, "normal"))


# ————用于实现点击翻格子————
def click_fan(x, y):
    global Game
    global u
    # 程序重启
    if 0 <= x <= 40 and 200 <= y <= 2400:  # 0, 150
        python = sys.executable
        os.execl(python, python, *sys.argv)
    column = 10
    row = 10
    for i in range(10):
        for j in range(10):
            if -107 + 30 * j < x < -77 + 30 * j and -190 + 30 * i < y < -160 + 30 * i:
                column = j
                row = 9 - i
    fan(row, column)
    # 画出更新后的扫雷图
    t1.clear()
    t.tracer(False)
    t1.penup()
    t1.goto(0, 0)
    # t1.write("\n\n",font=("微软黑体",10,"normal"))
    for i in range(10):
        t1.goto(-100 + 30 * i, 100)
        t1.write(str(i), font=("微软黑体", 20, "normal"))
    for i in range(10):
        t1.goto(-120, 80 - 30 * i)
        t1.write(i, font=("微软黑体", 20, "normal"))
        for j in range(10):
            t1.goto(-105 + 30 * j, 80 - 30 * i)
            t1.write(mines[i][j].txt, font=("微软黑体", 20, "normal"))

    # ————用作判断胜利条件————
    kl = 0
    for y in range(10):  # 通过剩下遍历剩下没翻的方块来判断胜利条件
        for s in range(10):
            if mines[y][s].is_fan == 0:  # 值为0表示方块未翻
                kl += 1
    t1.goto(-300, 200)
    t1.write("场上还剩{}个方块".format(kl), font=("微软黑体", 20, "normal"))
    t.tracer(True)
    if kl <= 10:
        u = 1
        t1.clear()
        t1.goto(-300, 100)
        t1.write("恭喜您获得胜利！", font=("微软黑体", 50, "normal"))
    if Game == 1:
        u = 2
        t1.clear()
        t1.goto(-300, 100)
        t1.write("Bomb,Game Over!!!", font=("微软黑体", 50, "normal"))


# ————————————————————————导入随机库————————————————————————
import random as r
import turtle as t
import time as ti
import os
import sys

# ——————创建画笔——————
t1 = t.Pen()
t1.hideturtle()
p1 = t.Pen()
p1.shape("square")
p1.hideturtle()

# ————————主程序部分————————
# ——————先新建一个10X10的空列表——————
mines = [[0 for _ in range(10)] for _ in range(10)]
# ——————再把创建的10X10的雷填写到列表中——————
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)
# ——————随机生成10个随机雷，并填写相关的雷对象的参数——————
sum = 0
while (sum < 10):
    a, b = r.randint(0, 9), r.randint(0, 9)
    if (mines[a][b].stat == False):
        mines[a][b].stat = True
        sum += 1

# ————透明扫雷作参考————
for i in range(10):  # 让点击的位置能输出周围雷的数量
    for j in range(10):
        n = 0
        if mines[i][j].stat == False:
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if 9 >= k >= 0 and 9 >= l >= 0:
                        if mines[k][l].stat == True:
                            n += 1
                            mines[i][j].minecount = n
        elif mines[i][j].stat == True:
            mines[i][j].minecount = '*'

area = 1  # 当前区号值
flag = 0  # 当前区号是否使用过
for i in range(0, 10):
    for j in range(0, 10):  # 对mines[i][j]这个雷块进行考查
        find_blank(area, i, j)  # 对当前雷块成片空白区打上区号
        if flag != 0:  # 当前区号已使用,区号要加1
            area += 1
            flag = 0
# ————重启程序————
t.tracer(False)
game_again = t.Pen()  # 重启图案
game_again.ht()
game_again.pu()
game_again.goto(0, 200)
game_again.pd()
game_again.color('black', 'yellow')
game_again.begin_fill()
for i in range(4):
    game_again.fd(40)
    game_again.left(90)
game_again.end_fill()
t.tracer(True)

# ————把10X10个空雷初始状态显示出来，要加上行列号————
Game = 0
t1.clear()
t.tracer(False)
t1.penup()
t1.goto(0, 0)
for i in range(10):
    t1.goto(-100 + 30 * i, 100)
    t1.write(str(i), font=("微软黑体", 20, "normal"))
for i in range(10):
    t1.goto(-120, 80 - 30 * i)
    t1.write(i, font=("微软黑体", 20, "normal"))
    for j in range(10):
        t1.goto(-105 + 30 * j, 80 - 30 * i)
        t1.write(mines[i][j].txt, font=("微软黑体", 20, "normal"))
t.tracer(True)
# ————寻找坐标————

t2 = t.Pen()
t2.hideturtle()
t2.penup()
sta = 1
add = 0.025
sao_time = 0
while sta == 1:
    u = 0
    t.tracer(100)
    t2.clear()
    sao_time += add
    t2.goto(200, 200)
    t2.write("{:.2f}s".format(sao_time), font=("微软黑体", 40, "normal"))
    ti.sleep(0.01)
    t.onscreenclick(click_fan)
    # t.onscreenclick(click)  # 在游戏结束时也能检测重启
    if u == 1:
        # game_again.clear()
        sta = 0
        t2.clear()
        t2.goto(-300, -150)
        t2.write("您总共花费了{:.2f}s".format(sao_time), font=("微软黑体", 20, "normal"))
    if u == 2:
        # game_again.clear()
        sta = 0
        t2.clear()
        t2.goto(-300, -100)
        t2.write("您花费了{:.2f}s,并且失败了".format(sao_time), font=("微软黑体", 30, "normal"))
