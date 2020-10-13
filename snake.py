import pygame
import random
from settings import *

# IMAGE LOAD
snake_head = pygame.image.load("imgs/snake_head.png")


class Snake:
    def __init__(self, app):
        self.app = app
        self.game_window = app.game_window
        self.pos = [self.game_window.width//2+WINDOW_POS[0], self.game_window.height//2]
        self.vel = []
        self.angle = "right"
        self.img = snake_head
        self.body = []
        self.head = self.img
        self.color = COLORS.get("light_green")
        self.snake_head = []

    def rotate(self):
        # SNAKE - ROTATION
        if (self.angle == "right") and (self.vel[0] != -BLOCK_SIZE):
            self.head = pygame.transform.rotate(self.img, 270)
        elif (self.angle == "left") and (self.vel[0] != BLOCK_SIZE):
            self.head = pygame.transform.rotate(self.img, 90)
        elif (self.angle == "up") and (self.vel[1] != BLOCK_SIZE):
            self.head = self.img
        elif (self.angle == "down") and (self.vel[1] != -BLOCK_SIZE):
            self.head = pygame.transform.rotate(self.img, 180)
        else:
            pass

    def move(self):
        if self.angle == "right" and self.app.state == "play":
            self.vel = [20, 0]
        elif self.angle == "left" and self.app.state == "play":
            self.vel = [-20, 0]
        elif self.angle == "up" and self.app.state == "play":
            self.vel = [0, -20]
        elif self.angle == "down" and self.app.state == "play":
            self.vel = [0, 20]
        else:
            pass

    def update(self):
        self.rotate()
        self.move()
        # SNAKE - MOVEMENT
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # SNAKE - COLLISION WITH BOUNDARIES
        if self.pos[0] < WINDOW_POS[0] or self.pos[0] >= self.game_window.width or \
                self.pos[1] < WINDOW_POS[1] or self.pos[1] >= self.game_window.height+(WINDOW_POS[1]/2)+WINDOW_POS[0]:
            self.app.running = False

    def draw(self):
        # SNAKE - BLIT
        self.app.screen.blit(self.head, self.pos)
