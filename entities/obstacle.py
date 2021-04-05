import pygame
import random
from pygame.math import Vector2
from settings import *


class Obstacle:
    def __init__(self, app, x, y):
        self.app = app
        self.img = pygame.image.load("imgs/entities/obstacle.png")
        self.x = x
        self.y = y
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        obstacle_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        self.app.screen.blit(self.img, obstacle_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)


