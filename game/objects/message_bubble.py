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
        self.old_message_color = (0,0,0)
        self.leveling_up = False
        self.game_over = False
        self.background = self.context.message_bubble_img
        self.pen = self.context.bold_font
        self.messages = []
        self.x = 180
        self.y = 100
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
        x = 40
        y = self.height - 62
        limit = len(self.messages)
        for i in xrange(limit):
            self.drawing.blit(self.messages[limit-i-1], (x, y))
            y -= self.messages[limit-i-1].get_height()


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
    def addMessage(self, message=None, message_arr=None, color=None):
        old_messages = self.messages
        for msg in self.messages:
            arr = pygame.PixelArray(msg)
            arr.replace(self.color, self.old_message_color)
        if not(color):
            color = self.color
        if message:
            self.messages.append(self.pen.render(message, True, color))
        if message_arr:
            for msg in message_arr:
                self.messages.append(self.pen.render(msg, True, color))

    """
    clear message from message bubble.
    """
    def clearMessages(self):
        self.messages = []
