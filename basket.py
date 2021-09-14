import pygame


class Basket():
    def __init__(self, game_settings, screen):
        """Initialize the basket and set its starting position."""
        self.screen = screen
        self.game_settings = game_settings

        # Load the basket image and get its rect.
        self.image = pygame.image.load('assets/basket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new basket at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

        # store a decimal value for the basket's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the basket's position based on the movement flags.'''
        # update the basket's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.basket_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.basket_speed

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def center_basket(self):
        """center the basket on the screen"""
        self.center = self.screen_rect.centerx