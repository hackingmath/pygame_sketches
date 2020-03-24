import pygame
from pygame.locals import *
import random
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
vels = [-3,-2,-1,1,2,3,4]

class Ball(object):
    def __init__(self):
        self.x = random.randint(10, width)
        self.y = random.randint(10, height)
        self.sz = 20
        self.xvel = random.choice(vels)
        self.yvel = random.choice(vels)

    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        if self.x > width-self.sz/2 or self.x < self.sz/2:
            self.xvel *= -1
        if self.y > height-self.sz/2 or self.y < self.sz/2:
            self.yvel *= -1
        pygame.draw.circle(screen, WHITE, [self.x,self.y], self.sz)


ball_list = [Ball() for i in range(NUM_BALLS)]

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
    for ball in ball_list:
        ball.update()


    counter += 1

    pygame.display.update()

    # if counter %5 == 0:
    # Capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()