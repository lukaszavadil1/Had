import sys
from game_window import *
from entities.snake import *
from entities.apple import *
from entities.obstacle import *
from states import play, intro, state_machine, pause, interlude, instructions, end_game, game_modes, high_scores


class App:
    def __init__(self):
        # ESSENTIALS
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, (CELL_NUMBER * CELL_SIZE)+75))
        self.running = True
        self.fps = FPS
        self.game_window = GameWindow(self)
        self.mode = None
        self.score = 0
        self.scores = []
        self.player_name = ""
        self.player_names = []
        self.player_scores = []
        # ICON
        self.icon = pygame.image.load("imgs/players/player_1.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Had")
        # ENTITIES
        self.snakes_start_pos = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10), Vector2(3, 10), Vector2(6, 5), Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.snake = Snake(self, [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)], Vector2(0, 0), False, "green")
        self.snake_2 = Snake(self, [Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)], Vector2(0, 0), False, "purple")
        self.apples_amount = 1
        self.apples = []
        self.make_apples()
        self.obstacles_amount = 10
        self.obstacles = []
        self.mp_disable = True
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
        self.high_scores = high_scores.HighScores(self)
        # COMPONENTS
        self.active_buttons = self.intro.intro_buttons
        self.make_buttons()
        self.make_texts()
        self.make_difficulty()
        self.make_input_boxes()
        self.get_scores()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    # MAIN LOOP
    def run(self):
        while self.running:
            self.state_machine.get_events()
            self.state_machine.update()
            self.state_machine.draw()
            self.clock.tick(self.fps)
            print(self.snake.body)
        quit()

    # MAKE METHODS
    def make_buttons(self):
        # MAKE BUTTONS
        self.intro.make_intro_buttons()
        self.play.make_play_buttons()
        self.pause.make_pause_buttons()
        self.instructions.make_instructions_buttons()
        self.end_game.make_end_game_buttons()
        self.game_modes.make_game_modes_buttons()
        self.high_scores.make_high_scores_buttons()

    def make_texts(self):
        self.instructions.make_instructions_texts()
        self.end_game.make_end_game_texts()
        self.high_scores.make_high_scores_texts()

    def make_difficulty(self):
        self.instructions.make_difficulty_snakes()

    def make_input_boxes(self):
        self.end_game.make_input_box()

    def make_apples(self):
        self.apples = []
        for num in range(self.apples_amount):
            apple = Apple(self, random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
            for a in self.apples:
                for obst in self.obstacles:
                    if a.pos == apple.pos or apple.pos in self.snakes_start_pos or apple.pos == obst.pos:
                        apple = Apple(self, random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
                    else:
                        pass
            self.apples.append(apple)

    def make_obstacles(self):
        self.obstacles = []
        for num in range(self.obstacles_amount):
            obstacle = Obstacle(self, random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
            for obst in self.obstacles:
                for apple in self.apples:
                    if obst.pos == obstacle.pos or obstacle.pos in self.snakes_start_pos or obstacle.pos == apple.pos:
                        obstacle = Obstacle(self, random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
                    else:
                        pass
            self.obstacles.append(obstacle)

    # SHORTCUTS
    def death(self):
        self.state = "end_game"
        self.active_buttons = self.end_game.end_game_buttons
        self.fps = FPS
        self.obstacles = []
        self.apples = []

    def back_to_menu(self):
        self.state = "intro"
        self.active_buttons = self.intro.intro_buttons
        self.fps = FPS
        self.score = 0
        self.obstacles = []
        self.apples = []

    # SCORE MANAGEMENT
    def get_scores(self):
        with open(SCORES_FILE, "r") as f:
            try:
                for line in f:
                    self.player_names.append(line.split(None, 1)[0])
                    self.scores.append(line.split()[1])
            except:
                pass
            self.players_scores = list(map(list, zip(self.player_names, self.scores)))
        for index, score in enumerate(self.scores):
            self.scores[index] = int(self.scores[index])

    def check_scores(self):
        if len(self.scores) <= 10:
            self.new_high_score()
        else:
            for score in self.scores:
                if self.score > score:
                    self.new_high_score()
                    return True

    def new_high_score(self):
        def func(score):
            return score[1]
        self.scores.append(self.score)
        self.player_names.append(self.player_name)
        self.players_scores = list(map(list, zip(self.player_names, self.scores)))
        self.players_scores.sort(reverse=True, key=func)
        self.set_scores()

    def set_scores(self):
        with open(SCORES_FILE, "w") as f:
            for player, score in self.players_scores:
                f.write(str(player) + " " + str(score) + "\n")
