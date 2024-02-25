# 空雷初始状态
class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.txt = '■'

    def __str__(self):
        return "mine%d%d" % (self.x, self.y)


# 创建二维列表用于存放雷对象
mines = [[0 for _ in range(10)] for _ in range(10)]
# print(mines)

for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)

mines[0][0].txt = "▲"
mines[5][5].txt = "#"
print("", end='  ')
for i in range(1, 11):
    print(i, end=' ')
print()
for i in range(1, 11):
    print(i, end=' ')
    for j in range(10):
        print(mines[i - 1][j].txt, end=' ')
    print()
