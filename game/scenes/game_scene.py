import pygame
from . import SceneBase
from game.objects import STATE, Text, Button, Pizza, MessageBubble

class GameScene(SceneBase):
    def __init__(self, context):
        SceneBase.__init__(self, context)
        self.buttons = []
        self.createGameMenu()
        self.createMessageBubble()
        self.buildPizzas()
        self.createToppingOptions()
        self.createTrashCan()
        self.addCookingButton()
        self.count = 0#for debugging

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    button.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    button.isHovered(event)

    def Update(self):
        self.count += 1
        self.message_bubble.addMessage( "Pizza #: {}".format(self.count))

    def Render(self):
        # The game scene is just a blank blue screen
        self.screen.fill((0, 0, 255))
        self.screen.blit(self.context.shop_background,(0,0))
        self.screen.blit(self.context.counter_top,(0,0))
        self.screen.blit(self.trashCan, (1000,600))
        self.message_bubble.drawOn(self.screen)
        for button in self.buttons:
            button.drawOn(self.screen)
        for pizza in self.pizzas:
            pizza.drawOn(self.screen)


    """
        Take care of element initialization and event handlers bellow
    """

    def createGameMenu(self):
        P, K = 300, 5
        currX = P
        self.quit_button = Button(self.context, "Quit")
        self.quit_button.setPen(self.context.font)
        self.quit_button.setColor((255, 255, 255))
        self.quit_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.quit_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.quit_button.setOnLeftClick(self.handleQuitButtonClick)
        self.quit_button.setOnHover(self.handleQuitButtonHover)
        self.quit_button.setLocation(P, 0)
        currX+= self.quit_button.width
        self.restart_button = Button(self.context, "Restart")
        self.restart_button.setPen(self.context.font)
        self.restart_button.setColor((255, 255, 255))
        self.restart_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.restart_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.restart_button.setOnLeftClick(self.handleRestartButtonClick)
        self.restart_button.setLocation(currX + K, 0)
        currX += self.restart_button.width + K
        self.home_button = Button(self.context, "Menu/Home")
        self.home_button.setPen(self.context.font)
        self.home_button.setColor((255, 255, 255))
        self.home_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.home_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.home_button.setOnLeftClick(self.handleHomeButtonClick)
        self.home_button.setLocation(currX + K, 0)
        self.buttons += [self.quit_button, self.restart_button, self.home_button]

    """
    helper methods below this point
    """
    def handleQuitButtonHover(self):
        pass

    def handleQuitButtonClick(self):
        self.context.quit()

    def handleRestartButtonClick(self):
        self.SwitchToScene(GameScene)

    def handleHomeButtonClick(self):
        self.SwitchToScene(self.context.starting_scene)

    def buildPizzas(self):
        self.pizzas = []
        Y = 0
        for i in xrange(0,5):
            pizza = Pizza(self.context)
            pizza.setLocation(140, 620-Y)
            Y+=5
            self.pizzas += [pizza]

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
        self.buttons += [self.cheeseBtn, self.mushroomBtn, self.pepperoniBtn, self.pineappleBtn]


    def addCookingButton(self):
        self.cook = Button(self.context, "Cook")
        self.cook.setLocation(120, 770)
        self.cook.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.cook.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.buttons += [self.cook]

    def createMessageBubble(self):
        self.message_bubble = MessageBubble(self.context)
        self.message_bubble.addMessage("I need a pizza")

    def createTrashCan(self):
        self.trashCan = self.context.trash_can_img
