# 10*10空雷
class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.txt = '□'

    def __str__(self):
        return "mine%d%d" % (self.x, self.y)


mines = [[0 for _ in range(10)] for _ in range(10)]
print(mines)
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)

# print(total_mines)
for i in range(10):
    for j in range(10):
        print(mines[i][j], end='')
    print()
