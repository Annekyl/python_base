import pygame
import random

# 定义常量
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义游戏难度对应的迷宫尺寸
DIFFICULTY_LEVELS = {
    "简单": (10, 10),
    "中等": (20, 15),
    "困难": (30, 20)
}

def generate_maze(width, height):
    # 初始化迷宫
    maze = [[1] * width for _ in range(height)]

    def generate(x, y):
        directions = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
        random.shuffle(directions)

        for dx, dy in directions:
            if 0 <= dx < width and 0 <= dy < height and maze[dy][dx] == 1:
                maze[dy][dx] = 0
                maze[(y + dy) // 2][(x + dx) // 2] = 0
                generate(dx, dy)

    generate(0, 0)
    return maze

def draw_maze(maze):
    screen.fill(WHITE)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # 游戏难度选择
    print("请选择游戏难度：")
    for i, level in enumerate(DIFFICULTY_LEVELS.keys(), start=1):
        print(f"{i}. {level}")
    choice = input("请输入选项号码：")
    while not choice.isdigit() or int(choice) <= 0 or int(choice) > len(DIFFICULTY_LEVELS):
        choice = input("输入无效，请重新输入选项号码：")
    choice = int(choice)

    # 生成迷宫
    difficulty = list(DIFFICULTY_LEVELS.keys())[choice - 1]
    maze_width, maze_height = DIFFICULTY_LEVELS[difficulty]
    maze = generate_maze(maze_width, maze_height)

    draw_maze(maze)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
