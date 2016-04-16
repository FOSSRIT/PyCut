import pygame
from game.events import Clickable, Hoverable
class Button(Clickable, Hoverable):
    """docstring for Button"""
    def __init__(self, context, label=""):
        Clickable.__init__(self)
        Hoverable.__init__(self)
        self.context = context
        self.label = label
        self.color = (0, 128, 0)
        self.background_img = None
        self.background_color = None
        self.x = None
        self.y = None
        self.location = (0,0)
        self.width = None
        self.height = None
        self.pen = self.context.font
        self.drawing = None
        self.draw()

    """
        update the button drawing surface.
    """
    def draw(self):
        surf = None
        if self.width and self.height:
            surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            if self.background_img or self.background_color:
                #TODO Handle case where there is a background image or color
                pass
            else:
                text = self.pen.render(self.label, True, self.color)
                surf.blit(text, ((self.width - text.get_width()) // 2,
                             (self.height - text.get_height()) // 2 ))
        else:
            surf = self.pen.render(self.label, True, self.color)
        self.drawing = surf
        self.width = self.drawing.get_width()
        self.height = self.drawing.get_height()

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
    change the font size
    """
    def setPen(self, font):
        self.pen = font
        self.draw()

    """
    change the font size
    """
    def setSize(width, height):
        self.width = width
        self.height = height
        self.draw()

    """
    change the color
    """
    def setColor(self, color=(0, 128, 0)):
        self.color = color
        self.draw()

    """
    x,y are the center points of the button.
    """
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.location = (x, y)
