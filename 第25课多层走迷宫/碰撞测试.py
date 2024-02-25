import pygame
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('迷宫游戏')


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # 墙壁为红色
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))  # 角色为绿色
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


wall = Wall(300, 100, 200, 20)
player = Player(100, 100)

all_sprites = pygame.sprite.Group()
all_sprites.add(wall, player)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[K_LEFT]:
        dx = -5
    elif keys[K_RIGHT]:
        dx = 5
    elif keys[K_UP]:
        dy = -5
    elif keys[K_DOWN]:
        dy = 5

    player.update(dx, dy)

    # 检测角色与墙壁的碰撞
    if pygame.sprite.spritecollide(player, all_sprites, False):
        player.rect.x -= dx
        player.rect.y -= dy

    screen.fill((255, 255, 255))

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
