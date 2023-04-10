import pygame

from Button import *

class Exit_button(Button):
    def action(self):
        pygame.quit()

class Start_button(Button):
    def action(self):
        print('Game start')

class Setiings_button(Button):
    def action(self):
        print('Settings')

class Load_button(Button):
    def action(self):
        print('Load')
