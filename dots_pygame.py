import pygame
from pygame.locals import *
from math import pi,sin,cos

width = 600
height = 600

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)
PURPLE = (204, 0, 204)

size = (width, height)

# set up display
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Puzzle Solver')
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0

'''Bouncing balls sketch'''

NUM_BALLS = 30

ratio = 0

# loop until user clicks the close button
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:  # if pygame window is closed by user
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if FPS == 60:
                    FPS = 300  # faster
                else:
                    FPS = 60

    # fill the screen with background color
    screen.fill(BLACK)
    for i in range(NUM_DOTS):
        h,s,v,a = 10*i,100,100,0
        color = pygame.Color('red') #don't know why this step is needed.
        color.hsva = (h,s,v,a)
        rotation_angle = 2 * pi * i / NUM_DOTS
        ratio = pygame.mouse.get_pos()
        #print(ratio)
        xval = 100 + 100 * sin(counter / 15 + ratio[0]/width * i)
        pygame.draw.circle(screen,color,[int(width/2 + xval*cos(rotation_angle)),
                                          int(height/2 + xval*sin(rotation_angle))],10)

    counter += 1

    pygame.display.update()

    # if counter %5 == 0:
    # Capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()