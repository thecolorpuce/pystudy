import sys

import pygame
from settings import Settings
from star import Star


class Stargame:
    """Overall class for the star printout."""
    
    def __init__(self):
        """Initialze the star printout, and resources."""
        pygame.init()
        self.settings = Settings()
        self.star = pygame.sprite.Group()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("STARZZZZZZZZZ")
    
    def run_game(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self._update_screen()
            self._create_star_sky()
            
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # Keydown 'q' quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _create_star_sky(self):
        """Create the stars."""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = 20
        number_stars_x = 5
        
        # Determine the number of rows of stars to be fit to the screen
        available_space_y = (self.settings.screen_height - 
                             (3 * star_height))
        number_rows = 4
        
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)
    
    def _create_star(self, star_number, row_number):
        """Create a star, and place it in the row."""
        star = Star(self)
        rand_x, rand_y = star.random_placement()
        print(f"{rand_x}, {rand_y}")
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_height * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star.rect.height * row_number 
        star.rect.x = star.rect.x + rand_x
        star.rect.y = star.rect.y + rand_y
        self.star.add((star))
    
    def _update_screen(self):
        """Update the screen, and flip to new images."""
        self.screen.fill(self.settings.bg_color)
        self.star.draw(self.screen)
        
        pygame.display.flip()
    

if __name__ == '__main__':
    # Make, and run instance
    st = Stargame()
    st.run_game()