import pygame
from game import SimpleGame

# =================数据准备=====================
# 窗口大小
WINDOW_SIZE = (600, 400)
# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


class TwoGame:
    def __init__(self):
        # =================初始化====================
        # 初始化pygame
        pygame.init()
        # 初始化mixer模块
        pygame.mixer.init()
        # 创建游戏窗口
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        # 设置标题
        pygame.display.set_caption('走迷宫')
        # 加载字体
        self.font = pygame.font.Font('字体.ttf', 20)
        # 绘制界面
        self.window.fill(WHITE)
        text1 = self.font.render("简单模式", True, BLACK)
        pygame.draw.rect(self.window, RED, (50, 50, 150, 50))
        self.window.blit(text1, (85, 60))
        text2 = self.font.render("困难模式", True, BLACK)
        pygame.draw.rect(self.window, GREEN, (350, 50, 150, 50))
        self.window.blit(text2, (385, 60))
        text3 = self.font.render("噩梦模式", True, BLACK)
        pygame.draw.rect(self.window, YELLOW, (50, 200, 150, 50))
        self.window.blit(text3, (85, 210))
        text4 = self.font.render("自定义", True, BLACK)
        pygame.draw.rect(self.window, BLUE, (350, 200, 150, 50))
        self.window.blit(text4, (395, 210))

        pygame.display.flip()
        # 选择的游戏模式
        self.point = 0
        # 背景音乐
        pygame.mixer.music.load('青睐 - 贩卖人间黄昏.mp3')  # 载入音乐文件
        pygame.mixer.music.play(-1)  # -1 表示循环播放

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 退出游戏
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 50 <= x <= 200 and 50 <= y <= 100:  # 点击了简单模式按钮
                        print("选择了简单模式")
                        # 设置游戏为简单模式
                        self.point = 1
                        running = False
                    if 350 <= x <= 500 and 50 <= y <= 100:  # 点击了困难模式按钮
                        print("选择了困难模式")
                        # 设置游戏为困难模式
                        self.point = 2
                        running = False
                    if 50 <= x <= 200 <= y <= 250:  # 点击了噩梦模式按钮
                        print("选择了噩梦模式")
                        # 设置游戏为困难模式
                        self.point = 3
                        running = False
                    if 350 <= x <= 500 and 200 <= y <= 250:  # 点击了自定义模式按钮
                        print("选择了自定义模式")
                        # 设置游戏为困难模式
                        self.point = 4
                        running = False

        if self.point == 1:
            self.window.fill(BLACK)
            run_game = SimpleGame(self.window, (0, 0), '简单模式迷宫.txt', '人物.gif')
            run_game.run()
        if self.point == 2:
            self.window.fill(BLACK)
            run_game = SimpleGame(self.window, (0, 0), '困难模式迷宫.txt', '人物.gif')
            run_game.run()
        if self.point == 3:
            self.window.fill(BLACK)
            run_game = SimpleGame(self.window, (0, 0), '噩梦模式迷宫.txt', '人物(小).gif')
            run_game.run()
        if self.point == 4:
            self.window.fill(BLACK)
            run_game = SimpleGame(self.window, (0, 0), '自定义迷宫.txt', '人物.gif')
            run_game.run()
        pygame.quit()  # 退出pygame


if __name__ == "__main__":
    game = TwoGame()
    game.run()
