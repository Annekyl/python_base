import pygame

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

# 定义迷宫地图
maze_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 定义迷宫尺寸
maze_width = len(maze_map[0])
maze_height = len(maze_map)

# 定义墙壁和路径的尺寸
wall_size = screen_width // maze_width
path_size = wall_size // 3

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
