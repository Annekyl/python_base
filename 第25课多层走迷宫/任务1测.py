# 迷宫地图，使用数字 0 表示通路，1 表示障碍物（墙）
maze_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if maze_map[self.y + dy][self.x + dx] == 0:
            self.x += dx
            self.y += dy


import pygame

# 设置窗口大小
WINDOW_SIZE = (640, 480)

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("迷宫小游戏")
        self.clock = pygame.time.Clock()
        self.player = Player(1, 1)

    def run(self):
        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.player.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0)

            # 绘制迷宫和玩家
            self.screen.fill(BLACK)
            for y in range(len(maze_map)):
                for x in range(len(maze_map[y])):
                    if maze_map[y][x] == 1:
                        pygame.draw.rect(self.screen, WHITE, (x * 40, y * 40, 40, 40))
            pygame.draw.circle(self.screen, (255, 0, 0), (self.player.x * 40 + 20, self.player.y * 40 + 20), 10)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
