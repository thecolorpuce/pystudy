import sys
import pygame
from settings import Settings

class InputTester:
    """Overall class to manage file"""
    
    def __init__(self):
        """Initialize the screen, and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.caption = pygame.display.set_caption(self.settings.set_caption)
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()          
            
            # Make most recently drawn screen visible
            pygame.display.flip()
    
    def _check_events(self):
        """Respond to kypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Keydown presses
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
    
    def _check_keydown_events(self, event):
        """Response to keypresses"""
        print(event.key)
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)


if __name__ == '__main__':
    # Make an instance and run it
    it = InputTester()
    it.run_game()