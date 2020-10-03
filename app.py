import pygame, sys
from settings import *

snake_1_head = pygame.image.load("imgs/snake_head.png")
snake_2_head = pygame.image.load("imgs/snake_head_2.png")
apple_img = pygame.image.load("imgs/apple.png")
obstacle_img = pygame.image.load("imgs/obstacle.png")


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.icon = pygame.image.load("imgs/logo.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Had")
        self.state = "intro"

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def get_events(self):
        if self.state == "intro":
            self.intro_events()

    def update(self):
        if self.state == "intro":
            self.intro_update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        if self.state == "intro":
            self.intro_draw()
        pygame.display.update()

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                self.running = False

    def intro_update(self):
        pass

    def intro_draw(self):
        pass
