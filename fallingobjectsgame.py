import pygame, colors, fallingplayer, fallingobjects, random, time, timer, draw


# Detects if player collides with enemy objects
def collisions(falling, player, player1, screen, WIDTH, HEIGHT):
	if (pygame.sprite.groupcollide(player, falling, False, True)):
		# Reset and display a lose message
		player1.score = 0
		draw.drawlose(falling, screen, WIDTH, HEIGHT)

def falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, mode):
	FPS = 60
	# Initializing groups
	player1 = fallingplayer.player(WIDTH,HEIGHT)
	all_players = pygame.sprite.Group()
	all_players.add(player1)
	all_falling = pygame.sprite.Group()
	fallingobj1 = fallingobjects.Fallingobjects(WIDTH, 5, random.randint(0, WIDTH), random.randint(0,1))
	all_falling.add(fallingobj1)

	# Loads the background
	background = pygame.image.load("backgrounds/fallingbackground.png")
	draw.info(screen, WIDTH, HEIGHT, 'Score 50 to Move on', 100)  # Displays the game info

	# Main game loop
	runnning = True
	while runnning:
		clock.tick(FPS)
		# Detects if player closes the window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
		# Randomly spawn a falling object, more objects spawn as player score increases
		if (random.randrange(0, 100) < difficulty + (player1.score/10)):
			newfallingobj = fallingobjects.Fallingobjects(WIDTH,
				random.randint(2,round(difficulty+player1.score/10)), random.randint(0, WIDTH), random.randint(0,2))
			all_falling.add(newfallingobj)
		# Displays background
		screen.fill(colors.black)
		screen.blit(background, (0,0))
		collisions(all_falling, all_players, player1, screen, WIDTH, HEIGHT)
		# Updates the objects and players
		all_falling.update(5, HEIGHT, all_falling, player1)
		all_players.update(WIDTH, HEIGHT)
		# Displays player score
		draw.displayscore(screen, WIDTH, HEIGHT, player1.score)
		# Draw sprites to the screen
		all_falling.draw(screen)
		all_players.draw(screen)
		# Shows the total elapsed time
		draw.drawtime(timer1, screen)
		pygame.display.flip()
		# Detects end game
		if player1.score >= 50:
			running = False
			if mode:
				timer1.pause()
				draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
			else:
				draw.drawWin(screen, WIDTH, HEIGHT)
			break

def main():
	WIDTH = 800
	HEIGHT = 600
	difficulty = 6
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Fallin! Minigame Mode")
	clock = pygame.time.Clock()
	timer1 = timer.Timer()
	timer1.start()
	falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, True)

if __name__=="__main__":
	main()