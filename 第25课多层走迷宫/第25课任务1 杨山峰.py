# ================载入模块=================
import pygame

# ==================数据==================
# 设置窗口大小
WINDOW_SIZE = (600, 400)
# 字体大小
FONT_SIZE = 30
# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
# 对象初始位置
PLAYER_POSITION = (0, 0)

# ================准备==================
# 初始化
pygame.init()
# 创建窗口
window = pygame.display.set_mode(WINDOW_SIZE)
# 窗口命名
pygame.display.set_caption("走迷宫")
# 创建字体
font = pygame.font.Font('字体.ttf', FONT_SIZE)
# 背景音乐
pygame.mixer.music.load('青睐 - 贩卖人间黄昏.mp3')  # 载入音乐文件
pygame.mixer.music.play(-1)  # -1 表示循环播放


# =================类==================
class Player:
    def __init__(self, x, y, map_obj):
        self.x = x
        self.y = y
        self.player = pygame.image.load("人物.gif")
        window.blit(self.player, (self.x, self.y))
        pygame.display.update()
        self.map = map_obj  # 保存地图对象
        self.rect = self.player.get_rect()  # 创建Rect对象，用于进行碰撞检测
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self, dx, dy):
        # 移动前先备份Rect对象的位置
        prev_x = self.rect.x
        prev_y = self.rect.y

        self.x = dx
        self.y = dy
        # window.blit(self.player, (self.x, self.y))
        # pygame.display.update()
        self.rect.x = self.x  # 更新Rect对象的位置
        self.rect.y = self.y

        # 检测是否与墙壁碰撞
        for row in range(self.map.maze_height):
            for col in range(self.map.maze_width):
                if self.map.maze_map[row][col] == 0:  # 墙壁
                    wall_rect = pygame.Rect(col * self.map.rect_width, row * self.map.rect_height, self.map.rect_width,
                                            self.map.rect_height)  # 墙壁的Rect对象
                    if self.rect.colliderect(wall_rect):  # 两个Rect对象重叠
                        # 与墙壁碰撞，撤回移动
                        self.x = prev_x
                        self.y = prev_y
                        window.blit(self.player, (self.x, self.y))
                        pygame.display.update()
                        self.rect.x = self.x
                        self.rect.y = self.y
                        return
        # 绘制玩家角色
        window.blit(self.player, (self.x, self.y))
        pygame.display.update()


class Map:
    def __init__(self):
        # 迷宫
        self.maze_map = [
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1]
        ]  # 二维列表创建10*8的迷宫,1为路，0为墙壁
        # 计算迷宫的大小
        self.maze_width = len(self.maze_map[0])  # 长为10
        self.maze_height = len(self.maze_map)  # 宽为8

        # 定义墙壁和路径的宽和高
        self.rect_width = WINDOW_SIZE[0] / self.maze_width
        self.rect_height = WINDOW_SIZE[1] / self.maze_height

    def draw(self):
        """画迷宫"""
        for row in range(self.maze_height):
            for col in range(self.maze_width):
                x = col * self.rect_width
                y = row * self.rect_height
                if self.maze_map[row][col] == 1:  # 路
                    pygame.draw.rect(window, WHITE, (x, y, self.rect_width, self.rect_width), 0)
                else:  # 墙壁
                    pygame.draw.rect(window, BLACK, (x, y, self.rect_width, self.rect_width), 0)
        pygame.display.update()


class Game:
    def __init__(self):
        # 初始化
        pygame.init()
        # 创建窗口
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        # 窗口命名
        pygame.display.set_caption("走迷宫")
        # 创建字体
        self.font = pygame.font.Font('字体.ttf', FONT_SIZE)
        # 创建对象
        self.x = PLAYER_POSITION[0]
        self.y = PLAYER_POSITION[1]
        self.map1 = Map()
        self.player = Player(PLAYER_POSITION[0], PLAYER_POSITION[1], self.map1)
        # 游戏帧率
        self.clock = pygame.time.Clock()
        # 移动速度
        self.x_speed = 1
        self.y_speed = 1
        # 是否移动
        self.is_move = None

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            if self.is_move:
                window.fill(BLACK)
                self.map1.draw()
                self.x += self.x_speed
                self.y += self.y_speed
                self.player.move(self.x, self.y)
            # 检测事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 退出
                    running = False
                if event.type == pygame.KEYDOWN:
                    char = chr(event.key)  # 敲击的按钮
                    # 往上
                    if char == 'w':
                        self.x_speed = 0
                        self.y_speed = -1
                        self.is_move = True
                    # 往左
                    if char == 'a':
                        self.x_speed = -1
                        self.y_speed = 0
                        self.is_move = True
                    # 往下
                    if char == 's':
                        self.x_speed = 0
                        self.y_speed = 1
                        self.is_move = True
                    # 往右
                    if char == 'd':
                        self.x_speed = 1
                        self.y_speed = 0
                        self.is_move = True

                if event.type == pygame.KEYUP:
                    self.x_speed = 0
                    self.y_speed = 0
                    self.is_move = False

        pygame.mixer.music.stop()  # 停止背景音乐
        pygame.quit()  # 退出pygame


if __name__ == "__main__":
    game = Game()
    game.run()
