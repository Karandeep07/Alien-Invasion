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
        self.ship_speed = 0.5  # Original = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (80, 80, 80)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1