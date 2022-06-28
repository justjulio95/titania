import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, screen object.
    pygame.init()
    tt_settings = Settings()
    screen = pygame.display.set_mode(
        (tt_settings.screen_width, tt_settings.screen_height))
    pygame.display.set_caption("Titania")

    # Make the play button.
    play_button = Button(tt_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(tt_settings)
    sb = Scoreboard(tt_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(tt_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(tt_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(tt_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(tt_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(tt_settings, screen, stats, sb, ship, aliens,
                bullets)

        gf.update_screen(tt_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)

run_game()