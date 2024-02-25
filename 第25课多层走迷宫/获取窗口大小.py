import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('获取窗口大小')

# 获取窗口大小
window_size = screen.get_size()
print("窗口大小：", window_size)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 退出游戏
pygame.quit()
