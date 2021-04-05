from components.button import *


class GameModes:
    def __init__(self, app):
        self.game_modes_buttons = []
        self.app = app

    def game_modes_events(self):
        # GAME MODES EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.game_modes_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass

    def game_modes_update(self):
        # INTRO STATE UPDATE
        for button in self.app.active_buttons:
            button.update()

    def game_modes_draw(self):
        # INTRO STATE DRAW
        for button in self.app.active_buttons:
            button.draw()

    def game_modes_casual(self):
        # CASUAL MODE
        self.app.apples_amount = 1
        self.app.make_apples()
        self.app.mode = "casual"
        self.app.state = "interlude"

    def game_modes_competitive(self):
        # COMPETITIVE MODE
        self.app.apples_amount = 1
        self.app.make_apples()
        self.app.mode = "competitive"
        self.app.state = "interlude"

    def game_modes_apples(self):
        self.app.apples_amount = 200
        self.app.make_apples()
        self.app.mode = "apples"
        self.app.state = "interlude"

    def game_modes_obstacles(self):
        self.app.apples_amount = 1
        self.app.make_apples()
        self.app.make_obstacles()
        self.app.mode = "obstacles"
        self.app.state = "interlude"

    def game_modes_intro(self):
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons

    def game_modes_quit(self):
        # QUIT FROM INTRO STATE
        self.app.running = False

    def make_game_modes_buttons(self):
        # MAKE INTRO BUTTONS
        game_modes_casual_button = Button(self.app,
                                        [300, 75],
                                        200,
                                        75,
                                        COLORS.get("dark_green"),
                                        TEXT_SIZE.get("medium"),
                                        hover_color=COLORS.get("green"),
                                        action=self.game_modes_casual,
                                        text="KLASIKA")
        self.game_modes_buttons.append(game_modes_casual_button)

        game_modes_competitive_button = Button(self.app,
                                        [300, 200],
                                        200,
                                        75,
                                        COLORS.get("purple"),
                                        TEXT_SIZE.get("medium"),
                                        hover_color=COLORS.get("light_purple"),
                                        action=self.game_modes_competitive,
                                        text="KOMPOT")
        self.game_modes_buttons.append(game_modes_competitive_button)

        game_modes_apples_button = Button(self.app,
                                               [300, 325],
                                               200,
                                               75,
                                               COLORS.get("red"),
                                               TEXT_SIZE.get("medium"),
                                               hover_color=COLORS.get("light_red"),
                                               action=self.game_modes_apples,
                                               text="JABKA")
        self.game_modes_buttons.append(game_modes_apples_button)

        game_modes_obstacles_button = Button(self.app,
                                               [300, 450],
                                               200,
                                               75,
                                               COLORS.get("orange"),
                                               TEXT_SIZE.get("medium"),
                                               hover_color=COLORS.get("light_orange"),
                                               action=self.game_modes_obstacles,
                                               text="KLÁDY")
        self.game_modes_buttons.append(game_modes_obstacles_button)

        game_modes_intro_button = Button(self.app,
                                        [20, 805],
                                        225,
                                        50,
                                        COLORS.get("yellow"),
                                        TEXT_SIZE.get("small"),
                                        hover_color=COLORS.get("light_yellow"),
                                        action=self.game_modes_intro,
                                        text="ZPĚT DO MENU")
        self.game_modes_buttons.append(game_modes_intro_button)
        game_modes_quit_button = Button(self.app,
                                   [655, 805],
                                   125,
                                   50,
                                   COLORS.get("red"),
                                   TEXT_SIZE.get("small"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.game_modes_quit,
                                   text="KONEC")
        self.game_modes_buttons.append(game_modes_quit_button)
