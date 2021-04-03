import pygame
from settings import *


class InputBox:
    def __init__(self, app, x, y, w, h, text=''):
        self.app = app
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLORS.get("black")
        self.text = text
        self.font = pygame.font.Font(None, TEXT_SIZE.get("normal"))
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.app.player_name = self.text
                    self.app.check_scores()
                    self.app.state = "intro"
                    self.app.active_buttons = self.app.intro.intro_buttons
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # RE-RENDER
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # BOX RESIZE
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        self.app.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(self.app.screen, self.color, self.rect, 2)
