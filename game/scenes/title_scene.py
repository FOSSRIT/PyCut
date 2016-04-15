import pygame
from . import SceneBase, GameScene

class TitleScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.start_button = context.start_button

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene)

    def Update(self):
        pass

    def Render(self):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 100, 100), pygame.Rect(100, 100, 200, 200))
