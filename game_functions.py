import sys
import pygame
import json
import os.path


def update_screen(game_settings, screen, basket, egg, play_button, stats, bomb, scoreboard):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(game_settings.bg_color)
    basket.blitme()


    # draw score
    scoreboard.show_score()
    if stats.game_active == True:
        bomb.blitme()
        egg.blitme()

    update_egg(game_settings, screen, basket, egg, stats, scoreboard)
    update_bomb(game_settings, screen, basket, bomb, stats)



    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def check_events(game_settings, screen, basket, egg, bomb, play_button, stats, scoreboard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, basket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, basket)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, basket, egg, bomb, play_button, stats, mouse_x, mouse_y, scoreboard)


def check_keydown_events(event, basket):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        basket.moving_right = True
    elif event.key == pygame.K_LEFT:
        basket.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, basket):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        basket.moving_right = False
    elif event.key == pygame.K_LEFT:
        basket.moving_left = False

def drop_egg(game_settings, egg):
    '''drop an egg down'''
    egg.rect.y += game_settings.egg_drop_speed

def drop_bomb(game_settings, bomb):
    '''drop a bomb down'''
    bomb.rect.y += game_settings.bomb_drop_speed


def check_egg_bottom(game_settings, screen, egg, stats):
    '''check if an egg have reached the bottom of the screen and create a new egg'''

    screen_rect = screen.get_rect()
    if egg.rect.bottom == screen_rect.bottom:
        # print("stracony punkt")
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_bomb_bottom(game_settings, screen, bomb, stats):
    '''check if a bomb have reached the bottom of the screen and create a new bomb'''

    screen_rect = screen.get_rect()
    if bomb.rect.bottom == screen_rect.bottom:
        bomb.new_bomb()

def check_basket_egg_collision(game_settings, screen, stats, basket, egg, scoreboard):
    ''' check ig egg reached basket and add point'''
    if egg.rect.bottom >= basket.rect.top and egg.rect.bottom <= basket.rect.bottom and \
            egg.rect.right >= basket.rect.left and egg.rect.left <= basket.rect.right:
        # print("punkt")
        stats.score += 10
        scoreboard.prep_score()
        check_high_score(stats, scoreboard)
        egg.new_egg()

def check_basket_bomb_collision(game_settings, screen, basket, bomb, stats):
    ''' check if bomb hit basket and lose game'''
    if bomb.rect.bottom >= basket.rect.top and bomb.rect.bottom <= basket.rect.bottom and \
            bomb.rect.right >= basket.rect.left and bomb.rect.left <= basket.rect.right:
        # print("stracony punkt")
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_egg(game_settings, screen, basket, egg, stats, scoreboard):
    check_egg_bottom(game_settings, screen, egg, stats)
    check_basket_egg_collision(game_settings, screen, stats, basket, egg, scoreboard)

def update_bomb(game_settings, screen, basket, bomb, stats):
    check_bomb_bottom(game_settings, screen, bomb, stats)
    check_basket_bomb_collision(game_settings, screen, basket, bomb, stats)

def check_play_button(game_settings, screen, basket, egg, bomb, play_button, stats,  mouse_x, mouse_y, scoreboard):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # set game as active
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        scoreboard.prep_score()
        scoreboard.prep_high_score()

        # center basket
        basket.center_basket()

        # new egg position
        egg.new_egg()

        # new bomb position
        bomb.new_bomb()

def check_high_score(stats, scoreboard):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
        with open('highscore.json', 'w') as obj:
            json.dump(stats.high_score, obj)

def load_high_score(stats):
    # load highscore from json file if exist
    if os.path.exists('highscore.json'):
        with open('highscore.json') as obj:
            stats.high_score = json.load(obj)











