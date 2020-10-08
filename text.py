import pygame
from settings import *


class Text:
    def __init__(self, app, pos, size, text, color=COLORS.get("black")):
        self.app = app
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("arial", self.size, bold=True)
        self.countdown = self.font.render(self.text, True, self.color)

    def update(self):
        pass

    def draw(self):
        # TEXT BLIT
        self.app.screen.blit(self.countdown, self.pos)
