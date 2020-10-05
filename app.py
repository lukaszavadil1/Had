import pygame
import sys
from settings import *
from button import *
from game_window import *
from snake import *

snake_2_head = pygame.image.load("imgs/snake_head_2.png")
apple_img = pygame.image.load("imgs/apple.png")
obstacle_img = pygame.image.load("imgs/obstacle.png")


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.icon = pygame.image.load("imgs/logo.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Had")
        self.state = "intro"
        self.play_buttons = []
        self.intro_buttons = []
        self.interlude_buttons = []
        self.active_buttons = self.intro_buttons
        self.make_buttons()
        self.game_window = GameWindow(self)
        self.snake = Snake(self)

    def run(self):
        # MAIN LOOP
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def make_buttons(self):

        # <--------------------------------------------INTRO BUTTONS--------------------------------------------------->

        intro_play_button = Button(self,
                                   [75, (SCREEN_HEIGHT/2)-37.5],
                                   150,
                                   75,
                                   COLORS.get("green"),
                                   BUTTON_TEXT_SIZE.get("normal"),
                                   hover_color=COLORS.get("light_green"),
                                   action=self.intro_play,
                                   text="HRÁT")
        self.intro_buttons.append(intro_play_button)

        intro_quit_button = Button(self,
                                   [(SCREEN_WIDTH / 2) + 75, (SCREEN_HEIGHT / 2) - 37.5],
                                   150,
                                   75,
                                   COLORS.get("red"),
                                   BUTTON_TEXT_SIZE.get("normal"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.intro_quit,
                                   text="KONEC")
        self.intro_buttons.append(intro_quit_button)

        # <--------------------------------------------PLAY BUTTONS---------------------------------------------------->

        play_quit_button = Button(self,
                                   [SCREEN_WIDTH - 90, 20],
                                   80,
                                   40,
                                   COLORS.get("red"),
                                   BUTTON_TEXT_SIZE.get("xsmall"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.play_quit,
                                   text="KONEC")
        self.play_buttons.append(play_quit_button)

        play_intro_button = Button(self,
                                  [10, 20],
                                  140,
                                  40,
                                  COLORS.get("yellow"),
                                  BUTTON_TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_yellow"),
                                  action=self.play_intro,
                                  text="ZPĚT DO MENU")
        self.play_buttons.append(play_intro_button)

        play_interlude_button = Button(self,
                                   [280, 20],
                                   80,
                                   40,
                                   COLORS.get("yellow"),
                                   BUTTON_TEXT_SIZE.get("xsmall"),
                                   hover_color=COLORS.get("light_yellow"),
                                   action=self.play_interlude,
                                   text="PAUZA")
        self.play_buttons.append(play_interlude_button)

        # <---------------------------------------INTERLUDE BUTTONS---------------------------------------------------->

        interlude_play_button = Button(self,
                                  [260, 20],
                                  140,
                                  40,
                                  COLORS.get("yellow"),
                                  BUTTON_TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_yellow"),
                                  action=self.interlude_play,
                                  text="ZPĚT DO HRY")
        self.interlude_buttons.append(interlude_play_button)

        interlude_intro_button = Button(self,
                                   [10, 20],
                                   140,
                                   40,
                                   COLORS.get("yellow"),
                                   BUTTON_TEXT_SIZE.get("xsmall"),
                                   hover_color=COLORS.get("light_yellow"),
                                   action=self.play_intro,
                                   text="ZPĚT DO MENU")
        self.interlude_buttons.append(interlude_intro_button)

        interlude_quit_button = Button(self,
                                  [510, 20],
                                  80,
                                  40,
                                  COLORS.get("red"),
                                  BUTTON_TEXT_SIZE.get("xsmall"),
                                  hover_color=COLORS.get("light_red"),
                                  action=self.play_quit,
                                  text="KONEC")
        self.interlude_buttons.append(interlude_quit_button)

        # <------------------------------------------------------------------------------------------------------------>

    def get_events(self):
        # EVENT SWITCH
        if self.state == "intro":
            self.intro_events()
        if self.state == "play":
            self.play_events()
        if self.state == "interlude":
            self.interlude_events()

    def update(self):
        # MAIN UPDATE
        if self.state == "intro":
            self.intro_update()
        if self.state == "play":
            self.play_update()
        if self.state == "interlude":
            self.interlude_update()

    def draw(self):
        # MAIN DRAW
        self.screen.fill(COLORS.get("bgcolor"))
        if self.state == "intro":
            self.intro_draw()
        if self.state == "play":
            self.play_draw()
        if self.state == "interlude":
            self.interlude_draw()
        pygame.display.update()

# <-------------------------------------------------------INTRO-------------------------------------------------------->

    def intro_events(self):
        # INTRO EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.intro_buttons:
                    if button.hovered:
                         button.click()
                    else:
                        pass

    def intro_update(self):
        # INTRO STATE UPDATE
        for button in self.active_buttons:
            button.update()

    def intro_draw(self):
        # INTRO STATE DRAW
        for button in self.active_buttons:
            button.draw()

    def intro_play(self):
        # FROM INTRO STATE TO PLAY
        self.state = "play"
        self.active_buttons = self.play_buttons

    def intro_quit(self):
        # QUIT FROM INTRO STATE
        self.running = False

# <-------------------------------------------------------PLAY--------------------------------------------------------->

    def play_events(self):
        # PLAY EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # BUTTON CLICK
                for button in self.play_buttons:
                    if button.hovered:
                         button.click()
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

    def play_update(self):
        # PLAY STATE UPDATE
        for button in self.active_buttons:
            button.update()
        self.game_window.update()

    def play_draw(self):
        # PLAY STATE DRAW
        self.game_window.draw()
        for button in self.active_buttons:
            button.draw()

    def play_quit(self):
        # QUIT FROM PLAY STATE
        self.running = False

    def play_intro(self):
        # FROM PLAY STATE TO INTRO
        self.state = "intro"
        self.active_buttons = self.intro_buttons

    def play_interlude(self):
        # FROM PLAY STATE TO INTERLUDE
        self.state = "interlude"
        self.active_buttons = self.interlude_buttons

# <---------------------------------------------------INTERLUDE-------------------------------------------------------->

    def interlude_events(self):
        # PLAY EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # BUTTON CLICK
                for button in self.interlude_buttons:
                    if button.hovered:
                         button.click()
                    else:
                        pass

    def interlude_update(self):
        self.snake.vel = [0, 0]
        # PLAY STATE UPDATE
        for button in self.active_buttons:
            button.update()
        self.game_window.update()

    def interlude_draw(self):
        # PLAY STATE DRAW
        self.game_window.draw()
        for button in self.active_buttons:
            button.draw()

    def interlude_quit(self):
        # QUIT FROM INTERLUDE STATE
        self.running = False

    def interlude_intro(self):
        # FROM INTERLUDE STATE TO INTRO
        self.state = "intro"
        self.active_buttons = self.intro_buttons

    def interlude_play(self):
        # FROM INTERLUDE STATE TO PLAY
        self.state = "play"
        self.active_buttons = self.play_buttons
