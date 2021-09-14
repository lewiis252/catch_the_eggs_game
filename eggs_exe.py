import pygame

from settings import Settings
import game_functions as gf
from basket import Basket
from egg import Egg
from button import Button
from game_stats import GameStats
from bomb import Bomb
from scoreboard import Scoreboard


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Catch the egg")

    # make a basket
    basket = Basket(game_settings, screen)

    # make an egg
    egg = Egg(game_settings, screen)

    # make a bobm
    bomb = Bomb(game_settings, screen)

    # make a button
    play_button = Button(game_settings, screen, 'Play')


    # create an instance to store game statistics and scoreboard
    stats = GameStats(game_settings)
    gf.load_high_score(stats)
    scoreboard = Scoreboard(game_settings, screen, stats)

    # Start the main loop for the game
    while True:

        gf.check_events(game_settings, screen, basket, egg, bomb, play_button, stats, scoreboard)
        if stats.game_active:
            basket.update()
            egg.update()
            bomb.update()

        gf.update_screen(game_settings, screen, basket, egg, play_button, stats, bomb, scoreboard)





run_game()


