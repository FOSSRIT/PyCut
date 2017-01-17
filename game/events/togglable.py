import pygame
from game.objects import STATE

class Togglable():
    """docstring for Clickable
        TODO: modify to handle clicked vs released
    """
    def __init__(self):
        self.setState(STATE.NORMAL)
        self.location = (0,0)
        self.width = 0
        self.height = 0
        self.onSelect = None #name of function to call when left clicking        
        self.onDeselect = None #name of function to call when left clicking

        self.initiated = False #mouse pressed
        self.engaged = False #mouse released
        self.dirty = True;

    def isClicked(self, event):
        if self.inRange(event.pos[0], event.pos[1]):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.initiated = True
            if self.initiated and (event.type == pygame.MOUSEBUTTONUP):
                self.engaged = True
        else: #when click or release is detected outside of range make sure this is still not initiated
            self.initiated = False

        if self.engaged:
            if self.state is STATE.ACTIVE:
                self.deselect()
            else: 
                self.select()
            self.initiated = False
            self.engaged = False

    def inRange(self, x, y):
        if ((self.x <= x <= (self.x + self.width)) and
            (self.y <= y <= (self.y + self.height))):
            return True
        else:
            return False
        
    def select(self):
        if self.state is STATE.NORMAL:
                self.setState(STATE.ACTIVE)
                if self.onSelect:
                    self.onSelect()
                    
    def deselect(self):
        if self.state is STATE.ACTIVE:
                self.setState(STATE.NORMAL)
                if self.onDeselect:
                    self.onDeselect()

    def setOnSelect(self, func):
        self.onSelect = func
        
    def setOnDeselect(self, func):
        self.onDeselect = func
        
    def setState(self, state):
        self.state = state
        self.dirty = True
