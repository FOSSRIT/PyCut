import pygame

class Rangable():
    """docstring for Clickable
        TODO: modify to handle clicked vs released
    """
    def __init__(self):
        self.x = None
        self.y = None
        self.width = 0
        self.height = 0

    def inRange(self, x, y):
        if not(self.x and self.y):
            return
        if ((self.x <= x <= (self.x + self.width)) and
            (self.y <= y <= (self.y + self.height))):
            return True
        else:
            return False

    def touches(self, rect):
        if not(self.x and self.y):
            return
        item = pygame.Rect((self.x, self.y), (self.width, self.height))
        if item.colliderect(rect):
            return True
        else:
            return False
