from components.text import *
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
                    pygame.draw.rect(self.app.screen, COLORS.get("bgcolor"), (165, 805, 480, 60))
                    for num in self.countdown:
                        countdown_text = Text(self.app, [380, 800], TEXT_SIZE.get("large"), num, color=COLORS.get("light_red"))
                        countdown_text.draw()
                        pygame.display.update()
                        pygame.draw.rect(self.app.screen, COLORS.get("bgcolor"), (380, 805, 40, 70))
                        time.sleep(1)
                        pygame.display.update()
                    self.interlude_play()

    def interlude_update(self):
        # INTERLUDE STATE UPDATE
        # self.app.game_window.update()
        pass

    def interlude_draw(self):
        # INTERLUDE STATE DRAW
        self.app.game_window.draw()
        resume_text = Text(self.app, [165, 805], TEXT_SIZE.get("medium"), "Stiskni 'S' pro start hry")
        resume_text.draw()

    def interlude_quit(self):
        # QUIT FROM INTERLUDE STATE
        self.app.running = False

    def interlude_play(self):
        # FROM INTERLUDE STATE TO PLAY
        self.app.state = "play"
        self.app.active_buttons = self.app.play.play_buttons
        self.app.instructions.check_fps()

