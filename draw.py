import pygame, colors, time


''' Contains all the common messages
that are drawn to the screen for each mini game'''


def drawlose(falling, screen, WIDTH, HEIGHT):
    for i in falling:  # Removes all enemy objects
        falling.remove(i)
    # Draws to the screen a lose message
    lose_font = pygame.font.SysFont('Comic Sans MS', 100)
    lose_message = lose_font.render('OOPS! Try Again!', False, colors.white)
    lose_width, lose_height = lose_font.size('OOPS! Try Again!')
    screen.fill(colors.red)
    screen.blit(lose_message, ((WIDTH-lose_width)/2, (HEIGHT - lose_height)/2))
    pygame.display.flip()
    time.sleep(1.5)


# Same function as above, but specialized for the Pop! game
def drawlosepop(falling, screen, WIDTH, HEIGHT, timer1):
    for i in falling:
        falling.remove(i)
    lose_font = pygame.font.SysFont('Comic Sans MS', 100)
    lose_message = lose_font.render('OOPS! Try Again!', False, colors.white)
    lose_width, lose_height = lose_font.size('OOPS! Try Again!')
    screen.fill(colors.red)
    screen.blit(lose_message, ((WIDTH-lose_width)/2, (HEIGHT - lose_height)/2))
    pygame.display.flip()
    timer1.pause()
    time.sleep(1.5)
    timer1.start()


def drawEnd(screen, WIDTH, HEIGHT, timer1):
    win_font = pygame.font.SysFont('Comic Sans MS', 100)
    win_message = win_font.render('Finished!', False, colors.white)
    win_width, win_height = win_font.size('Finished!')
    screen.fill(colors.green)
    screen.blit(win_message, ((WIDTH-win_width)/2, (HEIGHT - win_height)/2))
    pygame.display.flip()
    time.sleep(1.5)
    win_font = pygame.font.SysFont('Comic Sans MS', 100)
    win_message = win_font.render(str(round(timer1.get_elapsed(), 2)),
        False, colors.white)
    win_width, win_height = win_font.size(str(round(timer1.get_elapsed(), 2)))
    win1_message = win_font.render("Time:", False, colors.white)
    win1_width, win1_height = win_font.size("Time:")
    screen.fill(colors.green)
    screen.blit(win1_message, ((WIDTH-win1_width)/2,
        (HEIGHT - win1_height)/2 - win_height))
    screen.blit(win_message, ((WIDTH-win_width)/2, (HEIGHT - win_height)/2))
    pygame.display.set_caption("Minigame Race")
    pygame.display.flip()
    time.sleep(1.5)


def drawWin(screen, WIDTH, HEIGHT):
    win_font = pygame.font.SysFont('Comic Sans MS', 100)
    win_message = win_font.render('Good Job!', False, colors.white)
    win_width, win_height = win_font.size('Good Job!')
    screen.fill(colors.green)
    screen.blit(win_message, ((WIDTH-win_width)/2, (HEIGHT - win_height)/2))
    pygame.display.flip()
    time.sleep(1.5)


def drawtime(timer1, screen):
    time_font = pygame.font.SysFont('PressStart2P', 25)
    time_message = time_font.render(str(round(timer1.get_elapsed(), 2)),
        False, colors.white)
    time_width, time_height = time_font.size(
        str(round(timer1.get_elapsed(), 2)))
    screen.blit(time_message, (3, 0))


def displayscore(screen, WIDTH, HEIGHT, score):
    score_font = pygame.font.SysFont('PressStart2P', 25)
    score_message = score_font.render('Score: ' + str(score),
        False, colors.white)
    score_width, score_height = score_font.size('Score: ' + str(score))
    screen.blit(score_message, (WIDTH - score_width - 5, 0))


def countdown(screen, WIDTH, HEIGHT):
    counter = 3
    for i in range(3):
        count_font = pygame.font.SysFont('Comic Sans MS', 400)
        count_message = count_font.render(str(counter), False, colors.white)
        count_rect = count_message.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.fill(colors.green)
        screen.blit(count_message, count_rect)
        pygame.display.flip()
        time.sleep(1.0)
        counter -= 1


def welcomeScreen(WIDTH, HEIGHT, screen):
    welcome_font = pygame.font.SysFont('PressStart2P', 34)
    welcome1_message = welcome_font.render('Welcome to', False, colors.white)
    welcome1_width, welcome1_height = welcome_font.size('Welcome to')
    screen.fill(colors.black)
    screen.blit(welcome1_message, ((WIDTH-welcome1_width)/2,
        (HEIGHT - welcome1_height)/2 - welcome1_height))
    welcome2_message = welcome_font.render('Minigame Race',
        False, colors.white)
    welcome2_width, welcome2_height = welcome_font.size('Minigame Race')
    screen.blit(welcome2_message, ((WIDTH-welcome2_width)/2,
        (HEIGHT - welcome2_height)/2 + welcome2_height))
    pygame.display.flip()
    time.sleep(2)


def drawlosegame(screen, WIDTH, HEIGHT):
    lose_font = pygame.font.SysFont('Comic Sans MS', 100)
    lose_message = lose_font.render('OOPS! Try Again!', False, colors.white)
    lose_width, lose_height = lose_font.size('OOPS! Try Again!')
    screen.fill(colors.red)
    screen.blit(lose_message, ((WIDTH-lose_width)/2, (HEIGHT - lose_height)/2))
    pygame.display.flip()
    time.sleep(1.5)


def info(screen, WIDTH, HEIGHT, message, size):
    info_font = pygame.font.SysFont('Comic Sans MS', size)
    info_message = info_font.render(message, False, colors.white)
    info_width, info_height = info_font.size(message)
    screen.fill(colors.black)
    screen.blit(info_message, ((WIDTH-info_width)/2, (HEIGHT - info_height)/2))
    pygame.display.flip()
    time.sleep(1.5)


def drawremainingtime(start, screen):
    time_font = pygame.font.SysFont('PressStart2P', 25)
    time_message = time_font.render(str(round(start/60, 2)),
        False, colors.white)
    time_width, time_height = time_font.size(str(round(start/60, 2)))
    screen.blit(time_message, (350, 0))
