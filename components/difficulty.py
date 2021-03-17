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

    def check_fps(self):
        if self.app.instructions.active_difficulty == "easy":
            self.fps = 5
        elif self.app.instructions.active_difficulty == "medium":
            self.fps = 10
        elif self.app.instructions.active_difficulty == "hard":
            self.fps = 15
        else:
            pass
