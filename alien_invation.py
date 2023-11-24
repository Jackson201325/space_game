import pygame

from settings import Settings
from ship import Ship
# from alien import Alien
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)

    # Group of ships and aliens
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
