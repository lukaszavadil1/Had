import pygame
import random
from settings import *

snake_head = pygame.image.load("imgs/snake_head.png")


class Snake:
    def __init__(self, app):
        self.app = app
        self.game_window = app.game_window
        self.pos = [self.game_window.width//2, self.game_window.height//2]
        self.vel = [10, 0]
        self.angle = "right"
        self.img = snake_head
        self.body = []
        self.head = self.img
        self.color = COLORS.get("light_green")
        self.snake_head = []

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

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

    def draw(self):
        self.app.screen.blit(self.head, self.pos)
