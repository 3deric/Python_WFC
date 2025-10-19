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
            if element == None:
                return
            element.draw(self.screen, len(self.elements), i, self.collapsed, self.pos)
            i+=1

    def collapse(self):
        if self.collapsed == True:
            return
        self.collapsed = True
        self.elements = [self.elements[random.randrange(0, len(self.elements))]]
        self.entropy = 9999
        for i in range(4):
            temp = []
            if self.neighbours[i] != None:
                for element in self.neighbours[i].elements:
                    if element == None or self.elements[0] == None:
                        return
                    if element.id in self.elements[0].neighbours[i]:
                        temp.append(element)
                if self.neighbours[i].collapsed == False:
                    if len(temp) == 0:
                        temp.append(None)
                    self.neighbours[i].elements = temp
                    self.neighbours[i].update()

    def update(self):
        if self.collapsed == False:
            self.entropy = len(self.elements)
        if self.entropy == 0:
            print(f"Sprite {self.pos} has zero entropy, consider checking neighbour assignments!")


