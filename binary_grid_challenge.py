"""Annie Perkins Math Art Challenge
https://twitter.com/anniek_p/status/1244220881347502080
March 29, 2020"""

import pygame
from pygame.locals import *
import random

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width,height = 600,600

rows,cols = 30,30
offset1_list = [random.choice([0,1]) for i in range(rows)]
offset2_list = [random.choice([0,1]) for i in range(cols)]

print(offset1_list)
print(offset2_list)
length = width/rows

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

def draw_lines_row(y,offset):
    """draws lines every other square"""
    for c in range(0,cols,2):
        pygame.draw.line(screen,BLACK,[int(length*(c+offset)),int(y)],
                        [int(length*(c+1+offset)),int(y)],2)

def draw_lines_col(x,offset):
    """draws lines every other square"""
    for r in range(0,rows,2):
        pygame.draw.line(screen,BLACK,[x,int(length*(r+offset))],
                        [x,int(length*(r+1+offset))],2)



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

    idx = random.randint(0, rows - 1)
    if counter % 6 == 0:
        offset1_list[idx] = 1 - offset1_list[idx]
    if counter % 6 == 3:
        offset2_list[idx] = 1 - offset2_list[idx]

    for r in range(rows):
        for c in range(cols):
            draw_lines_row(c*length,offset1_list[c])
            draw_lines_col(r*length,offset2_list[r])

    counter += 1

    pygame.display.update()

    # for saving screenshots:
    # if counter %5 == 0:
    #pygame.image.save(screen,'Binary_Grid{}.png'.format(counter))
    clock.tick(FPS)
pygame.quit()