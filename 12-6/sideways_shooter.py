import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class SidewaysShooter:
    """Overall class for a sideways shooter."""
    
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._delete_bullets()
            self._update_screen()
            pygame.display.flip()
    
    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting..")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
                self.ship.moving_up = True
                print(event.key)
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            print(event.key)
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            print('Quitting..')
            sys.exit()
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        """Create a new bullet, and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            print("FIRING")
    
    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        self.bullets.update()
    
    def _delete_bullets(self):
        """Deletes bullets that have gone off screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
            
    def _update_screen(self):
        """Update the images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
    
if __name__ == '__main__':
    # Make an instance, and run it.
    ss = SidewaysShooter()
    ss.run_game()