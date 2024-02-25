import pygame
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("迷宫")

# 定义颜色
BLACK = (0, 0, 0)   # 墙壁的颜色
WHITE = (255, 255, 255)   # 路径的颜色

# 定义迷宫尺寸
maze_width = 31
maze_height = 31

# 定义墙壁和路径的尺寸
wall_size = screen_width // maze_width
path_size = wall_size // 3

# 创建迷宫地图
maze_map = [[1] * maze_width for _ in range(maze_height)]

# 定义四个方向的偏移量：上、右、下、左（顺时针）
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 随机选择起始位置
start_row = random.randint(0, maze_height - 1)
start_col = random.randint(0, maze_width - 1)

# 深度优先搜索生成迷宫
def dfs(row, col):
    maze_map[row][col] = 0  # 将当前位置设为路径

    # 随机打乱四个方向
    random.shuffle(directions)

    for d_row, d_col in directions:
        new_row = row + 2 * d_row
        new_col = col + 2 * d_col

        if 0 <= new_row < maze_height and 0 <= new_col < maze_width and maze_map[new_row][new_col] == 1:
            maze_map[row + d_row][col + d_col] = 0  # 将中间位置设为路径
            dfs(new_row, new_col)

# 生成迷宫
dfs(start_row, start_col)

# 游戏主循环
running = True
while running:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制迷宫地图
    screen.fill(BLACK)
    for row in range(maze_height):
        for col in range(maze_width):
            x = col * wall_size
            y = row * wall_size
            if maze_map[row][col] == 1:   # 墙壁
                pygame.draw.rect(screen, WHITE, (x, y, wall_size, wall_size))
            else:   # 路径
                pygame.draw.rect(screen, BLACK, (x + path_size, y + path_size, path_size, path_size))

    # 刷新屏幕
    pygame.display.update()

# 退出Pygame
pygame.quit()
