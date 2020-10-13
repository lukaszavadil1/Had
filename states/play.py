import pygame
from settings import *
from button import *


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
                        button.Button.click()
                    else:
                        pass
            if event.type == pygame.KEYDOWN:  # ON KEY DOWN
                # BASIC MOVEMENT
                if event.key == pygame.K_LEFT:
                    self.snake.vel = [-BLOCK_SIZE, 0]
                    self.snake.angle = "left"
                elif event.key == pygame.K_RIGHT:
                    self.snake.vel = [BLOCK_SIZE, 0]
                    self.snake.angle = "right"
                elif event.key == pygame.K_DOWN:
                    self.snake.vel = [0, BLOCK_SIZE]
                    self.snake.angle = "down"
                elif event.key == pygame.K_UP:
                    self.snake.vel = [0, -BLOCK_SIZE]
                    self.snake.angle = "up"
                else:
                    pass
                # KEY SHORTCUTS
                if event.key == pygame.K_q:
                    self.app.running = False
                if event.key == pygame.K_p:
                    self.app.state = "pause"
                    self.app.active_buttons = self.app.pause.pause_buttons
                if event.key == pygame.K_m:
                    self.app.state = "intro"
                    self.app.active_buttons = self.app.intro.intro_buttons

    def play_update(self):
        # PLAY STATE UPDATE
        for button in self.app.active_buttons:
            button.update()
        self.app.game_window.update()

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

    def play_pause(self):
        # FROM PLAY STATE TO PAUSE
        self.app.state = "pause"
        self.app.active_buttons = self.app.pause.pause_buttons

    def make_play_buttons(self):
        # MAKE PLAY BUTTONS
        play_quit_button = Button(self.app,
                                  [480, 20],
                                  110,
                                  40,
                                  COLORS.get("red"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_red"),
                                  action=self.play_quit,
                                  text="KONEC (Q)")
        self.play_buttons.append(play_quit_button)

        play_intro_button = Button(self.app,
                                  [10, 20],
                                  190,
                                  40,
                                  COLORS.get("yellow"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_yellow"),
                                  action=self.play_intro,
                                  text="ZPĚT DO MENU (M)")
        self.play_buttons.append(play_intro_button)

        play_pause_button = Button(self.app,
                                  [260, 20],
                                  110,
                                  40,
                                  COLORS.get("yellow"),
                                  TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_yellow"),
                                  action=self.play_pause,
                                  text="PAUZA (P)")
        self.play_buttons.append(play_pause_button)