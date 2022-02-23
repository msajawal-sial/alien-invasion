import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single Alien """
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """ A function to draw the alien at its correct position """
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.ai_settings.fleet_direction * self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False


