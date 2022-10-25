import pygame


class Character:
    """A class to initialize the character. 
    Going to use Mith ridites drinking a PBR for now."""
    
    def __init__(self, ai_game):
        """Initialize the character and their starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the character image and get rect
        self.image = pygame.image.load('images/MithPBRComp.bmp')
        self.rect = self.image.get_rect()
        
        # Start the character at Center of the screen
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        """Draw the character at their current location."""
        self.screen.blit(self.image, self.rect)