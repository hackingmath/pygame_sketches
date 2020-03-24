import pygame
from pygame.locals import *
from math import pi,sin,cos,degrees,radians

# define constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

#variables for display screen
width,height = 600,600

# set up display
pygame.init()

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

#initialize display screen
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Pygame Window') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count

# loop until user clicks the close button
done = False

def draw_lines():
    global counter
    m = counter/2#pygame.mouse.get_pos()
    angle = 90 + m * 90/width  #angle of rotation for lines
    length = 5 #starting length of lines
    pos = [width/2.0,height/2.0] #starting position of lines
    for i in range(50):
        #calculate new position with r*cis(theta) idea
        newpos = [pos[0]+length*cos(radians(angle*i)), pos[1]+length*sin(radians(angle*i))]
        pygame.draw.line(screen,BLACK,pos,newpos,2) #draw line
        pos = newpos[::] #translate to new position
        length += 5 #make length go up by 5

### Display loop ###
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:  # if pygame window is closed by user
            done = True

    # fill the screen with background color
    screen.fill(WHITE)

    ###Code goes here ###
    draw_lines()

    #increment frame counter
    counter += 1

    #update the screen
    pygame.display.update()

    # for saving screenshots:
    # if counter %4 == 0:
    #     #Capture(screen, 'Rotating_Lines{}.png'.format(counter), (0, 0), (600, 600))
    #     pygame.image.save(screen,'Rotating_Lines{}.png'.format(counter))
    clock.tick(FPS)
pygame.quit()