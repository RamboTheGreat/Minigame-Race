import pygame, colors
class player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        # Loads all images of the player
        self.images_up = [pygame.image.load("maincharacter/6.png")]
        self.images_left = [pygame.image.load("maincharacter/4.png"),
        pygame.image.load("maincharacter/20.png"),
        pygame.image.load("maincharacter/21.png"),
        pygame.image.load("maincharacter/22.png"),
        pygame.image.load("maincharacter/23.png"),
        pygame.image.load("maincharacter/24.png"),
        pygame.image.load("maincharacter/25.png"),
        pygame.image.load("maincharacter/26.png"),
        pygame.image.load("maincharacter/27.png"),
        pygame.image.load("maincharacter/28.png"),
        pygame.image.load("maincharacter/29.png")]
        self.images_right = [pygame.image.load("maincharacter/7.png"),
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
        self.image = self.images_up[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.score = 0
        # Timers for animation
        self.timer_left = 0
        self.timer_right = 0

    def update(self, WIDTH, HEIGHT):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        # Control animation and direction when
        # keys are pressed
        if keystate[pygame.K_a]:
            self.speedx = -8
            if self.timer_left == 60:
                self.image = self.images_left[10]
                self.timer_left = 0
            elif self.timer_left == 54:
                self.image = self.images_left[9]
            elif self.timer_left == 48:
                self.image = self.images_left[8]
            elif self.timer_left == 42:
                self.image = self.images_left[7]
            elif self.timer_left == 36:
                self.image = self.images_left[6]
            elif self.timer_left == 30:
                self.image = self.images_left[5]
            elif self.timer_left == 24:
                self.image = self.images_left[4]
            elif self.timer_left == 18:
                self.image = self.images_left[3]
            elif self.timer_left == 12:
                self.image = self.images_left[2]
            elif self.timer_left == 6:
                self.image = self.images_left[1]
            elif self.timer_left == 0:
                self.image = self.images_left[0]
            self.timer_left += 1
        if keystate[pygame.K_d]:
            self.speedx = 8
            if self.timer_right == 60:
                self.image = self.images_right[10]
                self.timer_right = 0
            elif self.timer_right == 54:
                self.image = self.images_right[9]
            elif self.timer_right == 48:
                self.image = self.images_right[8]
            elif self.timer_right == 42:
                self.image = self.images_right[7]
            elif self.timer_right == 36:
                self.image = self.images_right[6]
            elif self.timer_right == 30:
                self.image = self.images_right[5]
            elif self.timer_right == 24:
                self.image = self.images_right[4]
            elif self.timer_right == 18:
                self.image = self.images_right[3]
            elif self.timer_right == 12:
                self.image = self.images_right[2]
            elif self.timer_right == 6:
                self.image = self.images_right[1]
            elif self.timer_right == 0:
                self.image = self.images_right[0]
            self.timer_right += 1
        self.rect.x += self.speedx
        # Lets player wrap around
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        