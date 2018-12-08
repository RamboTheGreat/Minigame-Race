import pygame, colors


# Simple class that will set the gamestations
class Gamestations(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gamestations.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
