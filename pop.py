import pygame, popobjects, player, random, colors, time, timer, os, draw

def collisions(falling, player, player1, screen, WIDTH, HEIGHT):
	# Detects if the user caught the balloon
	if (pygame.sprite.groupcollide(player, falling, False, True)):
		player1.score += 1


def falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, mode):
	FPS = 60

	# Loads the background
	background = pygame.image.load("backgrounds/popbackground.jpg")

	# Initializes player and balloon groups
	player1 = player.Player(WIDTH/2,HEIGHT/2, 0, 5)
	all_players = pygame.sprite.Group()
	all_players.add(player1)
	all_objects = pygame.sprite.Group()
	obj1 = popobjects.Popobject(0, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), random.randint(2,round(difficulty+player1.score/10)), 0, 1)
	all_objects.add(obj1)

	# Displays to the player what their objective is
	draw.info(screen, WIDTH, HEIGHT, 'Pop 5 Balloons in 10 Seconds', 75)
	# Variable to keep track of time limit
	start = 600
	runnning = True
	while runnning:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
		# Randomly spawns a balloon, if there are no balloons on the screen it will spawn one also
		if (random.randrange(0, 100) < 1.5-player1.score/100 or len(all_objects) == 0):
			comingfrom = random.randint(1,8)
			if comingfrom == 1:
				newobj = popobjects.Popobject(-1, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 1)
			elif comingfrom == 2:
				newobj = popobjects.Popobject(random.randint(0,WIDTH), -1, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 1)
			elif comingfrom == 3:
				newobj = popobjects.Popobject(random.randint(0,WIDTH), 601, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 3)
			elif comingfrom == 4:
				newobj = popobjects.Popobject(801, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 3)
			elif comingfrom == 5:
				newobj = popobjects.Popobject(-1, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 2)
			elif comingfrom == 6:
				newobj = popobjects.Popobject(random.randint(0,WIDTH), 601, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 2)
			elif comingfrom == 7:
				newobj = popobjects.Popobject(801, random.randint(0,HEIGHT), random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 4)
			elif comingfrom == 8:
				newobj = popobjects.Popobject(random.randint(0,WIDTH), -1, random.randint(2,round(difficulty+player1.score/10)), 
					random.randint(2,round(difficulty+player1.score/10)), random.randint(0,0), 4)				
			all_objects.add(newobj)
		# Draws the background
		screen.fill(colors.black)
		screen.blit(background, (0,0))
		# Detects collisions
		collisions(all_objects, all_players, player1, screen, WIDTH, HEIGHT)
		# Updates objects, dislay score and time
		all_objects.update(HEIGHT, WIDTH, all_objects)
		all_players.update(WIDTH, HEIGHT)
		draw.displayscore(screen, WIDTH, HEIGHT, player1.score)
		all_objects.draw(screen)
		all_players.draw(screen)
		draw.drawtime(timer1, screen)
		draw.drawremainingtime(start, screen)
		pygame.display.flip()
		# Detects if time limit is reached and resets the game if it has been
		if start < 0:
			start = 600
			draw.drawlosepop(all_objects, screen, WIDTH, HEIGHT, timer1)
			player1.score = 0
		# Detects if the player reached the score within the time limit
		if player1.score >= 5 and start > 0:
			running = False
			if mode:
				timer1.pause()
				draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
			else:
				draw.drawWin(screen, WIDTH, HEIGHT)
			break
		start -= 1

def main():
	# Driver for minigame mode
	WIDTH = 800
	HEIGHT = 600
	difficulty = 8
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pop! Minigame Mode")
	clock = pygame.time.Clock()
	timer1 = timer.Timer()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	timer1.start()
	falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, True)

if __name__=="__main__":
	main()