import pygame
from pygame import gfxdraw
from .rangable import Rangable

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
        self.color=(0,0,0)
        self.x = 100
        self.y = 400 # 5=> margin between top and pizza
        self.location = (self.x,self.y)
        self.width = 150
        self.height = 150
        self.topics = []
        self.drawing = None
        self.draw()

    """
        update the button drawing surface.
    """
    def draw(self):
        S = 2 #speed towards trash can
        A = 9.8 #acceleration towards trash can
        surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pizza_img = pygame.transform.scale(self.context.plain_pizza, (self.width, self.height))
        if self.trashing:
            if self.touches(self.trash_can):
                self.trashed = True
                self.trashing = False
            else:
                self.setLocation(self.trash_pos[0] + 50, self.y + ((S)*A) )
        surf.blit(pizza_img, (0,0))
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
