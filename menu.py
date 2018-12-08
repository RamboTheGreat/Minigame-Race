import pygame, colors, time

# This file contains material modified from
# https://gist.github.com/ohsqueezy/2802185
# Determines whether the player wants to play singleplayer,
# multiplayer or to exit. Returns the players selection


def menu(screen, WIDTH, HEIGHT):
    class Option:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())

        def get_color(self):
            if self.hovered:
                return colors.green
            else:
                return colors.white

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

    menu_font = pygame.font.SysFont('PressStart2P', 40)
    option1_width, option1_height = menu_font.size('SINGLEPLAYER')
    option2_width, option2_height = menu_font.size("MULTIPLAYER")
    option3_width, option3_height = menu_font.size("EXIT")
    options = [Option("SINGLEPLAYER", (145,
        ((HEIGHT - option1_height) / 2 - option2_height))),
        Option("MULTIPLAYER", (145, (HEIGHT - option2_height) / 2)),
        Option("EXIT", (145,
            ((HEIGHT - option3_height) / 2 + option2_height)))]
    while True:
        pygame.event.pump()
        screen.fill(colors.black)
        counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for option in options:
            if counter == 4:
                counter = 0
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                if pygame.mouse.get_pressed()[0]:
                    if counter == 0:
                        print("Single")
                        return False
                    if counter == 1:
                        print("MULTIPLAYER")
                        return True
                    if counter == 2:
                        print("EXIT")
                        pygame.quit()
            else:
                option.hovered = False
            counter += 1
            option.draw()
        pygame.display.update()


# Not used, was for an arduino part that didn't work
def choosePort(screen, WIDTH, HEIGHT):

    class Option:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())

        def get_color(self):
            if self.hovered:
                return colors.green
            else:
                return colors.white

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos
    menu_font = pygame.font.SysFont('PressStart2P', 40)
    option0_message = menu_font.render('CHOOSE YOUR PORT', False, colors.white)
    option0_width, option0_height = menu_font.size('CHOOSE YOUR PORT')
    option1_width, option1_height = menu_font.size('/dev/ttyACM0')
    option2_width, option2_height = menu_font.size("/dev/ttyACM1")
    option3_width, option3_height = menu_font.size("EXIT")
    options = [Option('/dev/ttyACM0', (145,
            ((HEIGHT - option1_height) / 2 - option2_height))),
            Option("/dev/ttyACM1", (145, (HEIGHT - option2_height) / 2)),
            Option("EXIT", (145,
                ((HEIGHT - option3_height) / 2 + option2_height)))]

    while True:
        pygame.event.pump()
        screen.fill(colors.black)
        screen.blit(option0_message, (145,
            ((HEIGHT - option0_height)/2 - option1_height * 2)))

        counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for option in options:
            if counter == 4:
                counter = 0
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                if pygame.mouse.get_pressed()[0]:
                    if counter == 0:
                        print("ttyACM0")
                        return False
                    if counter == 1:
                        print("ttyACM1")
                        return True
                    if counter == 2:
                        print("EXIT")
                        pygame.quit()
            else:
                option.hovered = False
            counter += 1
            option.draw()
        pygame.display.update()


# Before the game starts, checks if the player is ready
def checkPlayerReady(screen, WIDTH, HEIGHT):
    class Option:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())

        def get_color(self):
            if self.hovered:
                return colors.green
            else:
                return colors.white

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos
    menu_font = pygame.font.SysFont('PressStart2P', 40)
    option0_message = menu_font.render('Are You Ready?', False, colors.white)
    option0_width, option0_height = menu_font.size('Are You Ready?')
    option1_width, option1_height = menu_font.size('YES')
    option2_width, option2_height = menu_font.size("NO")
    option3_width, option3_height = menu_font.size("EXIT")
    options = [Option('YES', (145, (
        (HEIGHT - option1_height)/2 - option2_height))),
        Option("NO", (145, (HEIGHT - option2_height)/2)),
        Option("EXIT", (145, ((HEIGHT - option3_height)/2 + option2_height)))]

    while True:
        pygame.event.pump()
        screen.fill(colors.black)
        screen.blit(option0_message, (145,
            ((HEIGHT - option0_height)/2 - option1_height * 2)))

        counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for option in options:
            if counter == 4:
                counter = 0
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                if pygame.mouse.get_pressed()[0]:
                    if counter == 0:
                        print("Ready")
                        return True
                    if counter == 1:
                        print("Not Ready")
                        return False
                    if counter == 2:
                        print("EXIT")
                        pygame.quit()
            else:
                option.hovered = False
            counter += 1
            option.draw()
        pygame.display.update()


