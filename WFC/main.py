import pygame
from wavefunctioncollapse import WaveFunctionCollapse as WFC

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
pygame.display.set_caption("Wave Function Collapse")
running = True
dt = 0


wfc = WFC(10, screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wfc.set_collapse()

    screen.fill("black")
    wfc.auto_collapse()
    wfc.draw()
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()