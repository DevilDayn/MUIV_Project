import pygame
from Button import *

from Menu_buttons import *
pygame.init()

screen_width = 100
screen_height = 100

screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Game on python")

start_img = pygame.image.load('Assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Assets/exit_btn.png').convert_alpha()
background_image = pygame.image.load('Assets/back.jpg')


FPS = pygame.time.Clock()
fps = 60

button_play = Start_button((screen_height//2) * 1, (screen_width//2) * 3, start_img, 0.7)
button_exit = Start_button((screen_height//2) * 2, (screen_width//2) * 3, start_img, 0.7)


Game_is_running = True
while Game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Game_is_running = False

    screen.blit(background_image, (0, 0))

    button_play.draw(screen)
    button_exit.draw(screen)


    pygame.display.update()

pygame.quit()
