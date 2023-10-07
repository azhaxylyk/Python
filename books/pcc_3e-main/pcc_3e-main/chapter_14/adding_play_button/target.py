import pygame

class Target:
    def __init__(self, ai_game):
        """Initialize target attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Set the dimensions and properties of the button.
        self.width, self.height = 80, 200
        self.button_color = (0, 0, 0)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottomright = self.screen_rect.midright
        self.y = float(self.rect.y)
        
    def draw_target(self):
        """Draw blank button"""
        self.screen.fill(self.button_color, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update(self):
        """Move the alien right or left."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y