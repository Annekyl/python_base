# 加十个随机雷
import random


class Mine:
    def __init__(self, x, y):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标
        self.txt = '■'  # 文本显示
        self.stat = False  # 是否为雷

    def __str__(self):
        return "mine%d%d" % (self.x, self.y)


# 创建二维列表用于存放雷对象
mines = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)

# 显示全部雷
print("用户界面")
print("", end='  ')
for i in range(1, 11):
    print(i, end=' ')
print()
for i in range(10):
    print(i, end=' ')
    for j in range(10):
        print(mines[i][j].txt, end=' ')
    print()
