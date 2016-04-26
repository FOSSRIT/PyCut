import pygame
from . import SceneBase
from game.objects import STATE, Text, Button, Pizza, MessageBubble

class GameScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.createQuitButton()
        self.createMessageBubble()
        self.pizza = Pizza(self.context)
        self.createToppingOptions()
        self.count = 0

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.quit_button.isClicked(event)
                self.cheeseBtn.isClicked(event)
                self.mushroomBtn.isClicked(event)
                self.pepperoniBtn.isClicked(event)
                self.pineappleBtn.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                self.quit_button.isClicked(event)
                self.cheeseBtn.isClicked(event)
                self.mushroomBtn.isClicked(event)
                self.pepperoniBtn.isClicked(event)
                self.pineappleBtn.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                self.quit_button.isHovered(event)
                self.quit_button.isHovered(event)
                self.cheeseBtn.isHovered(event)
                self.mushroomBtn.isHovered(event)
                self.pepperoniBtn.isHovered(event)
                self.pineappleBtn.isHovered(event)

    def Update(self):
        self.count += 1
        self.message_bubble.addMessage( "Pizza #: {}".format(self.count))

    def Render(self):
        # The game scene is just a blank blue screen
        self.screen.fill((0, 0, 255))
        self.screen.blit(self.context.shop_background,(0,0))
        self.screen.blit(self.context.counter_top,(0,0))
        self.quit_button.setLocation(50, 50)
        self.quit_button.drawOn(self.screen)
        self.message_bubble.drawOn(self.screen)
        self.pizza.drawOn(self.screen)
        self.cheeseBtn.drawOn(self.screen)
        self.mushroomBtn.drawOn(self.screen)
        self.pepperoniBtn.drawOn(self.screen)
        self.pineappleBtn.drawOn(self.screen)


    """
        Take care of element initialization and event handlers bellow
    """

    def createQuitButton(self):
        self.quit_button = Button(self.context, "Quit")
        self.quit_button.setPen(self.context.font_small)
        self.quit_button.setColor((255, 255, 255))
        self.quit_button.setOnLeftClick(self.handleQuitButtonClick)
        self.quit_button.setOnHover(self.handleQuitButtonHover)
        self.quit_button.setLocation((self.context.width - self.quit_button.width) - 5,
                                      ((self.context.height - self.quit_button.height)) - 5 )
    """
    helper methods below this point
    """
    def handleQuitButtonHover(self):
        pass

    def handleQuitButtonClick(self):
        self.context.quit()

    def createToppingOptions(self):
        X = 600
        Y = 650
        K = 10
        self.cheeseBtn = Button(self.context, "Cheese")
        self.cheeseBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.cheeseBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.cheeseBtn.setLocation(X, Y)
        self.mushroomBtn = Button(self.context, "Mushroom")
        self.mushroomBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.mushroomBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.mushroomBtn.setLocation(X, Y + self.cheeseBtn.height + K)
        self.pepperoniBtn = Button(self.context, "Pepperoni")
        self.pepperoniBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.pepperoniBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.pepperoniBtn.setLocation(X + self.cheeseBtn.width + K, Y)
        self.pineappleBtn = Button(self.context, "Pineapple")
        self.pineappleBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.pineappleBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.pineappleBtn.setLocation(X + self.mushroomBtn.width + K, Y + self.pepperoniBtn.height + K)


    def createMessageBubble(self):
        self.message_bubble = MessageBubble(self.context)
        self.message_bubble.addMessage("I need a pizza")
