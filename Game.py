import pygame
import sys
from Variables import *
from Button import *
def run_game():


    pygame.init()

    screen = pygame.display.set_mode((window_height, window_width))
    pygame.display.set_caption("Rock' em , Suck' em")
    bg_color = (0, 0, 0)

    FPS = pygame.time.Clock()
    fps = 60

    while True:
        FPS.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        button_play.draw(screen)
        button_play.click_event(event)

        button_settings.draw(screen)
        button_settings.click_event(event)

        button_exit.draw(screen)
        button_exit.click_event(event)



        pygame.display.flip()





run_game()
