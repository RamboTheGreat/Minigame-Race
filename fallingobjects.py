import pygame, colors, fallingplayer
class Fallingobjects(pygame.sprite.Sprite):
	# Initializes the object
	def __init__(self, WIDTH, ObjSpeed, startingpoint, sword):
		pygame.sprite.Sprite.__init__(self)
		self.images = [pygame.image.load("swords/sword1.png"),pygame.image.load("swords/sword2.png"),
		pygame.image.load("swords/sword3.png")]
		self.image = self.images[sword]
		self.rect = self.image.get_rect()
		self.speedy = 0
		self.rect.centerx = startingpoint
		self.rect.bottom = 0
		self.ObjSpeed = ObjSpeed
	def update(self, ObjSpeed, HEIGHT, group, player):
		# Makes the object move down each tick until it falls to the ground
		self.speedy = self.ObjSpeed
		self.rect.y += self.speedy
		# Object removes itself when it's a the bottom of the screen
		if self.rect.y > (HEIGHT - 30):
			group.remove(self)
			player.score += 1
