class Settings():

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.9
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60 ,60
        self.bulltets_allowed = 69

        self.fleet_drop_speed = 5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.alien_speed_factor = 0.5


        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.9
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        self.fleet_direction = 1
        # self.alien_points = 50
        #

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        # self.alien_points = int(self.alien_points * self.score_scale)
