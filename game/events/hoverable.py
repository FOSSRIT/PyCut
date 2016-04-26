import pygame
from game.objects import STATE

class Hoverable():
    """docstring for Hoverable

        For hoverables on use the isHovered(event) method in cases where you
        are expecting a hover. Otherwise it will hover with default configs
        unless overriden.
    """
    def __init__(self):
        self.state = STATE.NORMAL
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
            self.state = STATE.HOVER
            if self.onHover:
                self.onHover()
        else:
            self.mousein = False
            self.mouseout = True
            self.state = STATE.NORMAL

    def inRange(self, x, y):
        if ((self.x <= x <= (self.x + self.width)) and
            (self.y <= y <= (self.y + self.height))):
            return True
        else:
            return False

    def setOnHover(self, func):
        self.onHover = func
