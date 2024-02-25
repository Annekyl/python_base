import random as r


class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.txt = '■'
        self.stat = False
        self.minecount = 0  # 显示周围有几个雷
        self.www = 0

    def __str__(self):
        return ("mine%d%d" % (self.x, self.y))

    def click(self):
        global Game
        if self.stat == True:
            Game = 1
            return
        elif self.minecount != 0:
            self.txt = " " + str(self.minecount)
        else:
            self.txt = "□"


mines = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)
sum = 0

while (sum < 10):
    a, b = r.randint(0, 9), r.randint(0, 9)
    if (mines[a][b].stat == False):
        mines[a][b].stat = True
        # mines[a][b].txt='❁'
        sum += 1

for i in range(10):
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
Game = 0


def find_www(n, x, y):
    global flag
    if (mines[x][y].minecount == 0) and (mines[x][y].www == 0):
        mines[x][y].www = n
        flag = 1
        if y + 1 < 10:
            find_www(n, x, y + 1)
        if x + 1 < 10:
            find_www(n, x + 1, y)
        if y - 1 >= 0:
            find_www(n, x, y - 1)
        if x - 1 > 0:
            find_www(n, x - 1, y)


area = 1
flag = 0
for i in range(0, 10):
    for j in range(0, 10):
        find_www(area, i, j)
        if flag != 0:
            area += 1
            flag = 0
while (Game == 0):
    print("\n\n", end=' ')
    for i in range(10):
        print(' ' + str(i), end=' ')
    print()
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(mines[i][j].txt, end=' ')
        print()
    # ■□
    print("\n\n", end=' ')
    for i in range(10):
        print(i, end=' ')
    print()
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(mines[i][j].minecount, end=' ')
        print()

    print("\n\n", end=' ')
    for i in range(10):
        print(i, end=' ')
    print()
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(mines[i][j].www, end=' ')
        print()

    an = input("请输入单击雷块的(行,列)：")
    an = an.split(",")
    an1, an2 = int(an[0]), int(an[1])
    mines[an1][an2].click()
print("游戏结束")
