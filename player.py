import pygame
import colors
import time

class Player(pygame.sprite.Sprite):

	def __init__(self, startingX, startingY, playerSize, playerSpeed):

		pygame.sprite.Sprite.__init__(self)
		# Loads all images of the player
		self.images_down = [pygame.image.load("maincharacter/0.png"),
		pygame.image.load("maincharacter/10.png"),
		pygame.image.load("maincharacter/11.png"),
		pygame.image.load("maincharacter/12.png"),
		pygame.image.load("maincharacter/13.png"),
		pygame.image.load("maincharacter/14.png"),
		pygame.image.load("maincharacter/15.png"),
		pygame.image.load("maincharacter/16.png"),
		pygame.image.load("maincharacter/17.png"),
		pygame.image.load("maincharacter/18.png"),
		pygame.image.load("maincharacter/19.png")]
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
		self.images_up = [pygame.image.load("maincharacter/6.png"),
		pygame.image.load("maincharacter/30.png"),
		pygame.image.load("maincharacter/31.png"),
		pygame.image.load("maincharacter/32.png"),
		pygame.image.load("maincharacter/33.png"),
		pygame.image.load("maincharacter/34.png"),
		pygame.image.load("maincharacter/35.png"),
		pygame.image.load("maincharacter/36.png"),
		pygame.image.load("maincharacter/37.png"),
		pygame.image.load("maincharacter/38.png"),
		pygame.image.load("maincharacter/39.png")]
		self.image = self.images_down[0]
		self.rect = self.image.get_rect()
		self.rect.centerx  = startingX
		self.rect.bottom = startingY
		self.speedx = 0
		self.speedy = 0
		self.playerSpeed = playerSpeed
		# Initializes counters for animation
		self.timer_left = 0
		self.timer_right = 0
		self.timer_up = 0
		self.timer_down = 0
		self.score = 0

	def update(self, WIDTH, HEIGHT):
		self.speedx = 0
		self.speedy = 0
		keystate = pygame.key.get_pressed()
		# Detects what key was pressed and
		# moves/ animates the player accordingly
		if keystate[pygame.K_a]:
			self.speedx = -1 * self.playerSpeed
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
			self.speedx = self.playerSpeed
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
		if keystate[pygame.K_w]:
			self.speedy = -1 * self.playerSpeed
			if self.timer_up == 60:
				self.image = self.images_up[10]
				self.timer_up = 0
			elif self.timer_up == 54:
				self.image = self.images_up[9]
			elif self.timer_up == 48:
				self.image = self.images_up[8]
			elif self.timer_up == 42:
				self.image = self.images_up[7]
			elif self.timer_up == 36:
				self.image = self.images_up[6]
			elif self.timer_up == 30:
				self.image = self.images_up[5]
			elif self.timer_up == 24:
				self.image = self.images_up[4]
			elif self.timer_up == 18:
				self.image = self.images_up[3]
			elif self.timer_up == 12:
				self.image = self.images_up[2]
			elif self.timer_up == 6:
				self.image = self.images_up[1]
			elif self.timer_up == 0:
				self.image = self.images_up[0]
			self.timer_up += 1
		if keystate[pygame.K_s]:
			self.speedy = self.playerSpeed
			if self.timer_down == 60:
				self.image = self.images_down[10]
				self.timer_down = 0
			elif self.timer_down == 54:
				self.image = self.images_down[9]
			elif self.timer_down == 48:
				self.image = self.images_down[8]
			elif self.timer_down == 42:
				self.image = self.images_down[7]
			elif self.timer_down == 36:
				self.image = self.images_down[6]
			elif self.timer_down == 30:
				self.image = self.images_down[5]
			elif self.timer_down == 24:
				self.image = self.images_down[4]
			elif self.timer_down == 18:
				self.image = self.images_down[3]
			elif self.timer_down == 12:
				self.image = self.images_down[2]
			elif self.timer_down == 6:
				self.image = self.images_down[1]
			elif self.timer_down == 0:
				self.image = self.images_down[0]
			self.timer_down += 1

		self.rect.x += self.speedx
		self.rect.y += self.speedy

		# Prevents player from going off the screen
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
		if self.rect.top < 0:
			self.rect.top = 0
