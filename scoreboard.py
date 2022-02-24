import pygame.font


class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        rounded_high_score = round(self.stats.high_score, 1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.y = self.score_rect.y
        self.high_score_rect.centerx = self.screen_rect.centerx


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)

    def prep_level(self):
        self.level_img = self.font.render(str(self.stats.level), True, self.text_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

