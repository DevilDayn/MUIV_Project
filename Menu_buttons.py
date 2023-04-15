import pygame
from Button import *

class Exit_button(Button):
    def action(self):
        pygame.quit()

class Start_button(Button):
    def action(self):
        print('Game start')

class Settings_button(Button):
    def action(self):
        if self.clicked == True:
            pass


class Load_button(Button):
    def action(self):
        print('Load')

class Back_button(Button):
    def action(self):
        pass
