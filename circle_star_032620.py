import pygame
from pygame.locals import *
from math import pi,sin,cos

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)
GRAY = (200,200,200)

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

def convert(num, old_min, old_max, new_min, new_max):
    ratio = (new_max - new_min) / (old_max - old_min)
    return new_min + num * ratio

def circle_star(num,t):
    """Creates a circle of num circles, with dots
    rotating at t time"""
    global textsurface
    rad = 100
    R = 150 #radius of big circle
    ang = 2*pi/num
    _mouse = pygame.mouse.get_pos()
    m = 0.06#convert(_mouse[0],0,width,0,1)
    textsurface = myfont.render(str(round(m,2)),False,RED)
    point_list = []
    for i in range(num):
        this_pos = [int(width/2+R*cos(i*ang)),
                    int(height/2+R*sin(i*ang))]
        pygame.draw.circle(screen,GRAY,this_pos,rad,1)

    for i in range(2*num):
        this_pos = [int(width / 2 + R * cos(i * ang)),
                    int(height / 2 + R * sin(i * ang))]

        dot_pos = [int(this_pos[0] + rad*cos(t-m*i*(2*pi))),
                   int(this_pos[1] + rad*sin(t-m*i*(2*pi)))]
        point_list.append(dot_pos)
        pygame.draw.circle(screen,VIOLET,dot_pos,5)
    for i,pt in enumerate(point_list):
        if i == len(point_list)-1:
            pygame.draw.line(screen, VIOLET, pt, point_list[0])
        else:
            pygame.draw.line(screen,VIOLET,pt,point_list[i+1])


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
    screen.fill(WHITE)

    circle_star(25,counter/30)

    counter += 1
    #screen.blit(textsurface,(20,20))
    pygame.display.update()

    # for saving screenshots:
    #if counter %5 == 0:
    pygame.image.save(screen, 'circle_star{:4d}.png'.format(counter))
    clock.tick(FPS)
pygame.quit()