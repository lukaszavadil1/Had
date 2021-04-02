from components.button import *
from components.text import *
from components.input_box import *


class EndGame:
    def __init__(self, app):
        self.app = app
        self.end_game_buttons = []
        self.text_list = []
        self.inputs = []

    def end_game_events(self):
        # GAME OVER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.end_game_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass
            if self.app.mode == "competitive" and self.app.mp_disable:
                for inp in self.inputs:
                    inp.handle_event(event)

    def end_game_update(self):
        # GAME OVER STATE UPDATE
        for text in self.text_list:
            text.update()
        for button in self.app.active_buttons:
            button.update()
        if self.app.mode == "competitive" and self.app.mp_disable:
            for inp in self.inputs:
                inp.update()

    def end_game_draw(self):
        # GAME OVER STATE DRAW
        for text in self.text_list:
            text.draw()
        for button in self.app.active_buttons:
            button.draw()
        if self.app.mode == "competitive" and self.app.mp_disable:
            for inp in self.inputs:
                inp.draw()

    def end_game_intro(self):
        # FROM GAME OVER STATE TO INTRO
        # self.app.snake.reset()
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons

    def end_game_quit(self):
        # QUIT FROM GAME OVER STATE
        self.app.running = False

    def make_input_box(self):
        input_box = InputBox(self.app,
                             170,
                             500,
                             140,
                             32)
        self.inputs.append(input_box)

    def make_end_game_buttons(self):
        end_game_quit_button = Button(self.app,
                                       [500, 400],
                                       130,
                                       60,
                                       COLORS.get("red"),
                                       TEXT_SIZE.get("normal"),
                                       hover_color=COLORS.get("light_red"),
                                       action=self.end_game_quit,
                                       text="KONEC")
        self.end_game_buttons.append(end_game_quit_button)

        end_game_intro_button = Button(self.app,
                                        [170, 400],
                                        275,
                                        60,
                                        COLORS.get("yellow"),
                                        TEXT_SIZE.get("normal"),
                                        hover_color=COLORS.get("light_yellow"),
                                        action=self.end_game_intro,
                                        text="ZPĚT DO MENU")
        self.end_game_buttons.append(end_game_intro_button)

    def make_end_game_texts(self):
        test_text = Text(self.app,
                         [155, 250],
                         TEXT_SIZE.get("xxlarge"),
                         "KONEC HRY!",
                         COLORS.get("red"))
        self.text_list.append(test_text)
