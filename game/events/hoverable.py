import pygame

class Hoverable():
    """docstring for Hoverable"""
    def __init__(self):
        self.location = (0,0)
        self.width = 0
        self.height = 0
        self.onHover = None #name of function to call when being hovered over
        self.mousein = False
        self.mouseout = False

    def isHovered(self, event):
        if self.inRange(event.pos[0], event.pos[1]):
            self.mouseout = False
            self.mousein = True
            if self.onHover:
                self.onHover()
        else:
            self.mousein = False
            self.mouseout = True

    def inRange(self, x, y):
        if ((self.x <= x <= (self.x + self.width)) and
            (self.y <= y <= (self.y + self.width))):
            return True
        else:
            return False

    def setOnHover(self, func):
        self.onHover = func
