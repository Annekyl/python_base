import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('选择游戏模式')

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 加载字体
font = pygame.font.Font('字体.ttf', 20)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 检测鼠标左键点击事件
            x, y = event.pos
            if 150 <= x <= 300 and 200 <= y <= 250:  # 点击了简单模式按钮
                print("选择了简单模式")
                # 设置游戏为简单模式
            elif 500 <= x <= 650 and 200 <= y <= 250:  # 点击了困难模式按钮
                print("选择了困难模式")
                # 设置游戏为困难模式

    # 绘制界面
    screen.fill(WHITE)
    text1 = font.render("简单模式", True, BLACK)
    pygame.draw.rect(screen, RED, (150, 200, 150, 50))
    screen.blit(text1, (180, 210))
    text2 = font.render("困难模式", True, BLACK)
    pygame.draw.rect(screen, GREEN, (500, 200, 150, 50))
    screen.blit(text2, (520, 210))
    pygame.display.flip()

# 退出游戏
pygame.quit()
