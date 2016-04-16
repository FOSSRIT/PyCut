import pygame

class Clickable():
    """docstring for Clickable
        TODO: modify to handle clicked vs released
    """
    def __init__(self):
        self.location = (0,0)
        self.width = 0
        self.height = 0
        self.onLeftClick = None #name of function to call when left clicking
        self.onRightClick = None #name of function to call when right clicking
        self.initiated = False #mouse pressed
        self.engaged = False #mouse released

    def isClicked(self, event):
        if self.inRange(event.pos[0], event.pos[1]):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.initiated = True
            if self.initiated and (event.type == pygame.MOUSEBUTTONUP):
                self.engaged = True
        else: #when click or release is detected outside of range make sure this is still not initiated
            self.initiated = False

        if self.engaged:
            if event.button == 1: # left click
                if self.onLeftClick:
                    self.onLeftClick()
            elif event.button == 3: # right click
                if self.onRightClick:
                    self.onRightClick()
            self.initiated = False
            self.engaged = False

    def inRange(self, x, y):
        if ((self.x <= x <= (self.x + self.width)) and
            (self.y <= y <= (self.y + self.width))):
            return True
        else:
            return False

    def setOnLeftClick(self, func):
        self.onLeftClick = func

    def setOnRightClick(self, func):
        self.onRightClick = func
