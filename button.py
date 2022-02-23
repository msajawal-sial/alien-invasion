import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """ initialize button attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)  # Green Color Button
        self.text_color = (255, 255, 255)  # White Text
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color)
        self.msg_rect = self.msg_img.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_rect)


