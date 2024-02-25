import pygame


class Player:
    def __init__(self, window, x, y, map_obj, player_fill):
        """
        初始化
        :param window: 显示窗口
        :param x: 玩家初始横坐标
        :param y: 玩家初始纵坐标
        :param map_obj: 迷宫二维列表
        :param player_fill:玩家图片文件
        """
        self.x = x
        self.y = y
        self.player = pygame.image.load(player_fill)
        window.blit(self.player, (self.x, self.y))
        pygame.display.update()
        self.map = map_obj  # 保存地图对象
        self.rect = self.player.get_rect()  # 创建Rect对象，用于进行碰撞检测
        self.rect.x = self.x
        self.rect.y = self.y
        self.window = window

    def move(self, dx, dy):
        # 移动前先备份Rect对象的位置
        prev_x = self.rect.x
        prev_y = self.rect.y
        self.x = dx
        self.y = dy
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
                        self.window.blit(self.player, (self.x, self.y))
                        pygame.display.update()
                        self.rect.x = self.x
                        self.rect.y = self.y
                        return
        # 绘制玩家角色
        self.window.blit(self.player, (self.x, self.y))
        pygame.display.update()
