import pygame
from settings import *


class GameWindow:
    def __init__(self, app):
        self.app = app
        self.pos = WINDOW_POS
        self.width = (SCREEN_WIDTH-WINDOW_POS[0]*2)
        self.height = (SCREEN_HEIGHT-WINDOW_POS[1]*1.2)

    def update(self):
        pass

    def draw(self):
        # WINDOW
        pygame.draw.rect(self.app.screen,
                         COLORS.get("white"),
                         (self.pos[0], self.pos[1], self.width, self.height))
        # BORDER
        pygame.draw.rect(self.app.screen,
                         COLORS.get("black"),
                         (self.pos[0]-WINDOW_BORDER, self.pos[1]-WINDOW_BORDER, self.width+WINDOW_BORDER, self.height+WINDOW_BORDER), WINDOW_BORDER)
