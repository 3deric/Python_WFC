import pygame
import math
import random

class WorldElement:

    def __init__(self, screen, elements, x,y):
        self.collapsed = False
        self.entropy = len(elements)
        self.pos = (x,y)
        self.screen = screen
        self.elements = elements
        self.neighbours = []

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def draw(self):
        i = 0
        for element in self.elements:
            if not element:
                return
            element.draw(self.screen, len(self.elements), i, self.collapsed, self.pos)
            i+=1

    def collapse(self):
        if self.collapsed:
            return
        self.collapsed = True
        self.elements = [self.elements[random.randrange(0, len(self.elements))]]
        self.entropy = 9999
        for i in range(4):
            temp = []
            if self.neighbours[i]:
                for element in self.neighbours[i].elements:
                    if not (element and self.elements[0]):
                        return
                    if self._is_compatible(self.elements[0], element, i):
                        temp.append(element)
                if not self.neighbours[i].collapsed:
                    if len(temp) == 0:
                        temp.append(None)
                    self.neighbours[i].elements = temp
                    self.neighbours[i].update()

    def update(self):
        if not self.collapsed:
            self.entropy = len(self.elements)
        if self.entropy == 0:
            print(f"Sprite {self.pos} has zero entropy, consider checking neighbour assignments!")

    def _is_compatible(self, src_tile, neighbor_tile, dir_index):
        allowed = src_tile.compat.get(dir_index)
        if isinstance(allowed, (list, set)):
            return neighbor_tile.id in allowed
