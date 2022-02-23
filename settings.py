class Settings():
    """" A class for settings for Alien Invasion"""

    def __init__(self):
        # Screen Settings
        self.screen_height = 600
        self.screen_width = 900
        self.bg_color = (230, 230, 230)  # Background Color=Light Grey

        # Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # Dark grey
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 15

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.75
        self.alien_speed_factor = 0.75
        self.bullet_speed_factor = 2.25
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
