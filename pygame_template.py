import pygame
from pygame.locals import *

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width,height = 600,600

# set up display
pygame.init()

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Pygame Window') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count

# loop until user clicks the close button
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:  # if pygame window is closed by user
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if FPS == 60:
                    FPS = 300  #faster display
                else:
                    FPS = 60

    # fill the screen with background color
    screen.fill(CYAN)

    counter += 1

    pygame.display.update()

    # for saving screenshots:
    # if counter %5 == 0:
    # Capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()