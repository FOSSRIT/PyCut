import pygame
from pygame import gfxdraw
class Pizza():
    """docstring for Pizza"""
    def __init__(self, context):
        self.context = context
        self.pizza = self.context.plain_pizza
        self.slices = None
        self.color=(0,0,0)
        self.x = 120
        self.y = 500 - 5# 5=> margin between top and pizza
        self.location = (self.x,self.y)
        self.width = 100
        self.height = 100
        self.drawing = None
        self.draw()

    """
        update the button drawing surface.
    """
    def draw(self):
        surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        gfxdraw.filled_ellipse(surf, self.width//2,self.height//2, self.width/2, self.height/2, (219,162,74))#pizza
        pygame.draw.arc(surf, (225,216,0), [0, 0, self.width, self.height], 0, 360, 2)#crust
        #draw slices on here afterwards
        self.drawing = surf

    """
        draw on a surface
    """
    def drawOn(self, screen=None):
        if screen:
            self.draw()
            screen.blit(self.drawing, self.location)
        else:
            print("Error: drawOn was called on Button object but no screen argument was passed")
