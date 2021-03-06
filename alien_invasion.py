import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame.time import Clock


def run_game():
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    score = Scoreboard(ai_settings, screen, stats)
    gf.load_high_score(stats)
    play_button = Button(ai_settings, screen, "Play")
    gf.create_fleet(ai_settings, screen, aliens, ship)
    clock = Clock()

    while True:
        clock.tick(1000)
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, score)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, aliens, ship, bullets, stats, score)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, score)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, score)


# main
run_game()
