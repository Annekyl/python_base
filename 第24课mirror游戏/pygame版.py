import pygame
import random


class Window(object):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Mirror')
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), (400, 0, 400, 600))
        pygame.display.flip()
        self.mx = 0
        self.my = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#退出按钮
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    self.mx, self.my = event.pos
                    #print(self.mx)
                    self.qiu(self.mx, self.my)
            oj1.speed()
            oj2.speed()
            oj3.speed()

    def qiu(self, mx, my):
        if mx >= 420:
            pygame.draw.circle(self.screen, (255, 255, 255), (mx, my), c)
            pygame.draw.circle(self.screen, (0, 0, 0), (800 - mx, my), c)
            pygame.display.update()
            pygame.draw.circle(self.screen, (0, 0, 0), (mx, my), c)
            pygame.draw.circle(self.screen, (255, 255, 255), (800 - mx, my), c)
        elif mx <= 380:
            pygame.draw.circle(self.screen, (0, 0, 0), (mx, my), c)
            pygame.draw.circle(self.screen, (255, 255, 255), (800 - mx, my), c)
            pygame.display.update()
            pygame.draw.circle(self.screen, (255, 255, 255), (mx, my), c)
            pygame.draw.circle(self.screen, (0, 0, 0), (800 - mx, my), c)


class Oj(object):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 800)
        self.y = -20
        self.v = random.randint(2, 5)
        self.cl = (0, 0, 0)
        self.cl1 = (0, 0, 0)
        self.mun = 0
        if self.x >= 420:
            self.cl = (255, 255, 255)
            self.cl1 = (0, 0, 0)
        if self.x <= 380:
            self.cl = (0, 0, 0)
            self.cl1 = (255, 255, 255)
        if(380 < self.x < 420):
            self.__init__()

    def speed(self):
        self.mun +=1
        if self.mun % 10000 == 0:
            pygame.draw.rect(window.screen, self.cl1, (self.x, self.y, 10, 30))
            self.y += self.v
            pygame.draw.rect(window.screen, self.cl, (self.x, self.y, 10, 30))
            pygame.display.update()
        if ((self.x + 5 - window.mx)**2 + (self.y + 15 - window.my)**2 <= 900) or ((self.x + 5 + window.mx - 800)**2 + (self.y + 15 - window.my)**2 <= 900):
                print('你输了')
        if self.y >= 600:
            self.__init__()


c = 20
window = Window()
oj1 = Oj()
oj2 = Oj()
oj3 = Oj()
window.run()