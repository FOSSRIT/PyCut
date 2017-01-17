import pygame
from . import SceneBase, GameScene, HelpScene, DifficultyScene
from game.objects import Text, Button, STATE

class TitleScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.createTitle()
        self.createStartButton()
        self.createDifficultyButton()
        self.createHowToButton()
        self.createScoreText()
        self.createDifficultyText()

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_button.isClicked(event)
                self.help_button.isClicked(event)
                self.difficulty_button.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                self.start_button.isClicked(event)
                self.help_button.isClicked(event)
                self.difficulty_button.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                self.start_button.isHovered(event)
                self.help_button.isHovered(event)
                self.difficulty_button.isHovered(event)

    def Update(self):
        pass

    def Render(self):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen.fill((255, 255, 255))
        self.title.drawOn(self.screen)
        self.start_button.drawOn(self.screen)
        self.help_button.drawOn(self.screen)
        self.difficulty_button.drawOn(self.screen)
        self.score_msg.drawOn(self.screen)
        self.difficulty_msg.drawOn(self.screen)
        #self.screen.blit(self.start_button.draw(),
        #        ( (self.context.width - self.start_button.width) // 2,
        #         ((self.context.height - self.start_button.height) + self.title.get_height()) // 2))
        #pygame.draw.rect(self.screen, (0, 100, 100), pygame.Rect(100, 100, 200, 200))

    def createTitle(self):
        self.title = Text(self.context, self.context.title)
        self.title.setColor((244, 101, 36))
        self.title.setPen(self.context.bold_font_large)
        self.title.centered = True
        self.title.setLocation( self.context.width / 2, 300 )

    def createStartButton(self):
        self.start_button = Button(self.context, "Play Game")
        self.start_button.setPen(self.context.font_small)
        self.start_button.setPen(self.context.font, STATE.HOVER)
        self.start_button.setOnLeftClick(self.handleStartButtonClick)
        self.start_button.setOnHover(self.handleStartButtonHover)
        self.start_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.start_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.start_button.setLocation((self.context.width - self.start_button.width) // 2,
                                      ((self.context.height - self.start_button.height) // 2) + self.title.height)

    def createDifficultyButton(self):
        self.difficulty_button = Button(self.context, "Select Difficulty")
        self.difficulty_button.setPen(self.context.font_small)
        self.difficulty_button.setPen(self.context.font, STATE.HOVER)
        self.difficulty_button.setOnLeftClick(self.handleDifficultyButtonClick)
        self.difficulty_button.setOnHover(self.handleDifficultyButtonHover)
        self.difficulty_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.difficulty_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.difficulty_button.setLocation((self.context.width - self.difficulty_button.width) // 2,
                                    ((self.context.height - self.difficulty_button.height) // 2) + self.title.height + self.start_button.height + 5)

    def createHowToButton(self):
        self.help_button = Button(self.context, "How To Play")
        self.help_button.setPen(self.context.font_small)
        self.help_button.setPen(self.context.font, STATE.HOVER)
        self.help_button.setOnLeftClick(self.handleHelpButtonClick)
        self.help_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.help_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.help_button.setLocation((self.context.width - self.help_button.width) // 2,
                                      ((self.context.height - self.help_button.height) // 2) + self.title.height + self.start_button.height + self.difficulty_button.height + 10 )

    def createScoreText(self):
        self.score_msg = Text(self.context, "Experience: {} Pizzas".format(self.context.total_good_pizza))
        self.score_msg.setPen(self.context.bold_font)
        self.score_msg.setColor((244, 101, 36))
        self.score_msg.setLocation((self.context.width - self.score_msg.width) // 2,
                                    ((self.context.height - self.score_msg.height) // 2) + self.title.height + self.start_button.height + self.help_button.height + self.difficulty_button.height+ 15)
    def createDifficultyText(self):
        self.difficulty_msg = Text(self.context, "Current Difficulty: " + self.context.difficulty)
        self.difficulty_msg.setPen(self.context.bold_font)
        self.difficulty_msg.setColor((244, 101, 36))
        self.difficulty_msg.setLocation((self.context.width - self.difficulty_msg.width) // 2,
                                    ((self.context.height - self.difficulty_msg.height) // 2) + self.title.height + self.start_button.height + self.help_button.height + self.difficulty_button.height + self.score_msg.height + 15)

    """
    helper methods below this point
    """
    def handleDifficultyButtonHover(self):
        pass

    def handleDifficultyButtonClick(self):
        self.SwitchToScene(DifficultyScene)

    def handleStartButtonHover(self):
        pass

    def handleStartButtonClick(self):
        self.SwitchToScene(GameScene)

    def handleHelpButtonClick(self):
        self.SwitchToScene(HelpScene)
