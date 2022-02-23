import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and len(bullets) < ai_settings.bullets_allowed:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button):
    """Respond to user events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, stats, play_button, aliens, bullets, ship, screen, ai_settings)


def check_play_button(mouse_x, mouse_y, stats, play_button, aliens, bullets, ship, screen, ai_settings):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


def update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, score):
    # Update the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    score.show_score()
    for bullet in bullets:
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    # Make the new screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, aliens, ship, bullets, stats, score):
    """" Update position of bullets and remove old bullets """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullets_alien_collision(ai_settings, screen, aliens, ship, bullets, stats, score)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Function to fire the bullet """
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (4 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, x, y):
    alien = Alien(ai_settings, screen)
    alien.x = x
    alien.y = y
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    return alien


def get_number_rows(ai_settings, alien_height, ship):
    ship_height = ship.rect.height
    number_of_rows = ((ai_settings.screen_height - (3 * alien_height) - ship_height)/(2 * alien_height))
    return int(number_of_rows)


def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_of_rows = get_number_rows(ai_settings, alien_height, ship)
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)

    for row_number in range(number_of_rows):
        for alien_number in range(number_aliens_x):
            x = 2 * alien_width + ((2 * alien_number) * alien_width)
            y = alien_height + (2 * (row_number * alien_height))
            alien = create_alien(ai_settings, screen, x, y)
            aliens.add(alien)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship Hit Alien")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    else:
        check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    stats.ships_left -= 1
    print("Lives Left:", stats.ships_left)
    if stats.ships_left > 0:
        bullets.empty()
        aliens.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += 10
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_bullets_alien_collision(ai_settings, screen, aliens, ship, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += (ai_settings.alien_points * len(collisions))
        sb.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
