import pygame
from settings import *
from button import *


class Instructions:
    def __init__(self, app):
        self.instructions_buttons = []
        self.app = app

    def instructions_events(self):
        # INSTRUCTIONS EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.instructions_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass

    def instructions_update(self):
        # INSTRUCTIONS STATE UPDATE
        for button in self.app.active_buttons:
            button.update()

    def instructions_draw(self):
        # INSTRUCTIONS STATE DRAW
        for button in self.app.active_buttons:
            button.draw()

    def instructions_intro(self):
        # FROM INSTRUCTIONS STATE TO INTRO
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons

    def instructions_quit(self):
        # QUIT FROM INSTRUCTIONS STATE
        self.app.running = False

    def make_instructions_buttons(self):
        # MAKE INSTRUCTIONS BUTTONS
        instructions_intro_button = Button(self.app,
                                        [(SCREEN_HEIGHT / 2) - 100, SCREEN_HEIGHT - 75],
                                        175,
                                        50,
                                        COLORS.get("yellow"),
                                        TEXT_SIZE.get("small"),
                                        hover_color=COLORS.get("light_yellow"),
                                        action=self.instructions_intro,
                                        text="ZPĚT DO MENU")
        self.instructions_buttons.append(instructions_intro_button)

        instructions_quit_button = Button(self.app,
                                   [(SCREEN_WIDTH / 2) + 75, (SCREEN_HEIGHT / 2) - 37.5],
                                   150,
                                   50,
                                   COLORS.get("red"),
                                   TEXT_SIZE.get("small"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.instructions_quit,
                                   text="KONEC")
        self.instructions_buttons.append(instructions_quit_button)

