import pygame
import math

SIZE = 64
BORDER = 0.2

class WorldSprite:

    def __init__(self,id, image, neighbours):
        self.id = id
        self.image = pygame.image.load(image)
        self.neighbours = neighbours
        
    def draw(self, screen, count, i, collapsed, pos):
        w = math.ceil(math.sqrt(count))
        x = math.floor(i % w)
        y = math.floor(i / w)
        offset = (0,0)
        if count == 1 and collapsed == True:
            out_img = pygame.transform.scale(self.image, (SIZE, SIZE))
        else:
            out_img = pygame.transform.scale(self.image, (SIZE / w * (1-BORDER), SIZE / w * (1 - BORDER)))
            offset = ( x * SIZE / w + 2 + SIZE / w * BORDER / 2, 2 + SIZE / w * BORDER / 2)    
        screen.blit(out_img, (pos[0] * SIZE + offset[0] , pos[1] * SIZE + y * SIZE / w + offset[1]))
