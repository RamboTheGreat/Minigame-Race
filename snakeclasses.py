import pygame, colors, time
from random import randint

class player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        # Instantiates the player
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(colors.blue)
        self.rect = self.image.get_rect()
        self.x = 40
        self.y = 0
        self.score = 0

    def update(self, WIDTH, HEIGHT):
        # Detects what key is pressed and sets
        # movement accordingly
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.x = 0
            self.y = -40
        if keystate[pygame.K_a]:
            self.x = -40
            self.y = 0
        if keystate[pygame.K_s]:
            self.x = 0
            self.y = 40
        if keystate[pygame.K_d]:
            self.x = 40
            self.y = 0
        self.rect.x +=  self.x
        self.rect.y +=  self.y
        # Controls wrap around of snake
        if self.rect.left > WIDTH:
            self.rect.right  =  0
        if self.rect.right < 0:
            self.rect.left  =  WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.top  =  0
        if self.rect.top < 0:
            self.rect.bottom  =  HEIGHT
        time.sleep(50 / 1000)



class food(pygame.sprite.Sprite):
    def __init__(self, startingpointx, startingpointy):
        # Instiates food
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(colors.green)
        self.rect = self.image.get_rect()
        self.rect.x = startingpointx
        self.rect.y = startingpointy

        
class bad(pygame.sprite.Sprite):
    def __init__(self, startingpointx, startingpointy):
        # Instantiates an obstacles when called
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(colors.red)
        self.rect = self.image.get_rect()
        self.rect.x = startingpointx
        self.rect.y = startingpointy