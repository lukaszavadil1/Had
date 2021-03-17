import sys
from game_window import *
from entities.snake import *
from entities.apple import *
from states import play, intro, state_machine, pause, interlude, instructions, end_game


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, (CELL_NUMBER * CELL_SIZE)+75))
        self.running = True
        self.fps = FPS
        self.state = "intro"
        self.state_machine = state_machine.StateMachine(self)
        self.icon = pygame.image.load("imgs/logo.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Had")
        self.game_window = GameWindow(self)
        self.snake = Snake(self, [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)], Vector2(0, 0), False, "green")
        self.snake_2 = Snake(self, [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)], Vector2(0, 0), False, "purple")
        self.apple = Apple(self)
        self.intro = intro.Intro(self)
        self.interlude = interlude.Interlude(self)
        self.play = play.Play(self)
        self.pause = pause.Pause(self)
        self.instructions = instructions.Instructions(self)
        self.end_game = end_game.EndGame(self)
        self.active_buttons = self.intro.intro_buttons
        self.make_buttons()
        self.make_texts()
        self.make_difficulty()

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
            self.clock.tick(self.fps)
            print(self.fps)
            print(self.instructions.active_difficulty)
        quit()

    def make_buttons(self):
        # MAKE BUTTONS
        self.intro.make_intro_buttons()
        self.play.make_play_buttons()
        self.pause.make_pause_buttons()
        self.instructions.make_instructions_buttons()
        self.end_game.make_end_game_buttons()

    def make_texts(self):
        self.instructions.make_instructions_texts()
        self.end_game.make_end_game_texts()

    def make_difficulty(self):
        self.instructions.make_difficulty_snakes()
