import pygame
import sys
from Menu import *
from Variables import window_size

def run_game():


    pygame.init()

    size = (1200, 800)
    screen = pygame.display.set_mode((window_size))
    pygame.display.set_caption("Rock' em , Suck' em")
    bg_color = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        menu_draw.draw(screen)

        pygame.display.flip()





run_game()
