import pygame
from Variables import screen_height, screen_width
pygame.display.set_mode((screen_height, screen_width))


class Button:
    def __init__(self, x, y, image):
        width = image.get_width()
        height = image.get_height()
        scale = (screen_width**2 + screen_height**2)/(1920**2 + 1080**2)
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def action(self):
        pass