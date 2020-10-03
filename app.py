import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
Display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("imgs/logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Had")

snake_1_head = pygame.image.load("snake_head.png")
snake_2_head = pygame.image.load("snake_head_2.png")
apple_img = pygame.image.load("apple.png")
obstacle_img = pygame.image.load("obstacle.png")

pygame.display.update()


def exit_game():
    pygame.quit()
    quit()


exit_game()
