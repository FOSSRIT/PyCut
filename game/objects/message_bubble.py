import pygame
from game.events import Clickable, Hoverable
from . import STATE, STYLES_NAMES as SM

class MessageBubble(Hoverable):
    """docstring for Text"""
    def __init__(self, context):
        Hoverable.__init__(self)
        self.context = context
        self.state = STATE.NORMAL
        self.color = (30,144,255)
        self.background = self.context.message_bubble_img
        self.pen = self.context.font_small
        self.messages = []
        self.x = 180
        self.y = 60
        self.location = (self.x,self.y)
        self.width = self.background.get_width()
        self.height = self.background.get_height()
        self.drawing = None
        self.draw()

    """
        update the text drawing surface.
    """
    def draw(self):
        self.drawing = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.drawing.blit(self.background, (0,0))
        x = self.height - 60
        y = 40
        limit = len(self.messages)
        for i in xrange(limit):
            self.drawing.blit(self.messages[limit-i-1], (y, x))
            x -= self.messages[limit-i-1].get_height()


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

    """
    Add message to message bubble.
    """
    def addMessage(self,message, color=self.color):
        self.messages.append(self.pen.render(message, True, color))
