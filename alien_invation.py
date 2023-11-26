import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoardbard
from button import Button
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoardbard(ai_settings, screen, stats)

    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings, screen, "Play")

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            print("lifes: " + str(stats.ships_left))

        gf.update_screen(ai_settings, screen, sb, stats, ship, aliens, bullets, play_button)

run_game()
