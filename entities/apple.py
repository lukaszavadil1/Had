import pygame
import random
from pygame.math import Vector2
from settings import *


class Apple:
    def __init__(self, app):
        self.app = app
        self.img = pygame.image.load("imgs/apple.png")
        self.randomize()

    def draw(self):
        apple_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        self.app.screen.blit(self.img, apple_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)



