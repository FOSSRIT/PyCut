import pygame
from . import SceneBase, GameScene
from game.objects import Text

class TitleScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.start_button = None
        self.title = Text(self.context, self.context.title)
        self.title.setPen(self.context.font_large)
        self.r_1 = 15
        self.r_2 = 20
        self.r_3 = 80
        self.title.setLocation( (self.context.width - self.title.width) // 2,
                                (self.context.height - self.title.height) // 2)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene)

    def Update(self):
        pass

    def Render(self):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen.fill((255, 255, 255))
        self.title.drawOn(self.screen)
        #self.screen.blit(self.start_button.draw(),
        #        ( (self.context.width - self.start_button.width) // 2,
        #         ((self.context.height - self.start_button.height) + self.title.get_height()) // 2))
        #pygame.draw.rect(self.screen, (0, 100, 100), pygame.Rect(100, 100, 200, 200))
