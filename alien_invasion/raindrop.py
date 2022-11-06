import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent raindrops."""
    
    def __init__(self, ai_game):
        """Initialize the raindrops, and prepare for some pain.."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.raindrop_color
        
        # Store raindrop locations
        self.y = float(self.rect.y)
        
        # Create raindrop at (0, 0) and then set different positions
        self.rect = pygame.Rect(0, 0, self.settings.raindrop_width,
                                self.settings.raindrop_height)
    
    def update(self):
        """Move raindrops down the screen."""
        # Update the position of the raindrops.
        self.y += self.settings.raindrop_speed
        # Update the rect position of the raindrop
        self.rect.y = self.y
    
    def draw_raindrop(self):
        """Function to draw the raindrop on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)