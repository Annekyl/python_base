# 如果没有选到雷，那么把邻居不是雷的而且是一个数值的提取出来。
# 如果选到雷了那么bomb!game over!
import random as rd


class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.txt = "▆"
        self.df = False  # 判断是不是雷
        self.leicount = 0  # 邻居雷的数量
        self.blank = 0  # (初始是零)
        self.same_blank = 0  # 寻找相同的而且连成一片的空白区域
        self.out_blank = 0  # 翻开显现的数值

    def __str__(self):
        return 'mine%d%d' % (self.x, self.y)

    def click(self):
        global Game
        if self.df:
            self.txt = '*'
            Game = 1
            return
        if self.leicount != 0:
            self.txt = "" + str(self.leicount)
            self.out_blank = 1
        if self.leicount == 0:
            self.txt = '▢'
            self.out_blank = 1


def map1():  # (调试地图)
    print("调试图")
    for i in range(10):
        for j in range(10):  # 在这里是把所有的方块遍历一遍
            k = 0
            if not mine[i][j].df:  # 如果是不是雷那么循环遍历周围的雷数
                for m in range(i - 1, i + 2):
                    for n in range(j - 1, j + 2):
                        if 0 <= m <= 9 and 0 <= n <= 9:
                            if mine[m][n].df:
                                k += 1
                                # mine[i][j].same_blank=k
                                mine[i][j].leicount = k
            if mine[i][j].df:
                mine[i][j].leicount = '*'
    print()
    print('  ', end='')
    for i in range(10):
        print(i, end='  ')
    for i in range(10):
        print()
        print(i, end=' ')
        for j in range(10):
            print(mine[i][j].leicount, end='  ')


def find_same(n, x, y):  # 确定一样的区块
    global flag
    if mine[x][y].leicount == 0 and mine[x][y].same_blank == 0:
        mine[x][y].same_blank = n  # (周围没有雷的找出来，用n来定义)
        flag = 1  # 判断程序
        if (y + 1) < 10:
            find_same(n, x, y + 1)
        if (x + 1) < 10:
            find_same(n, x + 1, y)
        if (y - 1) >= 0:
            find_same(n, x, y - 1)
        if (x - 1) >= 0:
            find_same(n, x - 1, y)


def same_map():  # 把成片的相同的区块显示出来
    print("空雷分区")
    flag = 0
    algebra = 1
    for i in range(10):
        for j in range(10):
            find_same(algebra, i, j)
            if flag != 0:
                flag = 0
                algebra += 1
    print(' ', end=' ')
    for i in range(10):
        print(i, end=' ')
    for i in range(10):
        print()
        print(i, end=' ')
        for j in range(10):
            print(mine[i][j].same_blank, end=' ')


def strength_click(x, y):
    global Game
    if mine[x][y].leicount == 0 and mine[x][y].out_blank == 0:
        mine[x][y].click()
        for i in range(x - 1, x + 2):  # 把周围的显示了，除了雷的
            for j in range(y - 1, y + 2):
                if 0 <= i <= 9 and 0 <= j <= 9:
                    strength_click(i, j)
    if mine[x][y].leicount != 0 and mine[x][y].out_blank == 0:
        mine[x][y].click()


# ---------------------------------------------------------------------
mine = [[0 for _ in range(10)] for _ in range(10)]  # 十乘十的空（0）列表
for i in range(10):  # 数字在母函数里
    for j in range(10):
        mine[i][j] = Mine(i, j)
        # print(mine[i][j])#def __str__(self):的作用

sum = 0
while sum < 10:  # 随机做雷
    a = rd.randint(0, 9)
    b = rd.randint(0, 9)
    if not mine[a][b].df:
        mine[a][b].df = True
        mine[a][b].txt = '▆'
        sum += 1
    else:
        sum += 0

# -----------------------主函数---------------------
Game = 0
while Game == 0:
    print('  ', end='')  # 作图
    for i in range(10):
        print(i, end='  ')
    for i in range(10):
        print()
        print(i, end=' ')
        for j in range(10):
            print(mine[i][j].txt, end=' ')
    map1()
    same_map()
    print()
    zuobiao = input(f'请输入坐标：')
    zuobiao_part = zuobiao.split(',')
    xzuobiao = int(zuobiao_part[0])
    yzuobiao = int(zuobiao_part[1])
    strength_click(xzuobiao, yzuobiao)
    m = 0
    if not mine[xzuobiao][yzuobiao].df:
        print()
        m += 1
        if m == 90:
            print('congratulations!闯关通过！')
    if mine[xzuobiao][yzuobiao].df:
        print('Bomb!Game over!')
