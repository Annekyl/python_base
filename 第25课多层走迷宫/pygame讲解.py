import pygame

pygame.init()  # 初始化pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()