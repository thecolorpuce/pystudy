class Settings:
    """Class for general settings."""
    
    def __init__(self):
        """Initialize the Sideways shooter's settings."""
        
        # Screen Settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250, 250, 250)
        
        # Ship Settings
        self.ship_speed = 1.5
        
        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4