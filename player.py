import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(100, 100))

    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()
