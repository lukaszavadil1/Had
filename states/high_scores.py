from components.button import *
from components.text import *


class HighScores:
    def __init__(self, app):
        self.app = app
        self.high_scores_buttons = []
        self.high_scores_texts = []
        self.scores_font = pygame.font.SysFont("comicsansms", TEXT_SIZE.get("medium"))

    def high_scores_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
            if event.type == pygame.K_ESCAPE:
                self.app.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.high_scores_buttons:
                    if button.hovered:
                        button.click()
                    else:
                        pass

    def high_scores_update(self):
        for button in self.app.active_buttons:
            button.update()
        for text in self.high_scores_texts:
            text.update()

    def high_scores_draw(self):
        for button in self.app.active_buttons:
            button.draw()
        for text in self.high_scores_texts:
            text.draw()
        y = 80
        for index, pair in enumerate(self.app.players_scores):
            if index >= 10:
                pass
            else:
                y += 60
                self.show_scores(str(index+1) + ".)   " + str(pair[0]) + " - " + str(pair[1]), [80, y])

    def high_scores_intro(self):
        self.app.state = "intro"
        self.app.active_buttons = self.app.intro.intro_buttons

    def high_scores_quit(self):
        self.app.running = False

    def make_high_scores_buttons(self):
        high_scores_intro_button = Button(self.app,
                                           [20, 805],
                                           225,
                                           50,
                                           COLORS.get("yellow"),
                                           TEXT_SIZE.get("small"),
                                           hover_color=COLORS.get("light_yellow"),
                                           action=self.high_scores_intro,
                                           text="ZPĚT DO MENU")
        self.high_scores_buttons.append(high_scores_intro_button)

        high_scores_quit_button = Button(self.app,
                                          [655, 805],
                                          125,
                                          50,
                                          COLORS.get("red"),
                                          TEXT_SIZE.get("small"),
                                          hover_color=COLORS.get("light_red"),
                                          action=self.high_scores_quit,
                                          text="KONEC")
        self.high_scores_buttons.append(high_scores_quit_button)

    def make_high_scores_texts(self):
        head_txt = Text(self.app,
                        [100, 25],
                        TEXT_SIZE.get("large"),
                        "Tabulka nejvyšších skóre",
                        COLORS.get("blue"))
        self.high_scores_texts.append(head_txt)

    def show_scores(self, score, pos):
        text = self.scores_font.render(score, False, COLORS.get("black"))
        self.app.screen.blit(text, (pos[0], pos[1]))
