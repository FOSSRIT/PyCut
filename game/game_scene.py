import pygame
import game

class GameScene(game.SceneBase):
    def __init__(self):
        game.SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
