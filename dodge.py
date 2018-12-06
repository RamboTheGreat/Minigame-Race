import pygame, objectsfordodge, player, random, colors, time, timer, os, draw

# Detects if objects hit the player, if it does, game resets
def collisions(falling, player, player1, screen, WIDTH, HEIGHT):
	if (pygame.sprite.groupcollide(player, falling, False, True)):
		player1.score = 0
		draw.drawlose(falling, screen, WIDTH, HEIGHT)
		player1.rect.centerx = (WIDTH/2)
		player1.bottom = (HEIGHT/2)

def falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, mode):
	FPS = 60

	# Sets the player and enemy sprite groups
	player1 = player.Player(WIDTH/2,HEIGHT/2, 0, 7)
	all_players = pygame.sprite.Group()
	all_players.add(player1)
	all_objects = pygame.sprite.Group()
	obj1 = objectsfordodge.Object(0, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), random.randint(2,round(difficulty+player1.score/10)), 0, 1)
	all_objects.add(obj1)

	# Loads the background
	background = pygame.image.load("backgrounds/dodgebackground.jpg")
	# Displays the info on what to do to the player
	draw.info(screen, WIDTH, HEIGHT, 'Score 50 to Move on', 100)
	# Main loop
	runnning = True
	while runnning:
		clock.tick(FPS)
		# Detects if player has closed the window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
		# Randomly spawns objects around the screen
		if (random.randrange(0, 100) < difficulty + (player1.score/10)):
			comingfrom = random.randint(1,8)
			if comingfrom == 1:
				newobj = objectsfordodge.Object(-1, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 1)
			elif comingfrom == 2:
				newobj = objectsfordodge.Object(random.randint(0,WIDTH), -1, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 1)
			elif comingfrom == 3:
				newobj = objectsfordodge.Object(random.randint(0,WIDTH), 601, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 3)
			elif comingfrom == 4:
				newobj = objectsfordodge.Object(801, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 3)
			elif comingfrom == 5:
				newobj = objectsfordodge.Object(-1, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 2)
			elif comingfrom == 6:
				newobj = objectsfordodge.Object(random.randint(0,WIDTH), 601, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 2)
			elif comingfrom == 7:
				newobj = objectsfordodge.Object(801, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 4)
			elif comingfrom == 8:
				newobj = objectsfordodge.Object(random.randint(0,WIDTH), -1, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,5), 4)				
			# Adds object to the group if it spawns
			all_objects.add(newobj)
		# Detects collision
		collisions(all_objects, all_players, player1, screen, WIDTH, HEIGHT)
		# Updates of opbjects
		all_objects.update(HEIGHT, WIDTH, all_objects, player1)
		all_players.update(WIDTH, HEIGHT)
		screen.fill(colors.black)
		screen.blit(background, (0,0))
		draw.displayscore(screen, WIDTH, HEIGHT, player1.score)
		all_objects.draw(screen)
		all_players.draw(screen)
		draw.drawtime(timer1, screen)
		pygame.display.flip()
		# Checks for player win
		if player1.score == 50:
			running = False
			if mode:
				timer1.pause()
				draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
			else:
				draw.drawWin(screen, WIDTH, HEIGHT)
			break

def main():
	# Driver for Minigame mode
	WIDTH = 800
	HEIGHT = 600
	difficulty = 3.0
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Dodge! Minigame Mode")
	clock = pygame.time.Clock()
	timer1 = timer.Timer()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	timer1.start()
	falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, True)

if __name__=="__main__":
	main()