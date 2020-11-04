from button import *
from settings import *
from pygame.math import Vector2


class Pause:
    def __init__(self, app):
        self.pause_buttons = []
        self.app = app

    def pause_events(self):
        # PAUSE EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # BUTTON CLICK
                for button in self.pause_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.app.running = False
                if event.key == pygame.K_m:
                    self.app.state = "intro"
                    self.app.active_buttons = self.app.intro.intro_buttons
                if event.key == pygame.K_p:
                    self.app.state = "interlude"

    def pause_update(self):
        # PAUSE STATE UPDATE
        self.app.snake.direction = Vector2(0, 0)
        for button in self.app.active_buttons:
            button.update()
        self.app.game_window.update()

    def pause_draw(self):
        # PAUSE STATE DRAW
        self.app.game_window.draw()
        for button in self.app.active_buttons:
            button.draw()

    def pause_quit(self):
        # QUIT FROM PAUSE STATE
        self.app.running = False

    def pause_intro(self):
        # FROM PAUSE STATE TO INTRO
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons

    def pause_interlude(self):
        # FROM PAUSE STATE TO PLAY
        self.app.state = "interlude"

    def make_pause_buttons(self):
        # MAKE PAUSE BUTTONS
        pause_interlude_button = Button(self.app,
                                        [335, 820],
                                        165,
                                        40,
                                        COLORS.get("yellow"),
                                        TEXT_SIZE.get("xsmall"),
                                        hover_color=COLORS.get("light_yellow"),
                                        action=self.pause_interlude,
                                        text="ZPĚT DO HRY (P)")
        self.pause_buttons.append(pause_interlude_button)

        pause_intro_button = Button(self.app,
                                    [10, 820],
                                    175,
                                    40,
                                    COLORS.get("yellow"),
                                    TEXT_SIZE.get("xsmall"),
                                    hover_color=COLORS.get("light_yellow"),
                                    action=self.pause_intro,
                                    text="ZPĚT DO MENU (M)")
        self.pause_buttons.append(pause_intro_button)

        pause_quit_button = Button(self.app,
                                    [680, 820],
                                    105,
                                    40,
                                    COLORS.get("red"),
                                    TEXT_SIZE.get("xsmall"),
                                    hover_color=COLORS.get("light_red"),
                                    action=self.pause_quit,
                                    text="KONEC (Q)")
        self.pause_buttons.append(pause_quit_button)