import pygame
import random
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.ai_settings =  Settings()
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = random.randint(0, 1000) 
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.y = float(self.rect.y)
    
    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        '''Movie Down'''
        self.y += self.ai_settings.alien_speed_factor
        self.rect.y = self.y