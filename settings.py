class Settings():
    '''A class to store all settings for a game'''

    def __init__(self):
        '''Initialize game's settings'''
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        # basket settings
        self.basket_speed = 1

        # egg settings
        self.egg_drop_speed = 0.5

        # bomb settings
        self.bomb_drop_speed = 0.75