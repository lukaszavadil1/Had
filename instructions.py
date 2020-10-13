import pygame
from settings import *
from button import *
from text import *


class Instructions:
    def __init__(self, app):
        self.instructions_buttons = []
        self.app = app
        self.text_list = []

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
        for text in self.text_list:
            text.update()

    def instructions_draw(self):
        # INSTRUCTIONS STATE DRAW
        for button in self.app.active_buttons:
            button.draw()
        for text in self.text_list:
            text.draw()

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
                                        [25, 525],
                                        225,
                                        50,
                                        COLORS.get("yellow"),
                                        TEXT_SIZE.get("small"),
                                        hover_color=COLORS.get("light_yellow"),
                                        action=self.instructions_intro,
                                        text="ZPĚT DO MENU")
        self.instructions_buttons.append(instructions_intro_button)

        instructions_quit_button = Button(self.app,
                                   [450, 525],
                                   125,
                                   50,
                                   COLORS.get("red"),
                                   TEXT_SIZE.get("small"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.instructions_quit,
                                   text="KONEC")
        self.instructions_buttons.append(instructions_quit_button)

    def make_instructions_texts(self):
        # MAKE INSTRUCTIONS TEXT
        head_txt = Text(self.app,
                        [140, 25],
                        TEXT_SIZE.get("xlarge"),
                        "Nastavení",
                        COLORS.get("yellow"))
        self.text_list.append(head_txt)
        controls_txt = Text(self.app,
                            [225, 125],
                            TEXT_SIZE.get("medium"),
                            "Ovládání",
                            COLORS.get("green"))
        self.text_list.append(controls_txt)
        player_1_txt = Text(self.app,
                            [215, 200],
                            TEXT_SIZE.get("small"),
                            "Hráč 1 - šipky",
                            COLORS.get("black"))
        self.text_list.append(player_1_txt)
        pause_txt = Text(self.app,
                         [250, 250],
                         TEXT_SIZE.get("small"),
                         "Pauza - P",
                         COLORS.get("black"))
        self.text_list.append(pause_txt)
        back_to_menu_txt = Text(self.app,
                                     [200, 300],
                                     TEXT_SIZE.get("small"),
                                     "Zpět do menu - M",
                                     COLORS.get("black"))
        self.text_list.append(back_to_menu_txt)
        quit_txt = Text(self.app,
                        [250, 350],
                        TEXT_SIZE.get("small"),
                        "Konec - Q",
                        COLORS.get("black"))
        self.text_list.append(quit_txt)