import pygame, colors, random, time, sideclass, draw, timer
from random import randint


def collision(player, enemy, player1, screen, WIDTH, HEIGHT):
    if (pygame.sprite.groupcollide(player, enemy, False, True)):
        draw.drawlose(enemy, screen, WIDTH, HEIGHT)
        player1.score = 0


def side(screen, WIDTH, HEIGHT, clock, timer1, mode):
    FPS = 60

    # Initializes the groups of objects
    player1 = sideclass.player(WIDTH, HEIGHT)
    all_players = pygame.sprite.Group()
    all_players.add(player1)
    all_enemy = pygame.sprite.Group()
    enemy1 = sideclass.Enemy(WIDTH, HEIGHT, 5)
    all_enemy.add(enemy1)
    # Loads 2 instances of the same background for scrolling
    background1 = pygame.image.load("backgrounds/jumpback.jpg")
    background2 = pygame.image.load("backgrounds/jumpback.jpg")
    # Displays info to the user playing the game
    draw.info(screen, WIDTH, HEIGHT, 'Score 15 to Move on', 100)
    running = True
    move1 = 800
    move2 = 0

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        # Draws the background
        screen.fill(colors.black)
        screen.blit(background1,(move1,0))
        screen.blit(background2,(move2,0))

        # Randomly spawns enemies
        if (random.randrange(0,100)<1 and len(all_enemy) < 2) or len(all_enemy) == 0:
            enemy = sideclass.Enemy(WIDTH, HEIGHT, random.randint(5,8))
            all_enemy.add(enemy)
        # Displays the timer and score
        draw.drawtime(timer1, screen)
        draw.displayscore(screen,WIDTH,HEIGHT, player1.score)
        # Updates player and enemies
        all_players.update(WIDTH, HEIGHT)
        all_enemy.update(all_enemy, player1)
        all_players.draw(screen)
        all_enemy.draw(screen)
        # Detects collision between enemies and players
        collision(all_players, all_enemy, player1, screen, WIDTH, HEIGHT)
        # Sees if the player has reached the limit
        if player1.score == 15:
            if mode: # If in minigame mode
                timer1.pause()
                draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
            else:
                draw.drawWin(screen, WIDTH, HEIGHT)
            break

        # Controls movement of the background to scroll
        move1 -= 1
        move2 -= 1
        if move2 == -800:
            move2 = 800
        if move1 == -800:
            move1 = 800
        pygame.display.flip()

def main():
    # Driver for minigame mode
    WIDTH = 800
    HEIGHT = 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jump! Minigame Mode")
    clock = pygame.time.Clock()
    timer1 = timer.Timer()
    timer1.start()
    side(screen, WIDTH, HEIGHT, clock, timer1, True)



if __name__=="__main__":
    main()
