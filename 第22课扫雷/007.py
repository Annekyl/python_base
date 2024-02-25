import random


class Mine:
    def __init__(self, x, y):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标
        self.txt = '■'  # 文本显示
        self.stat = False  # 是否为雷
        self.mine_count = 0  # 附近的雷的数量
        self.blank = 0  # 成片空雷划分，初始值为0表示不属于任何区
        self.ee = 0

    def __str__(self):
        return "mine%d%d" % (self.x, self.y)

    def click(self):
        global Game
        if self.stat:  # 此处为雷
            Game = 1
            return  # 终止程序
        if self.mine_count != 0:  # 周围有雷
            self.txt = ' ' + str(self.mine_count)
        else:  # 周围没有雷
            self.txt = "□"


def find_blank(n, x, y):
    """
    找到成片的空雷并划分区号
    :param n: 区号
    :param x: 横坐标
    :param y: 纵坐标
    :return:
    """
    global flag
    if mines[x][y].mine_count == 0 and mines[x][y].blank == 0:
        mines[x][y].blank = n
        flag = 1
        if y + 1 < 10:
            find_blank(n, x, y + 1)
        if x + 1 < 10:
            find_blank(n, x + 1, y)
        if y - 1 >= 0:
            find_blank(n, x, y - 1)
        if x - 1 >= 0:
            find_blank(n, x - 1, y)


def eee(x, y):
    global Game
    if mines[x][y].stat != True:
        mines[x][y].click()
        if y + 1 < 10 and mines[x][y + 1].ee == 0:
            if mines[x][y + 1].blank == mines[x][y].blank:
                if mines[x][y + 1].mine_count == 0:
                    eee(x, y + 1)
            elif mines[x][y + 1].mine_count > 0:
                mines[x][y + 1].click()
        if x + 1 < 10 and mines[x + 1][y].ee == 0:
            if mines[x + 1][y].blank == mines[x][y].blank:
                if mines[x + 1][y].mine_count == 0:
                    eee(x + 1, y)
            elif mines[x + 1][y].mine_count > 0:
                mines[x + 1][y].click()
        if y - 1 >= 0 and mines[x][y - 1].ee == 0:
            if mines[x][y - 1].www == mines[x][y].www:
                if mines[x][y - 1].mine_count == 0:
                    eee(x, y - 1)
            elif mines[x][y - 1].mine_count > 0:
                mines[x][y - 1].click()
        if x - 1 > 0 and mines[x - 1][y].ee == 0:
            if mines[x - 1][y].www == mines[x][y].www:
                if mines[x - 1][y].mine_count == 0:
                    eee(x - 1, y)
            elif mines[x - 1][y].mine_count > 0:
                mines[x - 1][y].click()
    elif mines[x][y].stat == True:
        Game = 1
        return


# -----------------主程序----------------------------
# 创建二维列表用于存放雷对象
mines = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)
# 生成10个随机雷
sum = 0
while sum < 10:
    a, b = random.randint(0, 9), random.randint(0, 9)
    if not mines[a][b].stat:
        mines[a][b].stat = True
        mines[a][b].txt = "*"
        sum += 1
# 扫描附近雷的数量
print()
for i in range(10):
    for j in range(10):
        total = 0
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if 0 <= m <= 9 and 0 <= n <= 9:
                    if mines[m][n].stat:
                        total += 1
        if mines[i][j].stat:
            total = "*"
        mines[i][j].mine_count = total
# 给空雷分区号
area = 1
flag = 0
for i in range(10):
    for j in range(10):
        find_blank(area, i, j)
        if flag != 0:
            area += 1
            flag = 0
# 成片的空雷分区
print("空雷分区")
for i in range(10):
    for j in range(10):
        print(mines[i][j].blank, end=' ')
    print()
Game = 0
while Game == 0:
    # 显示全部雷
    print("用户界面")
    print("", end='  ')
    for i in range(10):
        print(i, end=' ')
    print()
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(mines[i][j].txt, end=' ')
        print()
    # 调试
    print("调试界面")
    print("", end='  ')
    for i in range(10):
        print(i, end=' ')
    print()
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(mines[i][j].mine_count, end=' ')
        print()

    # 选择雷块
    x = int(input("请输入横坐标"))
    y = int(input("请输入纵坐标"))
    mines[x][y].click()
print("游戏失败")
