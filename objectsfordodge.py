import pygame, colors, time


class Object(pygame.sprite.Sprite):
	def __init__(self, x, y, speedy, speedx, select, side):
		pygame.sprite.Sprite.__init__(self)
		# Loads images of rocks
		self.images = [pygame.image.load("rocks/rock0.png"),
		pygame.image.load("rocks/rock1.png"),
		pygame.image.load("rocks/rock2.png"),
		pygame.image.load("rocks/rock3.png"),
		pygame.image.load("rocks/rock4.png"),
		pygame.image.load("rocks/rock5.png")]
		# Randomly selects a rock image
		self.image = self.images[select]
		self.rect = self.image.get_rect()
		# Sets initial location and speeds
		self.rect.x = x
		self.rect.y = y
		self.Objspeedy = speedy
		self.Objspeedx = speedx
		self.side = side


	def update(self, HEIGHT, WIDTH, group, player):
		self.speedy = self.Objspeedy
		self.speedx = self.Objspeedx
		# Determines where the rock is coming from
		# then makes it go across the screen
		if self.side == 1:
			self.rect.y += self.speedy
			self.rect.x += self.speedx
		if self.side == 2:
			self.rect.y -= self.speedy
			self.rect.x += self.speedx
		if self.side == 3:
			self.rect.y -= self.speedy
			self.rect.x -= self.speedx
		if self.side == 4:
			self.rect.y += self.speedy
			self.rect.x -= self.speedx
		# Detects and then removes the rock if 
		# it has gone past the screen
		if (self.rect.y > HEIGHT or self.rect.y < 0 or
			self.rect.x > WIDTH or self.rect.x < 0):
			group.remove(self)
			player.score += 1