import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Position the bullet to align to ship
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the Bullet at its current position """
        pygame.draw.rect(self.screen, self.color, self.rect)
