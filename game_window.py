import pygame
from settings import *


class GameWindow:
    def __init__(self, app):
        self.app = app
        self.pos = [0, 0]

    def update(self):
        # WINDOW UPDATE
        self.app.snake.update()

    def draw(self):
        # WINDOW DRAW
        self.draw_game_window()
        self.app.snake.draw()
        self.app.apple.draw()

    def draw_game_window(self):
        # WINDOW
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.app.screen, COLORS.get("grass"), grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.app.screen, COLORS.get("grass"), grass_rect)
        pygame.draw.rect(self.app.screen,
                         COLORS.get("black"),
                         (self.pos[0], self.pos[1], CELL_NUMBER * CELL_SIZE,
                          CELL_NUMBER * CELL_SIZE + GAME_WINDOW_BORDER), GAME_WINDOW_BORDER)
