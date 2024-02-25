import turtle as t
import random as r


class Mine:
    def __init__(self, turtle_pen):
        self.t1 = turtle_pen
        self.grid_count = 10
        self.grid_size = 30
        self.mine_state = [['False'] * 10 for _ in range(10)]

        self.list = [x for x in range(10)]
        self.mine_num = [[0] * 10 for _ in range(10)]
        self.mine_adjust = [['False'] * 10 for _ in range(10)]

    def pen_start(self):
        self.t1.pensize(1)
        self.t1.speed(0)
        self.t1.color('gray')
        self.t1.hideturtle()

    def color_square(self):
        self.t1._tracer(False)
        for i in range(self.grid_count):
            for j in range(self.grid_count):
                self.t1.pu()
                self.t1.goto(i * self.grid_size, (j + 1) * self.grid_size)
                self.t1.pd()
                self.t1.begin_fill()
                for z in range(4):
                    self.t1.fd(self.grid_size - 2)
                    self.t1.right(90)
                self.t1.end_fill()
        self.t1._tracer(True)

    def click(self, a, b):
# 判断点击------------------------------------------------------

        self.mine_state[a][b] = 'True'
# 画出翻开后的牌------------------------------------------------

        self.t1.color('white')
        self.t1.pu()
        self.t1.goto(a * self.grid_size, (b + 1) * self.grid_size)
        self.t1.pd()
        self.t1._tracer(False)
        self.t1.begin_fill()
        for i in range(4):
            self.t1.fd(self.grid_size)
            self.t1.right(90)
        self.t1.end_fill()

        if self.mine_adjust[a][b] != 'False':
            pass
# 显示数字------------------------------------------------------
        else:
            self.t1.color('red')
            self.t1.pu()
            self.t1.goto(a * self.grid_size + 10, b * self.grid_size)
            self.t1.pd()
            self.t1.write(self.mine_num[a][b], align='center', font=('微软雅黑', 10, 'normal'))
        self.t1._tracer(True)
        if self.mine_adjust[a][b] == "True":
            print('game over 你炸了')
            t.bye()

    # ____翻开周围的雷____
    def au_mine(self, a, b):
        a = int(a // self.grid_size)
        b = int(b // self.grid_size)
        if self.mine_state[a][b] != 'True':
            self.click(a, b)
            global mine_reveal
            mine_reveal += 1
            if self.mine_num[a][b] != 0:
                return
            if 0 <= a + 1 <= 9 and 0 <= b <= 9:
                self.au_mine((a + 1) * self.grid_size, b * self.grid_size)
            if 0 <= a - 1 <= 9 and 0 <= b <= 9:
                self.au_mine((a - 1) * self.grid_size, b * self.grid_size)
            if 0 <= a <= 9 and 0 <= b - 1 <= 9:
                self.au_mine(a * self.grid_size, (b - 1) * self.grid_size)
            if 0 <= a <= 9 and 0 <= b + 1 <= 9:
                self.au_mine(a * self.grid_size, (b + 1) * self.grid_size)

    # ——————设置雷——————
    def place_mines(self):
        s = 0
        while s <= 10:
            a = r.choice(self.list)
            b = r.choice(self.list)
            if self.mine_num[a][b] == 0:
                self.mine_adjust[a][b] = 'True'

                for i in range(3):
                    for j in range(3):
                        if 0 <= a + i - 1 <= 9 and 0 <= b + j - 1 <= 9:
                            self.mine_num[a + i - 1][b + j - 1] += 1
            s += 1


# ——————主程序编写————————
mine_reveal = 0
my_turtle = t.Turtle()
mine = Mine(my_turtle)  

mine.pen_start()
mine.color_square()
mine.place_mines()


t.onscreenclick(mine.au_mine)
if mine_reveal != 90:
    pass
else:
    print('你赢了')
    t.bye()
    t.done()
t.done()