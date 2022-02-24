import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """" A class for ship object"""
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.moving_right = False
        self.moving_left = False

        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starting Ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # For Speed Control
        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Drawing the ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
