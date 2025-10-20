import pygame
import math

SIZE = 64
BORDER = 0.2

class WorldSprite:

    def __init__(self, id, image, edges=None):
        self.id = id
        self.image = pygame.image.load(image)
        # Store corner colors (NW, NE, SE, SW) as raw RGB tuples
        self.corners = self._corners_from_image(self.image)

    def _corners_from_image(self, surface):
        # Sample the color at each corner pixel and store as (R,G,B)
        w, h = surface.get_width(), surface.get_height()
        coords = {
            0: (0, 0),            # NW
            1: (w - 1, 0),        # NE
            2: (w - 1, h - 1),    # SE
            3: (0, h - 1),        # SW
        }
        def to_rgb(color):
            return (color[0], color[1], color[2])
        return {k: to_rgb(surface.get_at(pos)) for k, pos in coords.items()}

    def draw(self, screen, count, i, collapsed, pos):
        w = math.ceil(math.sqrt(count))
        x = math.floor(i % w)
        y = math.floor(i / w)
        offset = (0,0)
        if count == 1 and collapsed:
            out_img = pygame.transform.scale(self.image, (SIZE, SIZE))
        else:
            out_img = pygame.transform.scale(self.image, (SIZE / w * (1-BORDER), SIZE / w * (1 - BORDER)))
            offset = ( x * SIZE / w + 2 + SIZE / w * BORDER / 2, 2 + SIZE / w * BORDER / 2)    
        screen.blit(out_img, (pos[0] * SIZE + offset[0] , pos[1] * SIZE + y * SIZE / w + offset[1]))
