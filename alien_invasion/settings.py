class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 220)
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien Fleet Info
        """
        available_space_x = settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Adding Rows
        available_space_y = settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        """
        
        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Rain settings
        self.raindrop_speed = 2.5
        self.raindrop_width = 2
        self.raindrop_height = 10
        self.raindrop_color = (136, 206, 235)