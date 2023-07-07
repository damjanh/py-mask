import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/obstacle.png')
        self.rect = self.image.get_rect(center=(400,400))
