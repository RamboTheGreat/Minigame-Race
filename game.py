import pygame, colors, player, math, random, time, gamestations, minigames, serial, test
import fallingobjectsgame, serial, dodge, timer, os, snake, pop, catch
import draw, menu, sidescroll
from pygame.locals import *

# Draws all the gamestations at certain spots on the map
def drawGamestations():
    all_gamestations = pygame.sprite.Group()
    station = gamestations.Gamestations(40,40)
    all_gamestations.add(station)
    station = gamestations.Gamestations(365,40)
    all_gamestations.add(station)
    station = gamestations.Gamestations(680,40)
    all_gamestations.add(station)
    station = gamestations.Gamestations(40,480)
    all_gamestations.add(station)
    station = gamestations.Gamestations(365,480)
    all_gamestations.add(station)
    station = gamestations.Gamestations(680,480)
    all_gamestations.add(station)
    return all_gamestations

# Takes all the sprite groups and updates them
def updates(screen, all_players, all_gamestations, WIDTH, HEIGHT, background, player1):
    screen.blit(background, (0,0))
    all_players.draw(screen)
    all_gamestations.draw(screen)
    all_gamestations.update(player1, WIDTH, HEIGHT)
    all_players.update(WIDTH, HEIGHT)


# Detects collision between player and a gamestation and then chooses a game
def collision(player1, all_gamestations, screen, WIDTH, HEIGHT, clock, timer1):
    hit = pygame.sprite.spritecollide(player1, all_gamestations, True)
    global gamesplayed
    global gamechoice
    if hit:
        if gamechoice == 0:
            fallingobjectsgame.falling(screen, WIDTH, HEIGHT, clock, 6, timer1, False)
        elif gamechoice == 1:
            dodge.falling(screen, WIDTH, HEIGHT, clock, 3, timer1, False)
        elif gamechoice == 2:
            snake.Snake(screen, WIDTH, HEIGHT, clock, timer1, False)
        elif gamechoice == 3:
            difficulty = 15
            pop.falling(screen, WIDTH, HEIGHT, clock, difficulty, timer1, False)
        elif gamechoice == 4:
            catch.catch(screen, WIDTH, HEIGHT, clock, timer1, False)
        elif gamechoice ==5:
            sidescroll.side(screen, WIDTH, HEIGHT, clock, timer1, False)
        gamesplayed += 1
        gamechoice += 1
        player1.score += 1 #player score to send to arduino
        return gamesplayed

# Plays music
def music():
    pygame.mixer.music.load('soundtrack.wav')
    pygame.mixer.music.play(-1)

# In minigame mode, launchs each programs drivers
def runMinigame(choice):
    if choice == 0:
        dodge.main()
    elif choice == 1:
        fallingobjectsgame.main()
    elif choice == 2:
        snake.main()
    elif choice == 3:
        catch.main()
    elif choice == 4:
        pop.main()
    elif choice == 5:
        sidescroll.main()


def main():
    # Variable that controls if the welcome screen in shown
    global showTitle
    won = False
    quit = True
    WIDTH = 800
    HEIGHT = 600

    PLAYER_SIZE = 40
    PLAYER_SPEED = 5
    FPS = 60
    score = 0
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers the game screen

    # Sets up the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minigame Race")
    background = pygame.image.load("Background.png")
    # Instantiates a clock
    clock = pygame.time.Clock()


    running = True
    # Starts the music
    music()
    
    # Displays the welcome screen upon first launch
    if showTitle:
        draw.welcomeScreen(WIDTH, HEIGHT, screen)
    InMenu = True
    # Controls the whole menu
    while InMenu:
        mode = menu.menu(screen, WIDTH, HEIGHT)
        if (mode):
            time.sleep(.2)
            test.scoredisp('0')
            ready = menu.checkPlayerReady(screen, WIDTH, HEIGHT)
            time.sleep(.2)
            if ready:
                draw.countdown(screen, WIDTH, HEIGHT)
                InMenu = False
            else:
                continue
        else:
            time.sleep(.2)
            singlemode = menu.SinglePlayerMode(screen, WIDTH, HEIGHT)
            if singlemode:
                time.sleep(.2)
                ready = menu.checkPlayerReady(screen, WIDTH, HEIGHT)
                time.sleep(.2)
                if ready:
                    draw.countdown(screen, WIDTH, HEIGHT)
                    InMenu = False
                else:
                    continue
            else:
                choice = menu.minigamechooser(screen, WIDTH, HEIGHT)
                print(choice)
                if choice == 7:
                    running = False
                    quit = True
                elif choice == 6:
                    continue
                else:
                    runMinigame(choice)
                    running = False
                    quit = False

    # Initiates the player
    all_players = pygame.sprite.Group()
    player1 = player.Player(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SPEED)   
    all_players.add(player1)

    # Draws the gamestations
    all_gamestations = drawGamestations()
    
    # Instatiates and starts a timer
    timer1 = timer.Timer()
    timer1.start()
    while running:
        # Set the speed of the game
        clock.tick(FPS)
        
        # Detects exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    quit = False
                    showTitle = False
                    main()

        screen.fill(colors.black)
        # Calls update function to do updates
        updates(screen, all_players, all_gamestations, WIDTH, HEIGHT, background, player1)
        # Detects collision and determines the numbers of games played
        gamesplayed = collision(player1, all_gamestations, screen, WIDTH, HEIGHT, clock, timer1)
        draw.drawtime(timer1, screen)
        # This part runs only if in Multiplayer mode
        if mode:
            if score != player1.score:
                # Displays score to arduino
                test.scoredisp(player1.score)
                score = player1.score
        # Detects end game
        if gamesplayed == 6:
            draw.drawEnd(screen, WIDTH, HEIGHT, timer1)
            showTitle = False
            quit = False
            running = False
            main()
        if won == True:
            draw.drawlosegame(screen, WIDTH, HEIGHT)
            main()

        pygame.display.flip()
    if quit:
        pygame.quit()


gamechoice = 0
gamesplayed = 0
showTitle = True


if __name__=="__main__":
    main()
