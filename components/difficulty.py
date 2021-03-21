import pygame
from settings import *

class Difficulty:
    def __init__(self, app, pos, type):
        self.app = app
        self.pos = pos
        self.type = type

    def update(self):
        pass

    def draw(self):
        # HEAD BLIT
        self.app.screen.blit(self.type, self.pos)

