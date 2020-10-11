import sys
from game_window import *
from snake import *
from state_machine import *
from intro import *
from play import *
from pause import *
from interlude import *
from instructions import *

snake_2_head = pygame.image.load("imgs/snake_head_2.png")
apple_img = pygame.image.load("imgs/apple.png")
obstacle_img = pygame.image.load("imgs/obstacle.png")


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.state = "intro"
        self.state_machine = StateMachine(self)
        self.icon = pygame.image.load("imgs/logo.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Had")
        self.game_window = GameWindow(self)
        self.snake = Snake(self)
        self.intro = Intro(self)
        self.interlude = Interlude(self)
        self.play = Play(self)
        self.pause = Pause(self)
        self.instructions = Instructions(self)
        self.active_buttons = self.intro.intro_buttons
        self.make_buttons()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    def run(self):
        # MAIN LOOP
        while self.running:
            self.state_machine.get_events()
            self.state_machine.update()
            self.state_machine.draw()
            self.clock.tick(FPS)
        quit()

    def make_buttons(self):
        # MAKE BUTTONS
        self.intro.make_intro_buttons()
        self.play.make_play_buttons()
        self.pause.make_pause_buttons()
        self.instructions.make_instructions_buttons()


