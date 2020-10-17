from button import *
from text import *


class GameOver:
    def __init__(self, app):
        self.app = app
        self.game_over_buttons = []
        self.text_list = []

    def game_over_events(self):
        # GAME OVER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.app.running = False
                if event.key == pygame.K_m:
                    self.app.state = "intro"
                    self.app.active_buttons = self.app.intro.intro_buttons

    def game_over_update(self):
        # GAME OVER STATE UPDATE
        for text in self.text_list:
            text.update()
        for button in self.app.active_buttons:
            button.update()

    def game_over_draw(self):
        # GAME OVER STATE DRAW
        for text in self.text_list:
            text.draw()
        for button in self.app.active_buttons:
            button.draw()

    def game_over_intro(self):
        # FROM GAME OVER STATE TO INTRO
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.play_buttons

    def game_over_quit(self):
        # QUIT FROM GAME OVER STATE
        self.app.running = False

    def make_game_over_buttons(self):
        game_over_quit_button = Button(self.app,
                                  [480, 20],
                                  110,
                                  40,
                                  COLORS.get("red"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_red"),
                                  action=self.game_over_quit,
                                  text="KONEC (Q)")
        self.game_over_buttons.append(game_over_quit_button)

        game_over_intro_button = Button(self.app,
                                   [10, 20],
                                   190,
                                   40,
                                   COLORS.get("yellow"),
                                   TEXT_SIZE.get("xsmall"),
                                   hover_color=COLORS.get("light_yellow"),
                                   action=self.game_over_intro,
                                   text="ZPĚT DO MENU (M)")
        self.game_over_buttons.append(game_over_intro_button)

    def make_game_over_texts(self):
        test_text = Text(self.app,
                           [300, 150],
                           TEXT_SIZE.get("medium"),
                           "Pes")
        self.text_list.append(test_text)
