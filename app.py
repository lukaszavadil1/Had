import sys
from game_window import *
from entities.snake import *
from entities.apple import *
from states import play, intro, state_machine, pause, interlude, instructions, end_game, game_modes


class App:
    def __init__(self):
        # ESSENTIALS
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, (CELL_NUMBER * CELL_SIZE)+75))
        self.running = True
        self.fps = FPS
        self.game_window = GameWindow(self)
        # ICON
        self.icon = pygame.image.load("imgs/logo.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Had")
        # ENTITIES
        self.snakes_start_pos = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10), Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.snake = Snake(self, [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)], Vector2(0, 0), False, "green")
        self.snake_2 = Snake(self, [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)], Vector2(0, 0), False, "purple")
        self.apples_amount = 1
        self.apples = []
        self.make_apples()
        # STATES
        self.state = "intro"
        self.state_machine = state_machine.StateMachine(self)
        self.intro = intro.Intro(self)
        self.interlude = interlude.Interlude(self)
        self.play = play.Play(self)
        self.pause = pause.Pause(self)
        self.instructions = instructions.Instructions(self)
        self.end_game = end_game.EndGame(self)
        self.game_modes = game_modes.GameModes(self)
        self.mode = None
        # COMPONENTS
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
            print(self.mode)
        quit()

    def make_buttons(self):
        # MAKE BUTTONS
        self.intro.make_intro_buttons()
        self.play.make_play_buttons()
        self.pause.make_pause_buttons()
        self.instructions.make_instructions_buttons()
        self.end_game.make_end_game_buttons()
        self.game_modes.make_game_modes_buttons()

    def make_texts(self):
        self.instructions.make_instructions_texts()
        self.end_game.make_end_game_texts()

    def make_difficulty(self):
        self.instructions.make_difficulty_snakes()

    def make_apples(self):
        self.apples = []
        for num in range(self.apples_amount):
            apple = Apple(self, random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
            for a in self.apples:
                if a.pos == apple.pos or apple.pos in self.snakes_start_pos:
                    apple = Apple(self, random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
                else:
                    pass
            self.apples.append(apple)


