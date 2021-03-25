from components.button import *
from pygame.math import Vector2
from entities.obstacle import *


class Play:
    def __init__(self, app):
        self.play_buttons = []
        self.app = app
        self.snake = self.app.snake

    def play_events(self):
        # PLAY EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # BUTTON CLICK
                for button in self.play_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass
            if event.type == pygame.KEYDOWN:  # ON KEY DOWN
                # BASIC MOVEMENT
                # SNAKE 1
                if event.key == pygame.K_UP:
                    if self.app.snake.direction.y != 1:
                        self.app.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT:
                    if self.app.snake.direction.x != -1:
                        self.app.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if self.app.snake.direction.y != -1:
                        self.app.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if self.app.snake.direction.x != 1:
                        self.app.snake.direction = Vector2(-1, 0)
                # SNAKE 2
                if event.key == pygame.K_w:
                    if self.app.snake_2.direction.y != 1:
                        self.app.snake_2.direction = Vector2(0, -1)
                if event.key == pygame.K_d:
                    if self.app.snake_2.direction.x != -1:
                        self.app.snake_2.direction = Vector2(1, 0)
                if event.key == pygame.K_s:
                    if self.app.snake_2.direction.y != -1:
                        self.app.snake_2.direction = Vector2(0, 1)
                if event.key == pygame.K_a:
                    if self.app.snake_2.direction.x != 1:
                        self.app.snake_2.direction = Vector2(-1, 0)
                # KEY SHORTCUTS
                if event.key == pygame.K_q:
                    self.app.running = False
                if event.key == pygame.K_p:
                    self.app.state = "pause"
                    self.app.active_buttons = self.app.pause.pause_buttons
                    self.app.fps = FPS
                if event.key == pygame.K_m:
                    self.app.state = "intro"
                    self.app.active_buttons = self.app.intro.intro_buttons
                    self.app.fps = FPS

    def play_update(self):
        # PLAY STATE UPDATE
        for button in self.app.active_buttons:
            button.update()
        self.app.game_window.update()
        if self.app.mode == "competitive":
            self.friendly_fire()

    def play_draw(self):
        # PLAY STATE DRAW
        self.app.game_window.draw()
        for button in self.app.active_buttons:
            button.draw()

    def play_quit(self):
        # QUIT FROM PLAY STATE
        self.app.running = False

    def play_intro(self):
        # FROM PLAY STATE TO INTRO
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons
        self.app.fps = FPS

    def play_pause(self):
        # FROM PLAY STATE TO PAUSE
        self.app.state = "pause"
        self.app.active_buttons = self.app.pause.pause_buttons
        self.app.fps = FPS

    def make_play_buttons(self):
        # MAKE PLAY BUTTONS
        play_quit_button = Button(self.app,
                                  [680, 820],
                                  110,
                                  40,
                                  COLORS.get("red"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_red"),
                                  action=self.play_quit,
                                  text="KONEC (Q)")
        self.play_buttons.append(play_quit_button)

        play_intro_button = Button(self.app,
                                  [10, 820],
                                  190,
                                  40,
                                  COLORS.get("yellow"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_yellow"),
                                  action=self.play_intro,
                                  text="ZPĚT DO MENU (M)")
        self.play_buttons.append(play_intro_button)

        play_pause_button = Button(self.app,
                                  [380, 820],
                                  110,
                                  40,
                                  COLORS.get("yellow"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_yellow"),
                                  action=self.play_pause,
                                  text="PAUZA (P)")
        self.play_buttons.append(play_pause_button)

    def friendly_fire(self):
        for part in self.app.snake.body:
            for block in self.app.snake_2.body:
                if part == block:
                    self.app.death()
                else:
                    pass

