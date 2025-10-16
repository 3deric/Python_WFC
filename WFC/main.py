# Example file showing a circle moving on screen
import pygame
from worldElement import WorldElement as WE
from worldElement import WorldSprite as WS

WORLD_SIZE = 10

ELEMENTS = [
            WS(0,'img/tile_0000.png', [[5,13,14,15],[1,2,11],[13,7],[5]]),
            WS(1,'img/tile_0001.png', [[5],[2],[8,12],[0]]),
            WS(2,'img/tile_0002.png', [[14,15],[5],[9,15],[0,1]]),
            WS(3,'img/tile_0003.png', [[6,8,12],[14,15],[9,15],[6,7,12,8]]),
            WS(4,'img/tile_0004.png', [[6,8,12],[6,8,12],[7,13],[13,14]]),
            WS(5,'img/tile_0005.png', [[5.14,15],[5,7,13],[1,5,2],[5,15]]),
            WS(6,'img/tile_0006.png', [[6,8,12],[6,8,12],[6,8,12],[6,8,12]]),
            WS(7,'img/tile_0007.png', [[4,7],[6,8,12],[7,11,13],[0,5,13]]),
            WS(8,'img/tile_0008.png', [[6,8,13],[6,8,13],[4,6,8,13],[6,8,13]]),
            WS(9,'img/tile_0009.png', [[9],[5,7],[9,10],[6,8,13]]),
            WS(10,'img/tile_0010.png', [[3,9],[1,11],[6,8,12],[6,8,11,12]]),
            WS(11,'img/tile_0011.png', [[4,7],[6,8,12],[6,8,12],[1,10]]),
            WS(12,'img/tile_0012.png', [[6,8,12,1],[1,6,8,12],[6,8,12,14],[6,7,8,12]]),
            WS(13,'img/tile_0013.png', [[7],[14],[0,1,2,5],[5,9]]),
            WS(14,'img/tile_0014.png', [[6,8,12],[15],[5],[13]]),
            WS(15,'img/tile_0015.png', [[2,9],[5],[5],[13.14]])
            ]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True
dt = 0

#init world elements
worldElements = []
for y in range(WORLD_SIZE):
    for x in range(WORLD_SIZE):
        we = WE(screen, ELEMENTS.copy(), x, y)
        worldElements.append(we)
#set world element neighbours

for we in worldElements:
    north = None
    east = None
    south = None
    west = None

    if we.pos[1] - 1 >= 0:
        north = worldElements[we.pos[0] + WORLD_SIZE * (we.pos[1]-1)]
    if we.pos[0] + 1 < WORLD_SIZE:
        east = worldElements[we.pos[0] + 1 + WORLD_SIZE * we.pos[1]]
    if we.pos[1] + 1 < WORLD_SIZE:
        south = worldElements[we.pos[0] + WORLD_SIZE * (we.pos[1]+1)]
    if we.pos[0] - 1 >= 0:
        west = worldElements[we.pos[0] - 1 + WORLD_SIZE * we.pos[1]]
    we.set_neighbours([north, east, south, west])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    for we in worldElements:
        we.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        worldElements[4].collapse()



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()