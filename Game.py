import pygame
from Button import *
from Variables import *
from Menu_buttons import *
pygame.init()



screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Game on python")

start_img = pygame.image.load('Assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Assets/exit_btn.png').convert_alpha()
load_img = pygame.image.load('Assets/load_btn.png').convert_alpha()
settings_img = pygame.image.load('Assets/settings_btn.png').convert_alpha()
background_image = pygame.image.load('Assets/back.jpg')


FPS = pygame.time.Clock()
fps = 60

button_play = Start_button((screen_width//5) * 1, (screen_height//4) * 3.5, start_img, 0.7)
button_load = Load_button((screen_width//5) * 2, (screen_height//4) * 3.5, load_img, 0.7)
button_settings = Setiings_button((screen_width//5) * 3, (screen_height//4) * 3.5, settings_img, 0.7)
button_exit = Exit_button((screen_width//5) * 4, (screen_height//4) * 3.5, exit_img, 0.7)



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
    button_load.draw(screen)
    button_settings.draw(screen)

    pygame.display.update()

pygame.quit()
