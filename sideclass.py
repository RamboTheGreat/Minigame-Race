import pygame, colors, time
from random import randint

class player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        # Loads images 
        self.images_default = [pygame.image.load("maincharacter/7.png"),
        pygame.image.load("maincharacter/40.png"),
        pygame.image.load("maincharacter/41.png"),
        pygame.image.load("maincharacter/42.png"),
        pygame.image.load("maincharacter/43.png"),
        pygame.image.load("maincharacter/44.png"),
        pygame.image.load("maincharacter/45.png"),
        pygame.image.load("maincharacter/46.png"),
        pygame.image.load("maincharacter/47.png"),
        pygame.image.load("maincharacter/48.png"),
        pygame.image.load("maincharacter/49.png")] 
        self.image = self.images_default[0]
        self.rect=self.image.get_rect()
        self.rect.x = 80
        self.rect.y= HEIGHT - 80
        self.score = 0
        # Instantiates timers of jumping and animations
        self.jumpwait = 0
        self.animation = 1
        self.animationtimer = 0
        self.inJump = 0
        self.NextJump = 40
    def update(self, WIDTH, HEIGHT):
        keystate = pygame.key.get_pressed()
        # Detects if the player has pressed space.\
        # Will only work if the player is not alread
        # in a jump and cooldown of jump has been reached
        if keystate[pygame.K_SPACE] and self.inJump == 0 and self.NextJump > 40:
            self.jumpwait = 0
            self.rect.y = HEIGHT - 200
            self.animation = 0
            self.inJump = 1
            self.NextJump = 0

        # Controls how long player is in the air
        if self.jumpwait > 40:
            # Slowly sets player back to the ground
            self.rect.y += 9.81
            if self.rect.y >= HEIGHT - 80:
                self.animation = 1
                self.inJump = 0
                self.jumpwait = 0
        # Walking animaiton
        if self.animation == 1:
            if self.animationtimer == 60:
                self.image = self.images_default[10]
                self.animationtimer = 0
            elif self.animationtimer == 54:
                self.image = self.images_default[9]
            elif self.animationtimer == 48:
                self.image = self.images_default[8]
            elif self.animationtimer == 42:
                self.image = self.images_default[7]
            elif self.animationtimer == 36:
                self.image = self.images_default[6]
            elif self.animationtimer == 30:
                self.image = self.images_default[5]
            elif self.animationtimer == 24:
                self.image = self.images_default[4]
            elif self.animationtimer == 18:
                self.image = self.images_default[3]
            elif self.animationtimer == 12:
                self.image = self.images_default[2]
            elif self.animationtimer == 6:
                self.image = self.images_default[1]
            elif self.animationtimer == 0:
                self.image = self.images_default[0]
            self.animationtimer += 1
        if self.rect.y == HEIGHT - 200:
            self.jumpwait += 1
        self.NextJump += 0.75
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, SPEED):
        pygame.sprite.Sprite.__init__(self)
        # Loads sprite images needed for animation
        self.images = [pygame.image.load("Enemy/12.png"),
        pygame.image.load("Enemy/13.png"),
        pygame.image.load("Enemy/14.png"),
        pygame.image.load("Enemy/15.png"),
        pygame.image.load("Enemy/16.png"),
        pygame.image.load("Enemy/17.png"),
        pygame.image.load("Enemy/18.png"),
        pygame.image.load("Enemy/19.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.speed = SPEED
        self.speedx = 0
        self.rect.y = HEIGHT - 80
        self.rect.x =  WIDTH - 80
        self.spritetimer = 0
    def update(self, group, player1):
        # Moves the enemy to left and plays animation
        self.speedx = self.speed
        self.rect.x -= self.speedx
        if self.spritetimer == 60:
            self.image = self.images[2]
            self.spritetimer = 0
        elif self.spritetimer == 54:
            self.image = self.images[1]
        elif self.spritetimer == 48:
            self.image = self.images[0]
        elif self.spritetimer == 42:
            self.image = self.images[7]
        elif self.spritetimer == 36:
            self.image = self.images[6]
        elif self.spritetimer == 30:
            self.image = self.images[5]
        elif self.spritetimer == 24:
            self.image = self.images[4]
        elif self.spritetimer == 18:
            self.image = self.images[3]
        elif self.spritetimer == 12:
            self.image = self.images[2]
        elif self.spritetimer == 6:
            self.image = self.images[1]
        elif self.spritetimer == 0:
            self.image = self.images[0]
        self.spritetimer += 1

        if self.rect.x < 0:
            group.remove(self)
            player1.score += 1



