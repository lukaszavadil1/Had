import pygame
from settings import *


class StateMachine:
    def __init__(self, app):
        self.app = app

    def get_events(self):
        # EVENT SWITCH
        if self.app.state == "intro":
            self.app.intro.intro_events()
        if self.app.state == "play":
            self.app.play.play_events()
        if self.app.state == "pause":
            self.app.pause.pause_events()
        if self.app.state == "interlude":
            self.app.interlude.interlude_events()
        if self.app.state == "instructions":
            self.app.instructions.instructions_events()
        if self.app.state == "end_game":
            self.app.end_game.end_game_events()

    def update(self):
        # MAIN UPDATE
        if self.app.state == "intro":
            self.app.intro.intro_update()
        if self.app.state == "play":
            self.app.play.play_update()
        if self.app.state == "pause":
            self.app.pause.pause_update()
        if self.app.state == "interlude":
            self.app.interlude.interlude_update()
        if self.app.state == "instructions":
            self.app.instructions.instructions_update()
        if self.app.state == "end_game":
            self.app.end_game.end_game_update()

    def draw(self):
        # MAIN DRAW
        self.app.screen.fill(COLORS.get("bgcolor"))
        if self.app.state == "intro":
            self.app.intro.intro_draw()
        if self.app.state == "play":
            self.app.play.play_draw()
        if self.app.state == "pause":
            self.app.pause.pause_draw()
        if self.app.state == "interlude":
            self.app.interlude.interlude_draw()
        if self.app.state == "instructions":
            self.app.instructions.instructions_draw()
        if self.app.state == "end_game":
            self.app.end_game.end_game_draw()
        pygame.display.update()
