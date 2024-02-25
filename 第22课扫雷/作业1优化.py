import random


# ------------------定义雷块的类--------------------
class Mine:
    def __init__(self, x, y):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标
        self.txt = '■'  # 文本显示
        self.stat = False  # 是否为雷
        self.mine_count = 0  # 附近的雷的数量
        self.blank = 0  # 成片空雷划分，初始值为0表示不属于任何区

    def __str__(self):  # 显示内容
        return "mine%d%d" % (self.x, self.y)

    def click(self):  # 选择雷块
        global Game
        if self.stat:  # 选择到雷块,结束游戏
            Game = 1
            return
        if self.mine_count != 0:  # 周围有雷
            self.txt = str(self.mine_count)
        else:  # 周围没有雷
            self.txt = "□"


# -----------------------定义子函数-----------------
# 画扫雷游戏界面
def draw_map():
    print("扫雷游戏")
    print("", end='  ')
    for i in range(10):
        print(i, end=' ')
    print()
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(mines[i][j].txt, end=' ')
        print()


def scan_mines():  # 每个雷块的附近的雷的数量
    for i in range(10):
        for j in range(10):
            if not mines[i][j].stat:  # 此处不是雷
                n = 0  # 统计周围的雷的数量
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 9 >= k >= 0 and 9 >= l >= 0:
                            if mines[k][l].stat:  # 此处是雷
                                n += 1
                                mines[i][j].mine_count = n
            elif mines[i][j].stat:  # 此处是雷
                mines[i][j].mine_count = '*'


def near_mines_map():  # 作图显示附近的雷的数量
    scan_mines()  # 扫描附近雷的数量
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


def find_blank(n, x, y):
    """
    找到成片的空雷并划分区号
    :param n: 区号
    :param x: 横坐标
    :param y: 纵坐标
    :return:
    """
    global flag, area  # 判断此处是否已经划分好了空雷区
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


def click_total(x, y):
    global Game
    global count  # 统计雷块数量
    my_list = [(x, y)]  # 存储待点击的雷块坐标
    while my_list:  # 只要不是空的，就进入循环
        x, y = my_list.pop()  # 删除列表中的最后一个元素并得到返回值
        mines[x][y].click()
        if not mines[x][y].stat:  # 不是雷块
            count += 1
        if mines[x][y].mine_count == 0:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i <= 9 and 0 <= j <= 9 and mines[i][j].txt == '■':
                        mines[i][j].click()
                        my_list.append((i, j))
        if count == 90:
            Game = 2
            return


# --------------------初始化-----------------------
# 10*10的扫雷方阵
mines = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)
# print(mines)
# 随机生成10个雷
total = 0
while total < 10:
    p, q = random.randint(0, 9), random.randint(0, 9)
    if not mines[p][q].stat:
        mines[p][q].stat = True
        total += 1
# -----------------------主程序------------------------
Game = 0  # 用于判断是否点击到雷
count = 0
while Game == 0:
    draw_map()  # 扫雷界面
    near_mines_map()  # 调试界面
    # 选择雷块
    try:  # 输入的数字可能会超出范围
        xcor = int(input("请输入横坐标"))
        ycor = int(input("请输入纵坐标"))
        if xcor < 0 or xcor > 9 or ycor < 0 or ycor > 9:
            raise ValueError("坐标数值必须在0-9之间")  # ValueError数值错误
    except ValueError as e:  # 捕获异常并处理
        print("输入错误", e)
        xcor = int(input("请输入横坐标"))
        ycor = int(input("请输入纵坐标"))
    click_total(xcor, ycor)
    if Game == 1:
        print("游戏失败")
    if Game == 2:
        print("游戏成功")
