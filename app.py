import pygame
import sys
from settings import *
from button import *

snake_1_head = pygame.image.load("imgs/snake_head.png")
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
        self.active_buttons = self.intro_buttons
        self.make_buttons()

    def run(self):
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
                                   [(SCREEN_WIDTH / 2) - 75, 20],
                                   100,
                                   50,
                                   COLORS.get("red"),
                                   BUTTON_TEXT_SIZE.get("small"),
                                   hover_color=COLORS.get("light_red"),
                                   action=self.play_quit,
                                   text="KONEC")
        self.play_buttons.append(play_quit_button)

    def get_events(self):
        if self.state == "intro":
            self.intro_events()
        if self.state == "play":
            self.play_events()

    def update(self):
        if self.state == "intro":
            self.intro_update()
        if self.state == "play":
            self.play_update()

    def draw(self):
        self.screen.fill(COLORS.get("bgcolor"))
        if self.state == "intro":
            self.intro_draw()
        if self.state == "play":
            self.play_draw()
        pygame.display.update()

# <-------------------------------------------------------INTRO-------------------------------------------------------->

    def intro_events(self):
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
        for button in self.active_buttons:
            button.update()

    def intro_draw(self):
        for button in self.active_buttons:
            button.draw()

    def intro_play(self):
        self.state = "play"
        self.active_buttons = self.play_buttons

    def intro_quit(self):
        self.running = False

# <-------------------------------------------------------PLAY--------------------------------------------------------->

    def play_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.play_buttons:
                    if button.hovered:
                         button.click()
                    else:
                        pass

    def play_update(self):
        for button in self.active_buttons:
            button.update()

    def play_draw(self):
        for button in self.active_buttons:
            button.draw()

    def play_quit(self):
        self.running = False
