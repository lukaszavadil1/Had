import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
Display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Had")
pygame.display.update()


def exit_game():
    pygame.quit()
    quit()


exit_game()
