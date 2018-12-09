import pygame, colors, random, time, runclass, math, draw
from random import randint

def info(screen, WIDTH, HEIGHT):
	# displays the goal of the game with the desired font and pauses for 1.5 seconds before the game starts
	info_font  =  pygame.font.SysFont('Comic Sans MS', 100)
	info_message  =  info_font.render('Reach the other side', False, colors.white)
	info_width, info_height  =  info_font.size('Reach the other side')
	screen.fill(colors.black)
	screen.blit(info_message, ((WIDTH-info_width)/2, (HEIGHT - info_height)/2))
	pygame.display.flip()
	time.sleep(1.5)
def drawlose(screen, WIDTH, HEIGHT):
	# displays a mesage when an object is hit and pauses for 1.5 seconds before restarting the game
	lose_font  =  pygame.font.SysFont('Comic Sans MS', 100)
	lose_message  =  lose_font.render('OOPS! Try Again!', False, colors.white)
	lose_width, lose_height  =  lose_font.size('OOPS! Try Again!')
	screen.fill(colors.red)
	screen.blit(lose_message, ((WIDTH-lose_width)/2, (HEIGHT - lose_height)/2))
	pygame.display.flip()
	time.sleep(1.5)
def run(screen, WIDTH, HEIGHT, clock):
    FPS = 60

    # creates 6 objects to be avoided
    object = [0]*6

    #creates a player object and adds it to the sprite group
    player1 = runclass.player(WIDTH, HEIGHT)
    all_players = pygame.sprite.Group()
    all_players.add(player1)
    objectgroup = pygame.sprite.Group()

    # initializes each object's position
    for i in range(0,4):
        object[i] = runclass.object(WIDTH,HEIGHT)
        objectgroup.add(object[i])
    object[0].rect.y = HEIGHT-120
    object[0].rect.x = WIDTH/2
    object[0].speed = randint(20,30)
    for i in range (1,4):
        object[i].rect.y = object[i-1].rect.y-150
        object[i].rect.x = WIDTH/2
        object[i].speed = randint(20,30)
    info(screen, WIDTH, HEIGHT)
    running = True
	
    # gives parameters for how to move the player and each object. Also defines collisions and when the game is either won
    # or lost
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            player1.rect.x -= 8
        if keystate[pygame.K_w]:
            player1.rect.y -= 8
        if keystate[pygame.K_d]:
            player1.rect.x += 8
        if keystate[pygame.K_s]:
            player1.rect.y += 8
        for i in range(0,4):
            if object[i].rect.x >= WIDTH:
                object[i].rect.x = 0
            object[i].rect.x += object[i].speed
        if player1.rect.y <= 0:
            running = False
        for i in range(0,4):
            if abs(object[i].rect.x-player1.rect.x) <= 40 and abs(object[i].rect.y-player1.rect.y) <= 40:
                drawlose(screen, WIDTH, HEIGHT)
                player1.rect.x = WIDTH/2
                player1.rect.y = HEIGHT-40
        if player1.rect.x > WIDTH:
            player1.rect.x = 0
        if player1.rect.x < 0:
            player1.rect.x = WIDTH
        if player1.rect.y >= HEIGHT-40:
            player1.rect.y = HEIGHT-40
        screen.fill(colors.black)
        objectgroup.draw(screen)
        all_players.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    
    # sets the resolution of the game window and runs the game
    WIDTH = 800
    HEIGHT = 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    run(screen,WIDTH, HEIGHT, clock)
