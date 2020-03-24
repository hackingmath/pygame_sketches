import pygame
from pygame.locals import *
from math import pi, sin, cos

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width, height = 600, 600

# set up display
pygame.init()

# in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Pygame Window')  # add your own caption!
FPS = 120  # frames per second
clock = pygame.time.Clock()

counter = 0  # frame count


def polygon(sides, center, phase, size, rot=0, shift=0):
    """Draws a triangle with given center and 'radius'"""
    angle = 2 * pi / sides
    point_list = [(center[0] + size * cos(i * angle + (rot + shift) / phase),
                   center[1] + size * sin(i * angle + (rot + shift) / phase)) for i in range(sides)]
    pygame.draw.lines(screen, VIOLET, True, point_list, 2)


def circle_of_tris(num_tris, radius, phase):
    """Draws a circle of triangles with given radius"""
    for n in range(num_tris):
        center_x, center_y = width / 2, height / 2
        polygon(3, (center_x + radius * cos(2 * pi * n / num_tris),
                    center_y + radius * sin(2 * pi * n / num_tris)), phase, 100, counter, n)


def convert(num, old_min, old_max, new_min, new_max):
    ratio = (new_max - new_min) / (old_max - old_min)
    return new_min + num * ratio


# loop until user clicks the close button
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:  # if pygame window is closed by user
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if FPS == 60:
                    FPS = 300  # faster display
                else:
                    FPS = 60

    # fill the screen with background color
    screen.fill(BLACK)

    counter += .005
    m = pygame.mouse.get_pos()
    phase = 0.434#convert(m[0],1,width,0,2)
    text1 = myfont.render(str(phase), True, GREEN)

    # polygon(3,(width/2,height/2),200,counter/100)
    circle_of_tris(90, 200, phase)
    #screen.blit(text1, (20, 20))
    pygame.display.update()

    # for saving screenshots:
    # if counter %5 == 0:
    # Capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()