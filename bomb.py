import pygame

from random import randint


class Bomb():
    """A class to represent a single bomb."""

    def __init__(self, game_settings, screen):
        """Initialize the egg and set its starting position."""
        super(Bomb, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.screen_rect = screen.get_rect()

        # Load the bomb image and set its rect attribute.
        self.image = pygame.image.load('assets/bomb.bmp')
        self.rect = self.image.get_rect()

        # Start new bomb near the top of the screen, at random x position.
        self.rand_position_x = randint(100, 100)
        self.rect.x = self.rand_position_x
        self.rect.y = self.screen_rect.top


        # Store the egg's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''drop bomb down'''
        self.y += self.game_settings.bomb_drop_speed
        self.rect.y = self.y

    def new_bomb(self):
        self.rand_position_x = randint(100, 1100)
        self.rect.x = self.rand_position_x
        self.rect.y = self.screen_rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.screen.blit(self.image, self.rect)

    def blitme(self):
        """Draw the egg at its current location."""
        self.screen.blit(self.image, self.rect)