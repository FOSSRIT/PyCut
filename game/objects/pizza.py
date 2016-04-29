import pygame
from pygame import gfxdraw
from .rangable import Rangable
from random import randint

class Pizza(Rangable):
    """docstring for Pizza"""
    def __init__(self, context):
        Rangable.__init__(self)
        self.context = context
        self.pizza = self.context.plain_pizza
        self.trashed = False
        self.perfected = False
        self.trashing = False
        self.trash_can = None
        self.trash_pos = None
        self.slices = None
        self.offset = randint(0,4)
        self.color=(0,0,0)
        self.x = 100
        self.y = 400 # 5=> margin between top and pizza
        self.location = (self.x,self.y)
        self.width = 150
        self.height = 150
        self.topings = []
        self.drawing = None
        self.draw()

    """
        update the button drawing surface.
    """
    def draw(self):
        S = 2 #speed towards trash can
        A = 9.8 #acceleration towards trash can
        if self.trashing:
            if self.touches(self.trash_can):
                self.trashed = True
                self.trashing = False
            else:
                self.setLocation(self.trash_pos[0] + 50, self.y + ((S)*A) )
        surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pizza_img = pygame.transform.scale(self.context.plain_pizza, (self.width, self.height))
        surf.blit(pizza_img, (0,0))
        pad = self.offset
        for toping in self.topings:
            pad += 5
            self.drawToping(surf, toping, pad)
        #gfxdraw.filled_ellipse(surf, self.width//2,self.height//2, self.width/2, self.height/2, (219,162,74))#pizza
        #pygame.draw.arc(surf, (225,216,0), [0, 0, self.width, self.height], 0, 360, 2)#crust
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

    """
        return topping drawing
    """
    def drawToping(self, surf, toping_img, pad=0):
        #needs serious refactoring
        toping_img = pygame.transform.scale(toping_img, (self.width/4, self.height/4))
        degree = 0
        #center portion
        surf.blit(toping_img, ( (surf.get_width()/2) - (toping_img.get_width()/2), (surf.get_height()/2) - (toping_img.get_height()/2)))
        #top portion
        w,h = (surf.get_width()/6) + pad, surf.get_height()/6
        surf.blit(toping_img, ( w, h ))
        surf.blit(toping_img, ( 3*w , h ))
        #bottom portion
        surf.blit(toping_img, ( w, 3*h ))
        surf.blit(toping_img, ( 3*w , 3*h ))

        degree += 45
        return surf

    """
        draw on a surface
    """
    def moveToTrash(self, trash_pos=None, trash_can=None):
        if trash_pos and trash_can:
            self.trash_pos = trash_pos
            self.trash_can = pygame.Rect((trash_pos[0], trash_pos[1]+self.height), (trash_can.get_width(), trash_can.get_height()))
            self.trashing = True
            self.setLocation(trash_pos[0] + 50, 200)
        else:
            print("Error: expected a trash_pos, trash_can got {}, {}".format(trash_pos, trash_can))
    """
        Add topping
    """
    def addTopping(topping):
        self.topings += [topping]

    """
        draw on a surface
    """
    def setPerfect():
        self.perfected = True

    """
    x,y are the center points of the text.
    """
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.location = (x, y)
