import sys

import pygame

# 初始化Pygame库
pygame.init()

# 设置游戏窗口大小
window_size = (640, 480)

# 创建游戏窗口
screen = pygame.display.set_mode(window_size)

# 设置游戏窗口标题
pygame.display.set_caption("迷宫游戏")

# 地图数据
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 定义墙壁和空白区域的颜色
wall_color = (255, 255, 255)
empty_color = (0, 0, 0)

# 定义墙壁和空白区域的大小
cell_size = 40

# 定义角色的颜色和大小
player_color = (0, 255, 0)
player_size = (cell_size // 2, cell_size // 2)

# 定义玩家初始位置
player_pos = [1, 1]

# 主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 处理方向键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if map_data[player_pos[1]][player_pos[0]-1] == 0:
                    player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                if map_data[player_pos[1]][player_pos[0]+1] == 0:
                    player_pos[0] += 1
            elif event.key == pygame.K_UP:
                if map_data[player_pos[1]-1][player_pos[0]] == 0:
                    player_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                if map_data[player_pos[1]+1][player_pos[0]] == 0:
                    player_pos[1] += 1

    # 绘制地图
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            # 计算当前区域左上角的坐标
            pos = (x * cell_size, y * cell_size)

            # 根据当前区域的值绘制墙壁或空白区域
            if cell == 1:
                pygame.draw.rect(screen, wall_color, (pos, (cell_size, cell_size)))
            else:
                pygame.draw.rect(screen, empty_color, (pos, (cell_size, cell_size)))

    # 绘制玩家角色
    player_rect = pygame.Rect((player_pos[0] * cell_size + cell_size // 4,
                               player_pos[1] * cell_size + cell_size // 4),
                              player_size)
    pygame.draw.rect(screen, player_color, player_rect)

    # 更新游戏窗口
    pygame.display.update()
