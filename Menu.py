import pygame
from Variables import window_size

pygame.init()
class Menu:

    def __init__(self, items, font, font_size, font_color, x, y):
        self.items = items
        self.font = pygame.font.Font(font, font_size)
        self.font_color = font_color
        self.x = x
        self.y = y

    def draw(self, surface):
        for index, item in enumerate(self.items):
            label = self.font.render(item, True, self.font_color)
            width = label.get_width()
            height = label.get_height()

            x_pos = self.x - ((width / 2))
            y_pos = self.y + ((index * height))

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0]:
                if menu_x - (height / 2) < mouse_pos[0] < menu_x + (width / 2):
                    if menu_y < mouse_pos[1] < menu_y + height:
                        print("Start Game clicked")
                elif menu_y + height < mouse_pos[1] < menu_y + (height * 2):
                    print("Options clicked")
                elif menu_y + (height * 2) < mouse_pos[1] < menu_y + (height * 3):
                    pygame.quit()

            surface.blit(label, (x_pos, y_pos))




menu_items = ["Start Game", "Options", "Exit"]
menu_font = 'freesansbold.ttf'
menu_font_size = 36
menu_font_color = (255, 255, 255)
menu_x = window_size[0] / 2
menu_y = window_size[1] / 2

menu_draw = Menu(menu_items, menu_font, menu_font_size, menu_font_color, menu_x, menu_y)





