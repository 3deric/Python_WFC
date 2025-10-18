import pygame
from operator import attrgetter
from worldElement import WorldElement as WE
from worldElement import WorldSprite as WS

WORLD_SIZE = 10
ELEMENTS = [
            WS(0,'img/tile_0000.png', [[5,13,14,15],[1,2,11],[7,11,13],[2,5,9,15]]),
            WS(1,'img/tile_0001.png', [[5,13.14,15],[1,2,11],[8,12,14],[0,1,10]]),
            WS(2,'img/tile_0002.png', [[5,14,15],[0,5,7,13],[9,10,15],[0,1,10]]),
            WS(3,'img/tile_0003.png', [[6,8,12],[14,15],[9,10,15],[6,7,12,8]]),
            WS(4,'img/tile_0004.png', [[6,8,12],[6,8,12],[7,11,13],[3,13,14]]),
            WS(5,'img/tile_0005.png', [[5,13,14,15],[0,5,7,13],[0,1,2,5],[2,5,9,15]]),
            WS(6,'img/tile_0006.png', [[1,6,8,10,11,12],[3,6,8,10,12],[3,4,6,8,12,14],[6,8,12]]),
            WS(7,'img/tile_0007.png', [[0,4,7],[3,6,8,10,12,13],[7,11,13],[2,5,9,15]]),
            WS(8,'img/tile_0008.png', [[1,6,8,10,11,12],[6,8,9,10,12],[4,6,8,12,14],[4,6,8,7,11,12]]),
            WS(9,'img/tile_0009.png', [[2,3,9],[0,5,7,13],[9,10,15],[4,6,7,8,11]]),
            WS(10,'img/tile_0010.png', [[2,3,9],[1,2,11],[6,7,8,12,14],[6,8,9,11,12]]),
            WS(11,'img/tile_0011.png', [[0,4,7],[3,6,8,10,12],[3,4,6,8,12,14],[1,10]]),
            WS(12,'img/tile_0012.png', [[6,8,10,11,12],[6,8,9,10,12],[4,6,8,12,14],[6,7,8,12]]),
            WS(13,'img/tile_0013.png', [[0,4,7],[4,14,15],[0,1,2,4,5],[2,5,7,9,15]]),
            WS(14,'img/tile_0014.png', [[1,6,8,10,11,12],[4,14,15],[0,1,2,5],[3,13,14]]),
            WS(15,'img/tile_0015.png', [[2,3,9],[0,5,7,13],[0,1,2,5],[3,13,14]])
            ]

auto_collapse_active = False
last_time = -1
auto_collapse_wait = 200

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
pygame.display.set_caption("Wave Function Collapse")
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


def auto_collapse():
    if auto_collapse_active != True:
        return
    current_time = pygame.time.get_ticks()
    global last_time
    if current_time - last_time >= auto_collapse_wait:
        last_time = current_time
        next = worldElements.index(min(worldElements, key=attrgetter('entropy')))
        worldElements[next].collapse()  
 

def collapse():
    global auto_collapse_active
    global last_time 
    last_time= pygame.time.get_ticks()
    next = worldElements.index(min(worldElements, key=attrgetter('entropy')))
    worldElements[next].collapse()  
    auto_collapse_active = True


def draw():
    screen.fill("black")
    for we in worldElements:
        we.draw()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                auto_collapse_active = bool(1 - int(auto_collapse_active))
    
    auto_collapse()

    draw()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()