import pygame
from settings import *


class Button:
    def __init__(self, app, pos, width, height, color, text_size, hover_color=None, action=None, text=None, bold=False):
        self.app = app
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.border_color = COLORS.get("black")
        self.hover_color = hover_color
        self.hovered = False
        self.action = action
        self.text = text
        self.text_size = text_size
        self.font = pygame.font.SysFont("comicsansms", text_size, bold)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()  # GETTING POSITION OF MOUSE
        # CHECKING IF THE MOUSE COORDINATES ARE INSIDE THE BUTTON RECT
        if self.pos[0] + self.width > mouse_pos[0] > self.pos[0] and self.pos[1] + self.height > mouse_pos[1] > self.pos[1]:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        # CHANGING COLOR TO HOVER COLOR IF THE MOUSE COORDINATES ARE INSIDE THE BUTTON RECT
        if not self.hovered:
            pygame.draw.rect(self.app.screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))
        else:
            pygame.draw.rect(self.app.screen, self.hover_color, (self.pos[0], self.pos[1], self.width, self.height))
        # DRAWING BUTTON BORDER
        pygame.draw.rect(self.app.screen, self.color, (self.pos[0], self.pos[1], self.width, self.height), BUTTON_BORDER)
        # DRAWING TEXT
        self.show_text()

    def click(self):
        # EXECUTING ACTION
        if self.action != None:
            self.action()
        else:
            self.color = self.hovered

    def show_text(self):
        # TEXT FONT, CENTER AND BLIT
        if self.text != None:
            text = self.font.render(self.text, True, COLORS.get("black"))
            text_size = text.get_size()
            text_pos = [(self.pos[0]+(self.width/2)-(text_size[0]/2)),
                        (self.pos[1]+(self.height/2)-(text_size[1]/2))
                        ]
            self.app.screen.blit(text, text_pos)
