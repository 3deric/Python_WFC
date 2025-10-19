import pygame
from operator import attrgetter
from worldelement import WorldElement as WE
from worldsprite import WorldSprite as WS


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
            WS(10,'img/tile_0010.png', [[2,3,9],[1,2,11],[6,8,12,14],[6,8,9,11,12]]),
            WS(11,'img/tile_0011.png', [[0,4,7],[3,6,8,10,12],[3,4,6,8,12,14],[1,10]]),
            WS(12,'img/tile_0012.png', [[6,8,10,11,12],[6,8,9,10,12],[3,4,6,8,12,14],[6,7,8,12]]),
            WS(13,'img/tile_0013.png', [[0,4,7],[4,14,15],[0,1,2,4,5],[2,5,7,9,15]]),
            WS(14,'img/tile_0014.png', [[1,6,8,10,11,12],[4,14,15],[0,1,2,5],[3,13,14]]),
            WS(15,'img/tile_0015.png', [[2,3,9],[0,5,7,13],[0,1,2,5],[3,13,14]])
            ]


class WaveFunctionCollapse:

    def __init__(self):
        self.world_size = 10
        self.world_elements = []
        self.auto_collapse_active = False
        self.last_time = -1
        self.auto_collapse_wait = 50
        self.screen

        worldElements = []
        for y in range(self.world_size):
            for x in range(self.world_size):
                we = WE(self.screen, ELEMENTS.copy(), x, y)
                worldElements.append(we)
