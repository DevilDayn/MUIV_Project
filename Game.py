import pygame
import sys
from Player import Player_model


def run_game():


    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Анигеляторная пушка")
    bg_color = (0, 0, 0)
    model = Player_model(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        model.output()
        pygame.display.flip

run_game()

print("Hello world")