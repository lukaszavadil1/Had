from entities.apple import *


class Snake:
    def __init__(self, app, body, direction, new_block, color):
        self.app = app
        self.body = body
        self.start_pos = self.body
        self.direction = direction
        self.new_block = new_block
        self.color = color
        self.mp_disable = True

        # SNAKE 1
        if self.color == "green":
            self.head_up = pygame.image.load('imgs/snake_1/head_up.png').convert_alpha()
            self.head_down = pygame.image.load('imgs/snake_1/head_down.png').convert_alpha()
            self.head_right = pygame.image.load('imgs/snake_1/head_right.png').convert_alpha()
            self.head_left = pygame.image.load('imgs/snake_1/head_left.png').convert_alpha()
            self.tail_up = pygame.image.load('imgs/snake_1/tail_up.png').convert_alpha()
            self.tail_down = pygame.image.load('imgs/snake_1/tail_down.png').convert_alpha()
            self.tail_right = pygame.image.load('imgs/snake_1/tail_right.png').convert_alpha()
            self.tail_left = pygame.image.load('imgs/snake_1/tail_left.png').convert_alpha()
            self.body_vertical = pygame.image.load('imgs/snake_1/body_vertical.png').convert_alpha()
            self.body_horizontal = pygame.image.load('imgs/snake_1/body_horizontal.png').convert_alpha()
            self.body_tr = pygame.image.load('imgs/snake_1/body_tr.png').convert_alpha()
            self.body_tl = pygame.image.load('imgs/snake_1/body_tl.png').convert_alpha()
            self.body_br = pygame.image.load('imgs/snake_1/body_br.png').convert_alpha()
            self.body_bl = pygame.image.load('imgs/snake_1/body_bl.png').convert_alpha()
        # SNAKE 2
        else:
            self.head_up = pygame.image.load('imgs/snake_2/head_up_2.png').convert_alpha()
            self.head_down = pygame.image.load('imgs/snake_2/head_down_2.png').convert_alpha()
            self.head_right = pygame.image.load('imgs/snake_2/head_right_2.png').convert_alpha()
            self.head_left = pygame.image.load('imgs/snake_2/head_left_2.png').convert_alpha()
            self.tail_up = pygame.image.load('imgs/snake_2/tail_up_2.png').convert_alpha()
            self.tail_down = pygame.image.load('imgs/snake_2/tail_down_2.png').convert_alpha()
            self.tail_right = pygame.image.load('imgs/snake_2/tail_right_2.png').convert_alpha()
            self.tail_left = pygame.image.load('imgs/snake_2/tail_left_2.png').convert_alpha()
            self.body_vertical = pygame.image.load('imgs/snake_2/body_vertical_2.png').convert_alpha()
            self.body_horizontal = pygame.image.load('imgs/snake_2/body_horizontal_2.png').convert_alpha()
            self.body_tr = pygame.image.load('imgs/snake_2/body_tr_2.png').convert_alpha()
            self.body_tl = pygame.image.load('imgs/snake_2/body_tl_2.png').convert_alpha()
            self.body_br = pygame.image.load('imgs/snake_2/body_br_2.png').convert_alpha()
            self.body_bl = pygame.image.load('imgs/snake_2/body_bl_2.png').convert_alpha()

    def draw(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            print(self.body)
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            if index == 0:
                self.app.screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.app.screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.app.screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.app.screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        self.app.screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        self.app.screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        self.app.screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        self.app.screen.blit(self.body_br, block_rect)

    def update(self):
        self.move()
        self.collision()
        self.eat()

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = self.start_pos
        self.direction = Vector2(1, 0)

    def eat(self):
        if self.app.apple.pos == self.body[0]:
            self.app.apple.randomize()
            self.add_block()

        for block in self.body[1:]:
            if block == self.app.apple.pos:
                self.app.apple.randomize()

    def collision(self):
        if not 0 <= self.body[0].x < CELL_NUMBER or not 0 <= self.body[0].y < CELL_NUMBER:
            self.app.state = "end_game"
            self.app.active_buttons = self.app.end_game.end_game_buttons
            self.app.fps = FPS
        for block in self.body[1:]:
            if block == self.body[0]:
                self.app.state = "end_game"
                self.app.active_buttons = self.app.end_game.end_game_buttons
                self.app.fps = FPS
