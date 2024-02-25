from map import *
from player import Player

BLACK = (0, 0, 0)


class SimpleGame:
    def __init__(self, window, player_position, file, player_fill):
        """
        游戏模式
        :param window: 窗口界面
        :param player_position:玩家位置
        :param file:迷宫文件
        :param player_fill: Z玩家图片文件
        """
        # 初始化
        pygame.init()
        self.PLAYER_POSITION = player_position
        # 创建窗口
        self.window = window
        window_size = self.window.get_size()  # 获取窗口大小

        # 窗口命名
        pygame.display.set_caption("走迷宫")
        # 迷宫地图
        self.maze_map = read_txt_file(file)
        # 创建对象
        self.x = self.PLAYER_POSITION[0]
        self.y = self.PLAYER_POSITION[1]
        self.map1 = Map(self.window, window_size, self.maze_map)
        self.player = Player(self.window, self.PLAYER_POSITION[0], self.PLAYER_POSITION[1], self.map1, player_fill)
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
                self.window.fill(BLACK)
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

        pygame.quit()  # 退出pygame
