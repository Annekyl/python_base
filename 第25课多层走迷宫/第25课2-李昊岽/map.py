import pygame
class MazeMap:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        pygame.init()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.map_sprites = pygame.sprite.Group()

    def load_map(self, map_layout, wall_color, path_color):
        self.map_width = len(map_layout[0])
        self.map_height = len(map_layout)
        self.cell_width = self.window_width // 20
        self.cell_height = self.window_height // 20
        self.wall_color = wall_color
        self.path_color = path_color
        self.map_layout = map_layout
        for row in range(self.map_height):
            for col in range(self.map_width):
                if self.map_layout[row][col] == 0:
                    sprite = pygame.sprite.Sprite()
                    sprite.image = pygame.Surface((self.cell_width, self.cell_height))
                    sprite.image.fill(self.wall_color)
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = col * self.cell_width
                    sprite.rect.y = row * self.cell_height
                    self.map_sprites.add(sprite)
                else:
                    sprite = pygame.sprite.Sprite()
                    sprite.image = pygame.Surface((self.cell_width, self.cell_height))
                    sprite.image.fill(self.path_color)
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = col * self.cell_width
                    sprite.rect.y = row * self.cell_height
                    self.map_sprites.add(sprite)

    def draw_map(self):
        self.window.fill((255, 255, 255))
        self.map_sprites.draw(self.window)
        pygame.display.flip()