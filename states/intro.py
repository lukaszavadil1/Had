from components.button import *


class Intro:
    def __init__(self, app):
        self.intro_buttons = []
        self.app = app

    def intro_events(self):
        # INTRO EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.intro_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass

    def intro_update(self):
        # INTRO STATE UPDATE
        for button in self.app.active_buttons:
            button.update()

    def intro_draw(self):
        # INTRO STATE DRAW
        for button in self.app.active_buttons:
            button.draw()

    def intro_game_modes_p1(self):
        # FROM INTRO STATE TO PLAY
        self.app.snake.reset()
        self.app.snake_2.reset()
        self.app.mp_disable = True
        self.app.state = "game_modes"
        self.app.active_buttons = self.app.game_modes.game_modes_buttons

    def intro_game_modes_p2(self):
        # FROM INTRO STATE TO PLAY
        self.app.snake.reset()
        self.app.snake_2.reset()
        self.app.mp_disable = False
        self.app.state = "game_modes"
        self.app.active_buttons = self.app.game_modes.game_modes_buttons

    def intro_high_scores(self):
        self.app.state = "high_scores"
        self.app.active_buttons = self.app.high_scores.high_scores_buttons

    def intro_instructions(self):
        self.app.state = "instructions"
        self.app.active_buttons = self.app.instructions.instructions_buttons

    def intro_quit(self):
        # QUIT FROM INTRO STATE
        self.app.running = False

    def make_intro_buttons(self):
        # MAKE INTRO BUTTONS
        intro_game_modes_p1_button = Button(self.app,
                                        [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 225],
                                        200,
                                        75,
                                        COLORS.get("dark_green"),
                                        TEXT_SIZE.get("normal"),
                                        hover_color=COLORS.get("green"),
                                        action=self.intro_game_modes_p1,
                                        text="1 HRÁČ")
        self.intro_buttons.append(intro_game_modes_p1_button)

        intro_game_modes_p2_button = Button(self.app,
                                        [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 100],
                                        200,
                                        75,
                                        COLORS.get("purple"),
                                        TEXT_SIZE.get("normal"),
                                        hover_color=COLORS.get("light_purple"),
                                        action=self.intro_game_modes_p2,
                                        text="2 HRÁČI")
        self.intro_buttons.append(intro_game_modes_p2_button)

        intro_high_scores_button = Button(self.app,
                                           [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 25],
                                           200,
                                           75,
                                           COLORS.get("blue"),
                                           TEXT_SIZE.get("normal"),
                                           hover_color=COLORS.get("light_blue"),
                                           action=self.intro_high_scores,
                                           text="TABULKA")
        self.intro_buttons.append(intro_high_scores_button)

        intro_instructions_button = Button(self.app,
                                           [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 150],
                                           200,
                                           75,
                                           COLORS.get("yellow"),
                                           TEXT_SIZE.get("normal"),
                                           hover_color=COLORS.get("light_yellow"),
                                           action=self.intro_instructions,
                                           text="NASTAVENÍ")
        self.intro_buttons.append(intro_instructions_button)

        intro_quit_button = Button(self.app,
                                   [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 275],
                                   200,
                                   75,
                                   COLORS.get("red"),
                                   TEXT_SIZE.get("normal"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.intro_quit,
                                   text="KONEC")
        self.intro_buttons.append(intro_quit_button)
