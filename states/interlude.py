from text import *
import time


class Interlude:
    def __init__(self, app):
        self.app = app
        self.countdown = ["3", "2", "1"]

    def interlude_events(self):
        # INTERLUDE EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.draw.rect(self.app.screen, COLORS.get("bgcolor"), (80, 20, 480, 55))
                    for num in self.countdown:
                        countdown_text = Text(self.app, [280, 0], TEXT_SIZE.get("large"), num, color=COLORS.get("light_red"))
                        countdown_text.draw()
                        pygame.display.update()
                        pygame.draw.rect(self.app.screen, COLORS.get("bgcolor"), (280, 0, 40, 70))
                        time.sleep(1)
                        pygame.display.update()
                    self.interlude_play()
                    self.app.snake.vel = [10, 0]

    def interlude_update(self):
        # INTERLUDE STATE UPDATE
        self.app.snake.vel = [0, 0]
        self.app.snake.pos = [self.app.game_window.width//2+WINDOW_POS[0], self.app.game_window.height//2]
        self.app.game_window.update()

    def interlude_draw(self):
        # INTERLUDE STATE DRAW
        self.app.game_window.draw()
        resume_text = Text(self.app, [80, 10], TEXT_SIZE.get("medium"), "Stiskni 'S' pro start hry")
        resume_text.draw()

    def interlude_quit(self):
        # QUIT FROM INTERLUDE STATE
        self.app.running = False

    def interlude_play(self):
        # FROM INTERLUDE STATE TO PLAY
        self.app.state = "play"
        self.app.active_buttons = self.app.play.play_buttons
