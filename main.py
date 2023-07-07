import pygame
import sys
from obstacle import Obstacle
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()

        self.player = pygame.sprite.GroupSingle(Player())
        self.obstacle = pygame.sprite.GroupSingle(Obstacle())

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('white')

            self.player.update()

            self.player.draw(self.screen)
            self.obstacle.draw(self.screen)

            if pygame.sprite.spritecollide(self.player.sprite, self.obstacle, False, pygame.sprite.collide_mask):
                self.player.sprite.image.fill('green')
            else:
                self.player.sprite.image.fill('red')

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
