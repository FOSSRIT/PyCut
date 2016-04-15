import pygame
import game

class GameScene(game.SceneBase):
    def __init__(self, context):
        game.SceneBase.__init__(self, context)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self):
        # The game scene is just a blank blue screen
        self.screen.fill((0, 0, 255))
