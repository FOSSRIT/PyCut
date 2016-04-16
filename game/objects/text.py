import pygame

class Text():
    """docstring for Text"""
    def __init__(self, context, text):
        self.context = context
        self.text = text
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
        update the text drawing surface.
    """
    def draw(self):
        self.drawing = self.pen.render(self.text, True, self.color)
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
            print("Error: drawOn was called on Text object but no screen argument was passed")

    """
    change the font size
    """
    def setPen(self, font):
        self.pen = font
        self.draw()

    """
    change the color
    """
    def setColor(self, color=(0, 128, 0)):
        self.color = color
        self.draw()

    """
    x,y are the center points of the text.
    """
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.location = (x, y)
