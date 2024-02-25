# ================载入模块=================
from map import *
from player import Player

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


class Game:
    def __init__(self):
        # 创建窗口
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        # 窗口命名
        pygame.display.set_caption("走迷宫")
        # 创建字体
        self.font = pygame.font.Font('字体.ttf', FONT_SIZE)
        # 设置迷宫
        self.maze_map = read_txt_file('简单模式迷宫.txt')
        # 创建对象
        self.x = PLAYER_POSITION[0]
        self.y = PLAYER_POSITION[1]
        self.map1 = Map(window, WINDOW_SIZE, self.maze_map)
        self.player = Player(window, PLAYER_POSITION[0], PLAYER_POSITION[1], self.map1, '人物.gif')
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
