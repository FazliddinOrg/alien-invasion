import pygame
from pygame.sprite import Sprite
from random import choice


def load_random_alien_image():
    """Randomly select an alien image path."""
    image_paths = ['./images/monster.png', './images/gorilla.png']
    return choice(image_paths)


class Alien(Sprite):
    """A single alien enemy in the fleet."""

    def __init__(self, settings, screen):
        """Initialize alien and set its position."""
        super().__init__()
        self.points = 15
        self.screen = screen
        self.settings = settings

        # Load the alien image
        self.image = pygame.image.load(load_random_alien_image())
        self.rect = self.image.get_rect()

        # Start near the top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store float x-coordinate for smooth movement
        self.x = float(self.rect.x)

    def update(self):
        """Move alien left or right depending on fleet direction."""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien hits screen edge."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def draw(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)
