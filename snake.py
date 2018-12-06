import pygame, colors, random, time, snakeclasses, timer, draw
from random import randint


def collision(x1,x2,y1,y2):
	# Detects collision
	if x1==x2 and y1==y2:
		return True
	else:
		return False

def enemyCollision(player, enemy):
	# Detect Collision
	if (pygame.sprite.groupcollide(player, enemy, False, False)):
		return True
def Snake(screen, WIDTH, HEIGHT, clock, timer1, mode):
	FPS = 60

	# Initializes the sprites
	all_players = pygame.sprite.Group()
	all_food = pygame.sprite.Group()
	all_bad = pygame.sprite.Group()
	foodobject = snakeclasses.food(randint(1,(WIDTH/40)-1)*40,randint(1,(HEIGHT/40)-1)*40)
	player1 = snakeclasses.player(WIDTH, HEIGHT)
	badobject = snakeclasses.bad(randint(1,(WIDTH/40)-1)*40,randint(1,(HEIGHT/40)-1)*40)
	all_bad.add(badobject)
	all_food.add(foodobject)
	all_players.add(player1)
	# Displays info to the player
	draw.info(screen, WIDTH, HEIGHT,'Score 5 to Move on', 100)
	running = True
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
		# Detects if player collides with the food
		if collision(player1.rect.x,foodobject.rect.x,player1.rect.y,foodobject.rect.y):
			generating = True
			# Ensures food doesn't spawn on the obstacle
			while generating:
				foodobject.rect.x = randint(1,WIDTH/40-1)*40
				foodobject.rect.y = randint(1,HEIGHT/40-1)*40
				for bad in all_bad:
					if bad.rect.x != foodobject.rect.x and bad.rect.y != foodobject.rect.y:
						generating = False
			badobject = snakeclasses.bad(randint(1, (WIDTH / 40)-1) * 40, randint(1, (HEIGHT / 40)-1) * 40)
			all_bad.add(badobject)
			player1.score += 1
		# Detects collision with the enemy
		if enemyCollision(all_players, all_bad):
			# Displays loose message then resets the game
			draw.drawlosegame(screen, WIDTH, HEIGHT)
			for i in all_bad:
				all_bad.remove(i)
			player1.score=0
			badobject.rect.x = randint(1, (WIDTH / 40) - 1) * 40
			badobject.rect.y = randint(1, (HEIGHT / 40) - 1) * 40
			while badobject.rect.x == foodobject.rect.x and badobject.rect.y == foodobject.rect.y:
				badobject.rect.x = randint(1, (WIDTH / 40) - 1) * 40
				badobject.rect.y = randint(1, (HEIGHT / 40) - 1) * 40
			all_bad.add(badobject)
		# Detects if player reached score limit
		if player1.score == 5:
			if mode: # If in minigame mode
				timer1.pause()
				draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
			else:
				draw.drawWin(screen, WIDTH, HEIGHT)
			break
		# Updates on the screen
		all_players.update(WIDTH,HEIGHT)
		screen.fill(colors.black)
		draw.displayscore(screen, WIDTH, HEIGHT, player1.score)
		all_players.draw(screen)
		all_food.draw(screen)
		all_bad.draw(screen)
		draw.drawtime(timer1, screen)
		pygame.display.flip()


def main():
	# Driver for minigame mode
	WIDTH = 800
	HEIGHT = 600
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Snake Evolved")
	clock = pygame.time.Clock()
	timer1 = timer.Timer()
	timer1.start()
	Snake(screen, WIDTH, HEIGHT, clock, timer1, True)

if __name__=="__main__":
	main()
