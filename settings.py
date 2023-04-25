import pygame

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game's static settings"""
        
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)     
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
        self.fleet_drop_speed = 5
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        