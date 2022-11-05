from random import randint

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a star."""
    
    def __init__(self, st_game):
        """Initialize the star and the star's starting position."""
        super().__init__()
        self.screen = st_game.screen
        
        # Load the image of the star, and set rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        
        # Place each star near the top-left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def random_placement(self):
        """A function to change the placement of each star"""
        rand_x = randint(0, 100)
        rand_y = randint(0, 100)
        
        return [rand_x, rand_y]