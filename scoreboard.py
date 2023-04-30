import pygame.font
from pygame.sprite import Group

import sound_effects as se
from game_stats import GameStats
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) 	
        self.font2 = pygame.font.Font("fonts/Inika-Bold.ttf", 90)
        self.font3 = pygame.font.Font("fonts/Inika-Bold.ttf", 45)
        self.font4 = pygame.font.Font("fonts/IBMPlexSans-Regular.ttf", 38)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.mm_score()
        self.mm_text()
        self.box()

        

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font4.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """Draw score, ships & lvl to the screen."""
        if self.stats.game_active:     
            self.screen.blit(self.score_image, self.score_rect)
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.screen.blit(self.level_image, self.level_rect)
            self.ships.draw(self.screen)
        elif not self.stats.game_active and not self.stats.game_over:
            self.box()
            self.screen.blit(self.high_score_image, self.high_score_recta)
            self.screen.blit(self.score_image, self.score_recta)
            self.screen.blit(self.text_highscore, (42,642))
            self.screen.blit(self.text_score, self.text_rect)
            self.screen.blit(self.text_title, self.text_title_rect)
        else:
            self.box()
            self.screen.blit(self.high_score_image, self.high_score_recta)
            self.screen.blit(self.score_image, self.score_recta)
            self.screen.blit(self.text_highscore, (42,642))
            self.screen.blit(self.text_score, self.text_rect)
            self.screen.blit(self.text_go, self.text_go_rect)
    
    def mm_score(self):
        # Center the high score at the bottom left of the screen.
        self.high_score_recta = self.high_score_image.get_rect()
        self.high_score_recta.left = self.screen_rect.left + 38
        self.high_score_recta.top = 584

        self.score_recta = self.score_image.get_rect()
        self.score_recta.right = self.screen_rect.right - 280
        self.score_recta.top = 584

    def mm_text(self):
        # Labels for Main menu
        self.text_highscore = self.font3.render('HIGHSCORE', True, (0,0,0))

        self.text_score = self.font3.render('YOURSCORE', True, (0,0,0))
        self.text_rect = self.text_score.get_rect()
        self.text_rect.right = self.screen_rect.right - 37
        self.text_rect.top = 642

        # Title 
        self.text_title = self.font2.render('Alien Invasion', True, (0,0,0), (255,255,255))
        self.text_title_rect = self.text_title.get_rect()
        self.text_title_rect.center = self.screen_rect.center
        self.text_title_rect.top = 120

        # Game Over
        self.text_go = self.font2.render('GAME OVER', True,  (0,0,0), (255,255,255))
        self.text_go_rect = self.text_go.get_rect()
        self.text_go_rect.center = self.screen_rect.center
        self.text_go_rect.top = 120

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font4.render(high_score_str, True,self.text_color)
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top 
        

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.stats.highscore_se = self.stats.highscore_se + 1
            self.prep_high_score()
            

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font4.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10 # Change to bottom of screen
            self.ships.add(ship)

    def box(self): # x,y,width,height
        pygame.draw.rect(self.screen, (255, 255, 255), (300,97,680,147))
        pygame.draw.rect(self.screen, (255, 255, 255), (38,651,262,41))
        pygame.draw.rect(self.screen, (255, 255, 255), (980,651,262,41))
