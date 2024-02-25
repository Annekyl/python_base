import pygame
class Map:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        # 初始化 Pygame
        pygame.init()
        # 创建窗口
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("迷宫")
        # 创建精灵组
        self.map_sprites = pygame.sprite.Group()

    def load_map(self, map_layout, wall_color, path_color):
        # 定义迷宫地图的尺寸
        self.map_width = len(map_layout[0])
        self.map_height = len(map_layout)
        # 计算单个格子的宽度和高度
        self.cell_width = self.window_width // self.map_width
        self.cell_height = self.window_height // self.map_height

        self.wall_color = wall_color
        self.path_color = path_color
        self.map_layout = map_layout

        # 创建地图格子精灵并添加到精灵组
        for a in range(self.map_height):
            for b in range(self.map_width):
                if self.map_layout[a][b] == 0:
                    sprite = pygame.sprite.Sprite()
                    sprite.image = pygame.Surface((self.cell_width, self.cell_height))
                    sprite.image.fill(self.wall_color)
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = b * self.cell_width
                    sprite.rect.y = a * self.cell_height
                    self.map_sprites.add(sprite)
                else:
                    sprite = pygame.sprite.Sprite()
                    sprite.image = pygame.Surface((self.cell_width, self.cell_height))
                    sprite.image.fill(self.path_color)
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = b * self.cell_width
                    sprite.rect.y = a * self.cell_height
                    self.map_sprites.add(sprite)

    def draw_map(self):
        # 填充背景色
        self.window.fill((255, 255, 255))
        # 绘制地图精灵组
        self.map_sprites.draw(self.window)
        # 更新窗口显示
        pygame.display.flip()