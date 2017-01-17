"""
Difficulty Scene Module
"""
import pygame
from game.objects import Text, Button, STATE
from . import SceneBase

class DifficultyScene(SceneBase):
    """
    DifficultyScene
    Presents user with a choice of difficulty and stores that in the game context
    Inherits from SceneBase
    """

    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.createTitle()
        self.createEasyButton()
        self.createAdvancedButton()

    def ProcessInput(self, events, pressed_keys):
        """
        Process Input from user
        Inherited from SceneBase
                Args:   self
                        events - list of pygame events
                        pressed_keys
        """

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.easy_button.isClicked(event)
                self.adv_button.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                self.easy_button.isClicked(event)
                self.adv_button.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                self.easy_button.isHovered(event)
                self.adv_button.isHovered(event)

    def Update(self):
        """
        Update loop
        inherited from SceneBase
        """
        pass

    def Render(self):
        """
        Draw loop
        inherited from SceneBase
        """

        # For the sake of brevity, the difficulty scene is a blank red screen
        self.screen.fill((255, 255, 255))
        self.title.drawOn(self.screen)
        self.easy_button.drawOn(self.screen)
        self.adv_button.drawOn(self.screen)

    def createTitle(self):
        """
        Create the title for this page
        """

        self.title = Text(self.context, "Choose Difficulty")
        self.title.setColor((244, 101, 36))
        self.title.setPen(self.context.bold_font_large)
        self.title.centered = True
        self.title.setLocation( self.context.width / 2, 300)

    def createEasyButton(self):
        """
        Create the easy button
        """

        self.easy_button = Button(self.context, "Easy")
        self.easy_button.setPen(self.context.font_small)
        self.easy_button.setPen(self.context.font, STATE.HOVER)
        self.easy_button.setOnLeftClick(self.handleEasyButtonClick)
        self.easy_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.easy_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.easy_button.setLocation((self.context.width - self.easy_button.width) // 2,
                                     ((self.context.height - self.easy_button.height) // 2)
                                     + self.title.height)

    def createAdvancedButton(self):
        """
        Create the advanced button
        """

        self.adv_button = Button(self.context, "Advanced")
        self.adv_button.setPen(self.context.font_small)
        self.adv_button.setPen(self.context.font, STATE.HOVER)
        self.adv_button.setOnLeftClick(self.handleAdvancedButtonClick)
        self.adv_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.adv_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.adv_button.setLocation((self.context.width - self.adv_button.width) // 2,
                                    ((self.context.height - self.adv_button.height) // 2)
                                    + self.title.height + self.easy_button.height + 5)

    """
    helper methods below this point
    """

    def handleEasyButtonClick(self):
        """
        Callback for the easy button press
        sets the context to easy and switches back to title scene
        """

        self.context.difficulty = "Easy"
        self.SwitchToScene(self.context.starting_scene)

    def handleAdvancedButtonClick(self):
        """
        Callback for the easy button press
        sets the context to easy and switches back to title scene
        """

        self.context.difficulty = "Advanced"
        self.SwitchToScene(self.context.starting_scene)
