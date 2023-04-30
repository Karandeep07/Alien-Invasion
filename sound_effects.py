import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/laser1.wav')
alien_sound = pygame.mixer.Sound('sounds/explosion1.wav')
play_button_sound = pygame.mixer.Sound('sounds/click.wav') # Increase volume
highscore_sound = pygame.mixer.Sound('sounds/Hi-Score.ogg')
life_lost_sound = pygame.mixer.Sound('sounds/life_lost.mp3')
game_over_sound = pygame.mixer.Sound('sounds/GameOver.wav')