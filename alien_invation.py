import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, alien)

run_game()
