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

button_play = Start_button((screen_width//5) * 1, (screen_height//4) * 3, start_img)
button_load = Load_button((screen_width//5) * 2, (screen_height//4) * 3, load_img)
button_settings = Settings_button((screen_width//5) * 3, (screen_height//4) * 3, settings_img)
button_exit = Exit_button((screen_width//5) * 4, (screen_height//4) * 3, exit_img)

def main_menu():
    button_play.draw(screen)
    button_exit.draw(screen)
    button_load.draw(screen)
    button_settings.draw(screen)

def setting_menu():
    button_exit.draw(screen)

Main_menu_is_running = True
Settings_menu_is_running = False
Load_menu_is_running = False
Start_menu_is_running = False

while Main_menu_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Main_menu_is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Main_menu_is_running = False


    screen.blit(background_image, (0, 0))

    button_play.draw(screen)
    button_exit.draw(screen)
    button_load.draw(screen)
    button_settings.draw(screen)

    pygame.display.update()


while Settings_menu_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Settings_menu_is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Settings_menu_is_running = False

    screen.blit(background_image, (0, 0))

    setting_menu()

    pygame.display.update()


while Load_menu_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Main_menu_is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Main_menu_is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            Main_menu_is_running = False
            Settings_menu_is_running = True

    screen.blit(background_image, (0, 0))

    main_menu()

    pygame.display.update()

pygame.quit()
