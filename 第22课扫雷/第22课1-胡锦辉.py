import random as r


class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.txt = '\u25A0'
        self.number = 0
        self.statue = False  # 雷的状态
    # def click(self):


# ----------------------------------------
# ------------------扩展
def expand(x, y):  # 扩展
    global Game
    if x < 0 or x >= 10 or y < 0 or y >= 10 or mines[x][y].statue or mines[x][y].txt == '*':
        return  # 超出边界或者方块已被访问，停止扩展
    mines[x][y].statue = True  # 将此方块标记为已访问
    Game += 1
    # print(Game)#检测次数
    # print(f'{x,y}True')

    if mines[x][y].number > 0:
        return  # 如果方块周围有雷，停止扩展
    # 递归检查周围的8个方块
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                expand(x + dx, y + dy)


def Bomb_square():
    print('', end='\t')
    for i in range(10):
        print(i, end='\t')
    print()
    for i in range(10):
        print(i, end='\t')  # 行号
        for j in range(10):
            # if mines[i][j].number==0:
            # mines[i][j].statue=True
            if not mines[i][j].statue:
                print('\u25A0', end='\t')
            else:
                if mines[i][j].txt == '*':
                    print(mines[i][j].txt, end='\t')
                else:
                    if mines[i][j].number == 0:  # 如果是0打印空
                        print('\u25A1', end='\t')
                    else:
                        print(mines[i][j].number, end='\t')
        print()


mines = [[0 for _ in range(10)] for _ in range(10)]
# -----------------生成雷-----------------------
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)
n = 1
while n <= 10:  # 生成10个雷
    a, b = r.randint(0, 9), r.randint(0, 9)
    if mines[a][b].txt != '*':
        mines[a][b].txt = '*'
        n += 1

# ----------------------------------------------------------
# 游戏初始化
# -----列号------------------
print('', end='\t')
for i in range(10):
    print(i, end='\t')
print()
for i in range(10):
    print(i, end='\t')  # 行号
    for j in range(10):
        if not mines[i][j].statue:
            print('\u25A0', end='\t')
        else:
            print(mines[i][j].number, end='\t')
    print()
Game = 1
while Game <= 90:
    a = input('输入雷号:行，列 x,y')
    a1, a2 = a.split(',')
    expand(int(a1), int(a2))
    # mines[int(a1)][int(a2)].statue=True#揭开状态改变
    # -------------------------------------

    if mines[int(a1)][int(a2)].txt == '*':  # 踩雷----打印所有雷
        for i in range(10):
            for j in range(10):
                if mines[i][j].txt == '*':
                    mines[i][j].statue = True  # 将所有雷翻开
        Bomb_square()

        Game = 100  # 游戏结束
    else:  # ----未踩雷
        Bomb_square()
if 90 < Game < 100:
    print('恭喜通过')
else:
    print('Game over!')
