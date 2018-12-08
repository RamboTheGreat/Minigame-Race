import pygame, colors, fallingplayer, catchobjects, random, time, timer, draw


#  Detects if the player catchs the falling object and then adds score
# if the player did catch it
def collisions(falling, bombs, player, player1, screen, WIDTH, HEIGHT):
    if (pygame.sprite.groupcollide(player, falling, False, True)):
        player1.score += 1
    if (pygame.sprite.groupcollide(player, bombs, False, True)):
        player1.score = 0
        draw.drawlose(falling, screen, WIDTH, HEIGHT)
        for i in bombs:
            bombs.remove(i)


def catch(screen, WIDTH, HEIGHT, clock, timer1, mode):
    FPS = 60

    # Initializes the player and falling objects
    # sprite groups
    player1 = fallingplayer.player(WIDTH, HEIGHT)
    all_players = pygame.sprite.Group()
    all_players.add(player1)
    all_falling = pygame.sprite.Group()
    fallingobj1 = catchobjects.Catchobjects(WIDTH, 10,
        random.randint(0, WIDTH), random.randint(0, 1))
    all_falling.add(fallingobj1)
    all_bombs = pygame.sprite.Group()
    bomb = catchobjects.Bomb(WIDTH, 10, random.randint(0, WIDTH))
    all_bombs.add(bomb)

    # Loads the background we are going to use
    background = pygame.image.load("backgrounds/catchbackground.png")
    # Calls the draw.info function which will display to the player information
    # on what to do to move on
    draw.info(screen, WIDTH, HEIGHT,
        'Catch 10 to Move on', 100)  # Displays the game info

    # Main loop that will run until the end
    runnning = True
    while runnning:
        # Sets the FPS
        clock.tick(FPS)
        # Detects if player hits X on the window
        # and then closes the game if they did
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Algorithm to randomly spawn an enemy
        if (random.randrange(0, 100) < 0.75):
            # If above is true, create a new object and add it to the group
            newfallingobj = catchobjects.Catchobjects(WIDTH,
                random.randint(10, 15), random.randint(0, WIDTH),
                    random.randint(0, 2))
            all_falling.add(newfallingobj)
        if (random.randrange(0, 100) < .10):
            newbomb = catchobjects.Bomb(WIDTH,
                random.randint(10, 20), random.randint(0, WIDTH))
            all_bombs.add(newbomb)
        # Calls the collision function to detects collision
        collisions(all_falling, all_bombs, all_players,
            player1, screen, WIDTH, HEIGHT)
        # Updates the player and falling object
        all_falling.update(5, HEIGHT, all_falling, player1)
        all_bombs.update(5, HEIGHT, all_bombs, player1)
        all_players.update(WIDTH, HEIGHT)
        # Sets the background
        screen.fill(colors.black)
        screen.blit(background, (0, 0))
        # Displays the score in top righ corners
        draw.displayscore(screen, WIDTH, HEIGHT, player1.score)
        # Once updated, draws sprite groups to the screen
        all_falling.draw(screen)
        all_players.draw(screen)
        all_bombs.draw(screen)
        # Displays total run time
        draw.drawtime(timer1, screen)
        # Flips the displays
        pygame.display.flip()
        # Detects if player has reached the score limit
        if player1.score >= 10:
            running = False
            if mode:  # Detects the mode program was started in
                timer1.pause()
                # Will tell the player they finished and displays
                # their time
                draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
            else:
                # Tells the player the beat the level
                draw.drawWin(screen, WIDTH, HEIGHT)
            break


def main():
    # Driver for minigame mode
    WIDTH = 800
    HEIGHT = 600
    difficulty = 6
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Catch - Minigame Mode")
    clock = pygame.time.Clock()
    timer1 = timer.Timer()
    timer1.start()
    catch(screen, WIDTH, HEIGHT, clock, timer1, True)

if __name__ == "__main__":
    main()
