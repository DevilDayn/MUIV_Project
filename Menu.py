import pygame

class Menu:
    def __init__(self):
        self.option_surface = []
        self.callbacks = []
        self.current_option_index = 0

    def append_option(self,option, callback):

    def swich(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.option_surface) - 1))

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, option_y_paddiong):
        for i, option in enumerate(self.option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + 1 * option_y_paddiong)
            if i == self.current_option_index:
                draw.rect(surf, (0, 0, 0), option_rect)
            surf.blit(option, option_rect)

menu = Menu()