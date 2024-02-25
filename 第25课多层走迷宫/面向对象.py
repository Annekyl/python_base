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

class MazeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = self.generate_maze()

    def generate_maze(self):
        # 初始化迷宫
        maze = [[1] * self.width for _ in range(self.height)]

        def generate(x, y):
            directions = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
            random.shuffle(directions)

            for dx, dy in directions:
                if 0 <= dx < self.width and 0 <= dy < self.height and maze[dy][dx] == 1:
                    maze[dy][dx] = 0
                    maze[(y + dy) // 2][(x + dx) // 2] = 0
                    generate(dx, dy)

        generate(0, 0)
        return maze

    def draw_maze(self, screen):
        screen.fill(WHITE)

        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 1:
                    pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()

        self.draw_maze(screen)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()

def main():
    # 生成迷宫游戏对象并开始游戏
    game = MazeGame(GRID_WIDTH, GRID_HEIGHT)
    game.play()

if __name__ == "__main__":
    main()
