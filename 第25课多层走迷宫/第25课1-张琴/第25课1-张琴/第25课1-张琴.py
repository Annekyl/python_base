import pygame
from map import Map


class MazeGame:
    def __init__(self, map_file):
        # 初始化 Pygame
        pygame.init()

        # 创建窗口
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('迷宫')

        # 加载地图布局
        self.map_layout = self.load_map_layout(map_file)

        # 定义墙壁和路径的颜色
        self.wall_color = (0, 0, 0)  # 墙
        self.path_color = (255, 255, 255)  # 路

        # 创建迷宫地图对象
        self.maze = self.create_maze()

        # 创建墙壁精灵组
        self.wall_sprites = pygame.sprite.Group()

        # 将墙壁精灵添加到精灵组中
        for sprite in self.maze.map_sprites:
            if sprite.image.get_at((0, 0)) == self.wall_color:
                self.wall_sprites.add(sprite)

        # 创建玩家对象
        self.player = self.create_player()

        # 创建精灵组，包括玩家精灵和墙壁精灵
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.wall_sprites)  # 添加

        # 游戏循环控制变量
        self.running = False

    def load_map_layout(self, map_file):
        map_layout = []
        with open(map_file, "r") as file:
            for ls in file:
                row = [int(cell) for cell in ls.strip().split()]
                map_layout.append(row)
        print(row)
        print(map_layout)
        return map_layout

    def create_maze(self):
        maze = Map(self.window_width, self.window_height)
        maze.load_map(self.map_layout, self.wall_color, self.path_color)
        return maze

    def create_player(self):
        player = Player(self.wall_sprites)
        return player

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:  # 按下
                if event.key == pygame.K_w:
                    self.player.is_w_pressed = True
                elif event.key == pygame.K_a:
                    self.player.is_a_pressed = True
                elif event.key == pygame.K_s:
                    self.player.is_s_pressed = True
                elif event.key == pygame.K_d:
                    self.player.is_d_pressed = True
            if event.type == pygame.KEYUP:  # 抬起
                if event.key == pygame.K_w:
                    self.player.is_w_pressed = False
                elif event.key == pygame.K_a:
                    self.player.is_a_pressed = False
                elif event.key == pygame.K_s:
                    self.player.is_s_pressed = False
                elif event.key == pygame.K_d:
                    self.player.is_d_pressed = False

    def run(self):
        # 设置游戏循环标志为True
        self.running = True

        # 创建时钟对象
        clock = pygame.time.Clock()
        fps = 60  # 帧率

        while self.running:
            # 处理事件
            self.handle_events()
            # 清空屏幕
            self.window.fill((255, 255, 255))
            # 绘制地图
            # 将窗口对象传递给迷宫地图对象
            self.maze.window = self.window
            self.maze.draw_map()
            # 更新玩家
            self.all_sprites.update()
            # 绘制玩家和墙壁
            self.all_sprites.draw(self.window)
            # 更新窗口显示
            pygame.display.update(self.player.rect)
            # 控制帧率
            clock.tick(fps)
            # 如果玩家到达终点（x坐标大于等于770），则退出循环
            if self.player.rect.x >= 770:
                break
        # 退出游戏
        pygame.quit()


class Player(pygame.sprite.Sprite):
    def __init__(self, walls):
        super().__init__()
        self.image = pygame.image.load('喜羊羊.gif')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250
        self.is_w_pressed = False  # 长按
        self.is_a_pressed = False
        self.is_s_pressed = False
        self.is_d_pressed = False
        self.walls = walls

    def update(self):
        speed = 1  # 移动速度增加到1个像素
        if self.is_w_pressed:
            self.rect.y -= speed
        if self.is_a_pressed:
            self.rect.x -= speed
        if self.is_s_pressed:
            self.rect.y += speed
        if self.is_d_pressed:
            self.rect.x += speed
        # 检测与墙壁的碰撞
        collision_sprites = pygame.sprite.spritecollide(self, self.walls, False)
        if collision_sprites:
            # 碰撞发生，阻止玩家穿过墙壁
            self.rect.x -= speed if self.is_d_pressed else 0
            self.rect.x += speed if self.is_a_pressed else 0
            self.rect.y -= speed if self.is_s_pressed else 0
            self.rect.y += speed if self.is_w_pressed else 0


def main():
    # 创建迷宫游戏对象
    game = MazeGame("地图数据.txt")
    # 运行游戏
    game.run()


if __name__ == '__main__':
    main()
