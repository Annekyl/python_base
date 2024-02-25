class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.txt = '■'

    def __str__(self):
        return ("mine%d%d" % (self.x, self.y))


mines = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)
mines[0][0].txt = "▼"
mines[5][5].txt = "④"
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
