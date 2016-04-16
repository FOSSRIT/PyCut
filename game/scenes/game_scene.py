import pygame
from . import SceneBase
from game.objects import Text, Button

class GameScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.quit_button = Button(self.context, "Quit")
        self.quit_button.setPen(self.context.font_small)
        self.quit_button.setColor((255, 0, 0))
        self.quit_button.setOnLeftClick(self.handleQuitButtonClick)
        self.quit_button.setOnHover(self.handleQuitButtonHover)
        self.quit_button.setLocation((self.context.width - self.quit_button.width) - 5,
                                      ((self.context.height - self.quit_button.height)) - 5 )

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.quit_button.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                self.quit_button.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                self.quit_button.isHovered(event)

    def Update(self):
        pass

    def Render(self):
        # The game scene is just a blank blue screen
        self.screen.fill((0, 0, 255))
        self.quit_button.drawOn(self.screen)

    """
    helper methods below this point
    """
    def handleQuitButtonHover(self):
        pass

    def handleQuitButtonClick(self):
        self.context.quit()
