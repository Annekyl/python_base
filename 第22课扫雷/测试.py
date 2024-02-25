import random

# 定义雷区大小和雷的数量
rows = 5
cols = 5
num_mines = 5

# 初始化雷区
mines = [[0 for _ in range(cols)] for _ in range(rows)]

# 随机生成雷的位置
mine_positions = random.sample([(i, j) for i in range(rows) for j in range(cols)], num_mines)
for pos in mine_positions:
    mines[pos[0]][pos[1]] = -1  # -1 表示这个位置有雷

# 打印雷区（玩家看到的视图）
def print_game_board():
    for i in range(rows):
        for j in range(cols):
            if mines[i][j] == -1:
                print('X', end=' ')  # X 表示有雷的位置
            else:
                print('.', end=' ')  # . 表示无雷的位置
        print()

# 游戏主循环
while True:
    print_game_board()
    x = int(input("请输入要挖掘的格子的横坐标："))
    y = int(input("请输入要挖掘的格子的纵坐标："))

    if mines[x][y] == -1:
        print("很遗憾，你踩到了地雷！游戏结束！")
        break
    else:
        print("恭喜你，这个位置没有地雷！继续挖掘！")