# Displays a list of all minigames
# Returns the chosen minigame
def minigamechooser(screen, WIDTH, HEIGHT):
    class Option:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())

        def get_color(self):
            if self.hovered:
                return colors.green
            else:
                return colors.white

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos
    menu_font = pygame.font.SysFont('PressStart2P', 40)
    option0_message = menu_font.render('Choose a game:', False, colors.white)
    option0_width, option0_height = menu_font.size('Choose a game:')
    option1_width, option1_height = menu_font.size('Dodge!')
    option2_width, option2_height = menu_font.size("Falling!")
    option3_width, option3_height = menu_font.size("Snake Evolved")
    option4_width, option4_height = menu_font.size("Catch")
    option5_width, option5_height = menu_font.size("Pop")
    option6_width, option6height = menu_font.size("None")
    option7_width, option7_height = menu_font.size("Back")
    options = [Option('Dodge!',
                    (145, ((HEIGHT - option1_height)/2 - 3*option2_height))),
                Option("Falling!",
                    (145, (HEIGHT - option2_height)/2 - 2*option2_height)),
                Option("Snake Evolved",
                    (145, ((HEIGHT - option3_height)/2 - option2_height))),
                Option("Catch",
                    (145, ((HEIGHT - option4_height)/2))),
                Option("Pop!",
                    (145, ((HEIGHT - option3_height)/2 + option2_height))),
                Option("Jump!",
                    (145, ((HEIGHT - option3_height)/2 + 2*option2_height))),
                Option("Back",
                    (145, ((HEIGHT - option3_height)/2 + 3*option2_height))),
                Option("Exit",
                    (145, ((HEIGHT - option3_height)/2 + 4*option2_height)))]
    time.sleep(.2)

    while True:
        pygame.event.pump()
        screen.fill(colors.black)
        screen.blit(option0_message,
            (145, ((HEIGHT - option0_height)/2 - option1_height * 4)))

        counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for option in options:
            if counter == 7:
                counter = 0
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                if pygame.mouse.get_pressed()[0]:
                    if counter == 0:
                        return 0
                    if counter == 1:
                        return 1
                    if counter == 2:
                        return 2
                    if counter == 3:
                        return 3
                    if counter == 4:
                        return 4
                    if counter == 5:
                        return 5
                    if counter == 6:
                        return 6
                    if counter == 7:
                        return 7

            else:
                option.hovered = False
            counter += 1
            option.draw()
        pygame.display.update()


# Displays if the player wants to play race mode
# or if the player wants to play a single minigame
def SinglePlayerMode(screen, WIDTH, HEIGHT):
    class Option:
        hovered = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())

        def get_color(self):
            if self.hovered:
                return colors.green
            else:
                return colors.white

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos
    menu_font = pygame.font.SysFont('PressStart2P', 40)
    option0_message = menu_font.render('Mode?', False, colors.white)
    option0_width, option0_height = menu_font.size('Mode?')
    option1_width, option1_height = menu_font.size('Race')
    option2_width, option2_height = menu_font.size("Minigames")
    option3_width, option3_height = menu_font.size("EXIT")
    options = [Option('Race', (145,
                    ((HEIGHT - option1_height)/2 - option2_height))),
            Option("Minigames", (145, (HEIGHT - option2_height)/2)),
            Option("EXIT",
                (145, ((HEIGHT - option3_height)/2 + option2_height)))]
    while True:
        pygame.event.pump()
        screen.fill(colors.black)
        screen.blit(option0_message,
            (145, ((HEIGHT - option0_height)/2 - option1_height * 2)))

        counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for option in options:
            if counter == 4:
                counter = 0
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                if pygame.mouse.get_pressed()[0]:
                    if counter == 0:
                        print("Race")
                        return True
                    if counter == 1:
                        print("Minigames")
                        return False
                    if counter == 2:
                        print("EXIT")
                        pygame.quit()
            else:
                option.hovered = False
            counter += 1
            option.draw()
        pygame.display.update()
