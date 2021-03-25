from components.button import *
from components.text import *
from components.difficulty import *


class Instructions:
    def __init__(self, app):
        self.app = app
        self.instructions_buttons = []
        self.text_list = []
        self.difficulties = []
        self.snake_easy = pygame.image.load('imgs/difficulties/snake_easy_test.png')
        self.snake_medium = pygame.image.load('imgs/difficulties/snake_medium_test.png')
        self.snake_hard = pygame.image.load('imgs/difficulties/snake_hard_test.png')
        self.active_difficulty = "medium"


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
        for difficulty in self.difficulties:
            difficulty.update()

    def instructions_draw(self):
        # INSTRUCTIONS STATE DRAW
        for button in self.app.active_buttons:
            button.draw()
        for text in self.text_list:
            text.draw()
        """for difficulty in self.difficulties:
            difficulty.draw()"""
        if self.active_difficulty == "easy":
            self.difficulties[0].draw()
        elif self.active_difficulty == "medium":
            self.difficulties[1].draw()
        elif self.active_difficulty == "hard":
            self.difficulties[2].draw()
        else:
            pass

    def instructions_intro(self):
        # FROM INSTRUCTIONS STATE TO INTRO
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons

    def instructions_quit(self):
        # QUIT FROM INSTRUCTIONS STATE
        self.app.running = False

    def set_difficulty_easy(self):
        self.active_difficulty = "easy"

    def set_difficulty_medium(self):
        self.active_difficulty = "medium"

    def set_difficulty_hard(self):
        self.active_difficulty = "hard"

    def make_instructions_buttons(self):
        # MAKE INSTRUCTIONS BUTTONS
        instructions_intro_button = Button(self.app,
                                        [20, 805],
                                        225,
                                        50,
                                        COLORS.get("yellow"),
                                        TEXT_SIZE.get("small"),
                                        hover_color=COLORS.get("light_yellow"),
                                        action=self.instructions_intro,
                                        text="ZPĚT DO MENU")
        self.instructions_buttons.append(instructions_intro_button)

        instructions_quit_button = Button(self.app,
                                   [655, 805],
                                   125,
                                   50,
                                   COLORS.get("red"),
                                   TEXT_SIZE.get("small"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.instructions_quit,
                                   text="KONEC")
        self.instructions_buttons.append(instructions_quit_button)

        instructions_difficulty_easy_button = Button(self.app,
                                          [50, 650],
                                          225,
                                          60,
                                          COLORS.get("yellow"),
                                          TEXT_SIZE.get("small"),
                                          hover_color=COLORS.get("light_yellow"),
                                          action=self.set_difficulty_easy,
                                          text="MÍRUMILOVNÁ")
        self.instructions_buttons.append(instructions_difficulty_easy_button)

        instructions_difficulty_medium_button = Button(self.app,
                                                     [300, 650],
                                                     225,
                                                     60,
                                                     COLORS.get("orange"),
                                                     TEXT_SIZE.get("small"),
                                                     hover_color=COLORS.get("light_orange"),
                                                     action=self.set_difficulty_medium,
                                                     text="ZLATEJ STŘED")
        self.instructions_buttons.append(instructions_difficulty_medium_button)

        instructions_difficulty_hard_button = Button(self.app,
                                                     [550, 650],
                                                     225,
                                                     60,
                                                     COLORS.get("red"),
                                                     TEXT_SIZE.get("small"),
                                                     hover_color=COLORS.get("light_red"),
                                                     action=self.set_difficulty_hard,
                                                     text="PYTHONOVSKÁ")
        self.instructions_buttons.append(instructions_difficulty_hard_button)

    def make_instructions_texts(self):
        # MAKE INSTRUCTIONS TEXT
        head_txt = Text(self.app,
                        [240, 25],
                        TEXT_SIZE.get("xlarge"),
                        "Nastavení",
                        COLORS.get("light_yellow"))
        self.text_list.append(head_txt)

        controls_txt = Text(self.app,
                            [325, 125],
                            TEXT_SIZE.get("medium"),
                            "Ovládání",
                            COLORS.get("light_green"))
        self.text_list.append(controls_txt)

        player_1_txt = Text(self.app,
                            [325, 200],
                            TEXT_SIZE.get("small"),
                            "Hráč 1 - šipky",
                            COLORS.get("black"))
        self.text_list.append(player_1_txt)

        player_2_txt = Text(self.app,
                            [315, 250],
                            TEXT_SIZE.get("small"),
                            "Hráč 2 - WASD",
                            COLORS.get("black"))
        self.text_list.append(player_2_txt)

        pause_txt = Text(self.app,
                         [355, 300],
                         TEXT_SIZE.get("small"),
                         "Pauza - P",
                         COLORS.get("black"))
        self.text_list.append(pause_txt)

        back_to_menu_txt = Text(self.app,
                                     [310, 350],
                                     TEXT_SIZE.get("small"),
                                     "Zpět do menu - M",
                                     COLORS.get("black"))
        self.text_list.append(back_to_menu_txt)

        quit_txt = Text(self.app,
                        [350, 400],
                        TEXT_SIZE.get("small"),
                        "Konec - Q",
                        COLORS.get("black"))
        self.text_list.append(quit_txt)

        difficulty_txt = Text(self.app,
                        [260, 465],
                        TEXT_SIZE.get("medium"),
                        "Výběr obtížnosti",
                        COLORS.get("red"))
        self.text_list.append(difficulty_txt)

    def make_difficulty_snakes(self):
        easy = Difficulty(self.app,
                          [130, 550],
                          self.snake_easy)
        self.difficulties.append(easy)
        medium = Difficulty(self.app,
                            [380, 550],
                            self.snake_medium)
        self.difficulties.append(medium)
        hard = Difficulty(self.app,
                          [630, 550],
                          self.snake_hard)
        self.difficulties.append(hard)

    def check_fps(self):
        if self.app.instructions.active_difficulty == "easy":
            self.app.fps = 5
        elif self.app.instructions.active_difficulty == "medium":
            self.app.fps = 10
        elif self.app.instructions.active_difficulty == "hard":
            self.app.fps = 15
        else:
            pass
