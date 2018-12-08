import pygame, colors, fallingplayer


class Catchobjects(pygame.sprite.Sprite):
    # Initializes the pygame sprite
    def __init__(self, WIDTH, ObjSpeed, startingpoint, obj):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("catch_objects/catch0.png"),
            pygame.image.load("catch_objects/catch1.png"),
            pygame.image.load("catch_objects/catch2.png")]
        self.image = self.images[obj]
        self.rect = self.image.get_rect()
        self.speedy = 0
        self.rect.centerx = startingpoint
        self.rect.bottom = 0
        self.ObjSpeed = ObjSpeed

    def update(self, ObjSpeed, HEIGHT, group, player):
        # every time update is called, the object
        # will move down until the bottom of the screen
        # where it will despawn
        self.speedy = self.ObjSpeed
        self.rect.y += self.speedy
        if self.rect.y > (HEIGHT - 30):
            group.remove(self)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, WIDTH, ObjSpeed, startingpoint):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("catch_objects/bomb.png")
        self.rect = self.image.get_rect()
        self.speedy = 0
        self.rect.centerx = startingpoint
        self.rect.bottom = 0
        self.ObjSpeed = ObjSpeed

    def update(self, ObjSpeed, HEIGHT, group, player):
        # every time update is called, the object
        # will move down until the bottom of the screen
        # where it will despawn
        self.speedy = self.ObjSpeed
        self.rect.y += self.speedy
        if self.rect.y > (HEIGHT - 30):
            group.remove(self)
