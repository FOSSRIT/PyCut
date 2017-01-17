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
        self.flip = False
        self.setLocation(180, 100)
        self.width = self.background.get_width()
        self.height = self.background.get_height()
        self.drawing = None
        self.draw()

    """
        update the text drawing surface.
    """
    def draw(self):
        self.drawing = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.flip:
            self.drawing.blit(pygame.transform.flip(self.background, True, False), (0,0))
        else:
            self.drawing.blit(self.background, (0,0))
        x = self.width * 0.05
        y = self.height - 62
        limit = len(self.messages)
        for i in xrange(limit):
            self.drawing.blit(self.messages[limit-i-1], (x, y))
            y -= self.messages[limit-i-1].get_height()
        self.dirty = False


    """
        draw on a surface
    """
    def drawOn(self, screen=None):
        if screen:
            if self.dirty:
                self.draw()
            screen.blit(self.drawing, self.location)
        else:
            print("Error: drawOn was called on Text object but no screen argument was passed")

    """
    change the font size
    """
    def setPen(self, font):
        self.pen = font
        self.dirty = True

    """
    change the color
    """
    def setColor(self, color=(0, 128, 0)):
        self.color = color
        self.dirty = True

    """
    x,y are the center points of the text.
    """
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.location = (x, y)
        
    def setScale(self, width, height):
        self.background = pygame.transform.scale(self.background, (width, height))
        self.width = self.background.get_width()
        self.height = self.background.get_height()
        self.dirty = True

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
        self.dirty = True

    """
    clear message from message bubble.
    """
    def clearMessages(self):
        self.messages = []
        self.dirty = True
