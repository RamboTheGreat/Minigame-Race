import pygame, colors, time


class Popobject(pygame.sprite.Sprite):
	# Initializes the object as a sprite. Sets the
	# initial speed, and location of the balloon
	def __init__(self, x, y, speedy, speedx, select, side):
		pygame.sprite.Sprite.__init__(self)
		self.images = [pygame.image.load("Balloons/balloon1.png")]
		self.images_end = [pygame.image.load("Balloons/balloon1pop.png")]
		self.image = self.images[select]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.Objspeedy = speedy
		self.Objspeedx = speedx
		self.side = side
	def update(self, HEIGHT, WIDTH, group):
		self.speedy = self.Objspeedy
		self.speedx = self.Objspeedx
		# Moves balloon across screen depending where 
		# it spawned and their directions
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
		# Detects if balloon has gone off screen
		if (self.rect.y > HEIGHT or self.rect.y < 0 or
			self.rect.x > WIDTH or self.rect.x < 0):
			group.remove(self)