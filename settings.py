import pygame

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        # self.bg_color = (230, 230, 230)     
        self.bg_image = pygame.image.load('images/background.png')

        # Ship settings
        self.ship_speed = 1.5
        