from map import *
class MazeGame:
    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600
        self.current_level = 1
        self.levels = ['map1.txt', 'map2.txt']
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('原神——迷宫')
        self.map_layout = self.load_map_layout()
        self.wall_color = (0, 0, 0)
        self.path_color = (255, 255, 255)
        self.maze = self.create_maze()
        self.wall_sprites = pygame.sprite.Group()
        for sprite in self.maze.map_sprites:
            if sprite.image.get_at((0, 0)) == self.wall_color:
                self.wall_sprites.add(sprite)
        self.player = self.create_player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.running = False

    def load_map_layout(self):
        level = self.levels[self.current_level - 1 ]
        with open(level, 'r') as file:
            map_layout = [[int(cell) for cell in line.strip().split()] for line in file]
        return map_layout

    def next_level(self):
        self.current_level += 1
        if self.current_level > len(self.levels):
            print("恭喜你通关了！")
            exit()
        else:
            self.wall_sprites.empty()
            self.all_sprites.remove(self.player)
            self.map_layout = self.load_map_layout()
            self.maze = self.create_maze()
            self.player = self.create_player()
            for sprite in self.maze.map_sprites:
                if sprite.image.get_at((0, 0)) == self.wall_color:
                    self.wall_sprites.add(sprite)
            self.all_sprites.add(self.player)

    def create_maze(self):
        maze = MazeMap(self.window_width, self.window_height)
        maze.load_map(self.map_layout, self.wall_color, self.path_color)
        return maze

    def create_player(self):
        player = Player(self.wall_sprites)
        return player

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.is_w_pressed = True
                elif event.key == pygame.K_a:
                    self.player.is_a_pressed = True
                elif event.key == pygame.K_s:
                    self.player.is_s_pressed = True
                elif event.key == pygame.K_d:
                    self.player.is_d_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.is_w_pressed = False
                elif event.key == pygame.K_a:
                    self.player.is_a_pressed = False
                elif event.key == pygame.K_s:
                    self.player.is_s_pressed = False
                elif event.key == pygame.K_d:
                    self.player.is_d_pressed = False

    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        fps = 100
        while self.running:
            self.handle_events()
            self.window.fill((255, 255, 255))
            self.maze.window = self.window
            self.maze.draw_map()
            self.all_sprites.update()
            self.all_sprites.draw(self.window)
            pygame.display.update(self.player.rect)
            clock.tick(fps)
            if self.player.rect.x >= 770:
                self.next_level()
                self.player.rect.x = 50
                self.player.rect.y = 540
        pygame.quit()

class Player(pygame.sprite.Sprite):
    def __init__(self, walls):
        super().__init__()
        self.image = pygame.image.load('files/胡桃.gif')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 540
        self.is_w_pressed = False
        self.is_a_pressed = False
        self.is_s_pressed = False
        self.is_d_pressed = False
        self.walls = walls

    def update(self):
        speed = 1
        if self.is_w_pressed:
            self.rect.y -= speed
        if self.is_a_pressed:
            self.rect.x -= speed
        if self.is_s_pressed:
            self.rect.y += speed
        if self.is_d_pressed:
            self.rect.x += speed
        collision_sprites = pygame.sprite.spritecollide(self, self.walls, False)
        if collision_sprites:
            self.rect.x -= speed if self.is_d_pressed else 0
            self.rect.x += speed if self.is_a_pressed else 0
            self.rect.y -= speed if self.is_s_pressed else 0
            self.rect.y += speed if self.is_w_pressed else 0
class PG:
    def __init__(self):
        game = MazeGame()
        game.run()

P = PG()
