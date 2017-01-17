"""
Game Scene Module
"""
import random
import pygame
from game.objects import STATE, Text, Button, Pizza, MessageBubble, Toggle
from . import SceneBase
import cProfile

class GameScene(SceneBase):
    """
    Game Scene
    Inherits from SceneBase
    Responsible for the actual game logic and interaction
    """

    def __init__(self, context):
        SceneBase.__init__(self, context)
        #self.c = cProfile.Profile()
        #self.c.enable()
        self.override_render = True
        self.level = self.context.level
        self.game_over = False
        self.leveling_up = False
        self.context.fractions = [0, 0.25, 0.5, 0.75, 1]
        self.context.fractionStrings = ["0", "1/4", "1/2", "3/4", "1"]
        self.buttons = []
        self.bad_pizzas = []
        self.good_pizzas = []
        self.texts = []
        self.game_toppings = self.context.game_toppings
        self.characters = []
        for character in self.context.game_characters:
            if self.context.difficulty == "Advanced":
                self.characters.append(pygame.transform.scale(character, (character.get_width() / 2, character.get_height() / 2)))
            else:
                self.characters.append(character)
        self.current_pizza = None

        self.createGameMenu()
        self.buildPizzas()
        if self.context.difficulty == "Easy":
            self.createToppingOptions()
            self.num_customers = 1
            self.createMessageBubble()
        else:
            self.createToppingOptionsWithFractions()
            self.num_customers = 4
            self.createMessageBubbles(self.num_customers)
                
        self.pizza_count_msg = Text(self.context, "{} Pizzas left".format(len(self.pizzas)))
        self.pizza_count_msg.setPen(self.context.font)
        self.pizza_count_msg.setColor((0, 0, 0))
        self.pizza_count_msg.setLocation(350, 675)

        self.game_over_msg = Text(self.context, "Game Over!!!")
        self.game_over_msg.centered = True
        self.game_over_msg.setPen(self.context.bold_font_large)
        self.game_over_msg.setColor((255, 140, 0))
        self.game_over_msg.setLocation( self.context.width / 2, 300)

        self.level_up_msg = Text(self.context, "New Level reached")
        self.level_up_msg.centered = True
        self.level_up_msg.setPen(self.context.bold_font_large)
        self.level_up_msg.setColor((255, 140, 0))
        self.level_up_msg.setLocation(self.context.width/2, 300)

        self.continue_button = Button(self.context, "continue")
        self.continue_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.continue_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.continue_button.setOnLeftClick(self.handleContinueButtonClick)
        self.continue_button.setLocation((self.screen.get_width()/2)
                                         -(self.continue_button.width/2),
                                         (self.screen.get_height()/2)
                                         -(self.continue_button.height/2))
        
        self.createTrashCan()
        self.addCookingButton()
        self.generateCurrentPizzaRequirements()
        self.count = 0#for debugging

        self.static_surface = pygame.Surface((self.context.width, self.context.height), pygame.SRCALPHA)
        
        # The game scene is just a blank blue screen
        self.static_surface.fill((244, 101, 36))
        self.static_surface.blit(self.context.shop_background,(0,0))
        if self.context.difficulty == "Advanced":
            self.static_surface.blit(self.characters[0],(150,255))
            self.static_surface.blit(self.characters[1],(594,255))
            self.static_surface.blit(self.characters[2],(150,380))
            self.static_surface.blit(self.characters[3],(594,380))
        else:
            self.static_surface.blit(self.characters[self.level% len(self.characters)],(850,255))
        self.static_surface.blit(self.context.counter_top,(0,0))
        
        pygame.display.flip()

    def ProcessInput(self, events, pressed_keys):
        """
        Process input from user
        Inherits from SceneBase
                Args:   self
                        events - pygame events
                        pressed_keys
        """

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.isClicked(event)
                if self.leveling_up:
                    self.continue_button.isClicked(event)

            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    button.isClicked(event)
                if self.leveling_up:
                    self.continue_button.isClicked(event)

            if event.type == pygame.MOUSEMOTION:
                #for button in self.buttons:
                #    button.isHovered(event)
                if self.leveling_up:
                    self.continue_button.isHovered(event)

    def Update(self):
        """
        Update loop
        inherited from SceneBase
        """

        self.count += 1
        self.checkForGoodPizzas()
        self.checkForTrashedPizzas()
        self.pizza_count_msg.setText("{} Pizzas left".format(len(self.pizzas)))
        self.levelDisplay.setText("Level: {}".format(self.level))

    def Render(self):
        """
        Draw loop
        inherited from SceneBase
        """
        
        self.screen.blit(self.static_surface, (0, 0))
        
        for x in range(0, len(self.message_bubbles)):
            self.message_bubbles[x].drawOn(self.screen)
            
        if self.game_over:
            self.restart_button.setLocation((self.screen.get_width()/2)
                                            -(self.restart_button.width/2),
                                            (self.screen.get_height()/2)
                                            -(self.restart_button.height/2))
            self.restart_button.drawOn(self.screen)
            self.game_over_msg.drawOn(self.screen)
        elif self.leveling_up:
            self.level_up_msg.drawOn(self.screen)
            self.continue_button.drawOn(self.screen)
        else:
            for button in self.buttons:
                button.drawOn(self.screen)
            if self.context.difficulty == "Advanced":
                for fracText in self.fractionTexts:
                    fracText.drawOn(self.screen)

        if self.context.difficulty == "Advanced":
            for text in self.texts:
                text.drawOn(self.screen)
                
        self.screen.blit(self.trashCanBack, (1000, 600))
        #draw pizzas in the trash can
        for pizza in self.bad_pizzas:
            pizza.drawOn(self.screen)
        #then draw available pizzas
        for pizza in self.pizzas:
            pizza.drawOn(self.screen)
        self.pizza_count_msg.drawOn(self.screen)
        self.screen.blit(self.trashCanFront, (1000, 600))
        pygame.display.update()

    """
        Take care of element initialization and event handlers bellow
    """

    def createGameMenu(self):
        """
        Create the in-game menu
        """

        P, K, Y = 300, 5, 30
        currX = P
        self.quit_button = Button(self.context, "Quit")
        self.quit_button.setPen(self.context.font)
        self.quit_button.setColor((255, 255, 255))
        self.quit_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.quit_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.quit_button.setOnLeftClick(self.handleQuitButtonClick)
        self.quit_button.setOnHover(self.handleQuitButtonHover)
        self.quit_button.setLocation(P, Y)
        currX += self.quit_button.width
        self.restart_button = Button(self.context, "Restart")
        self.restart_button.setPen(self.context.font)
        self.restart_button.setColor((255, 255, 255))
        self.restart_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.restart_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.restart_button.setOnLeftClick(self.handleRestartButtonClick)
        self.restart_button.setLocation(currX + K, Y)
        currX += self.restart_button.width + K
        self.home_button = Button(self.context, "Menu/Home")
        self.home_button.setPen(self.context.font)
        self.home_button.setColor((255, 255, 255))
        self.home_button.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.home_button.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.home_button.setOnLeftClick(self.handleHomeButtonClick)
        self.home_button.setLocation(currX + K, Y)
        currX += self.home_button.width + K
        self.levelDisplay = Text(self.context, "Level: {}".format(self.level))
        self.levelDisplay.setPen(self.context.bold_font)
        self.levelDisplay.setLocation(currX + K, Y+5)
        self.levelDisplay.setColor((0, 0, 0))
        self.buttons += [self.quit_button, self.restart_button, self.home_button, self.levelDisplay]

    """
    helper methods below this point
    """
    def handleQuitButtonHover(self):
        """
        Callback for quit button hover
        """
        pass

    def handleQuitButtonClick(self):
        """
        Callback for quit click
        """
        #self.c.disable()
        #self.c.dump_stats("output.txt")
        self.context.quit()

    def handleRestartButtonClick(self):
        """
        Callback for restart click
        """

        self.SwitchToScene(GameScene, self.context)

    def handleContinueButtonClick(self):
        """
        Callback for continue click
        """

        self.SwitchToScene(GameScene, self.context)

    def handleHomeButtonClick(self):
        """
        Callback for home click
        """

        self.SwitchToScene(self.context.starting_scene, self.context)

    def buildPizzas(self):
        """
        build the pizza stack
        """

        self.pizzas = []
        Y = 0
        for _ in xrange(0, 11-self.level):
            pizza = Pizza(self.context)
            pizza.setLocation(140, 620-Y)
            Y += 5
            self.pizzas += [pizza]
        if len(self.pizzas) > 0:
            self.current_pizza = self.pizzas[-1]

    def checkForTrashedPizzas(self):
        """
        Checks for Pizzas in the current game instance and if a pizza is trashed as
        denounced by the pizza_instance.trashed propety it adds it to the bad_pizzas
        pile and removes it from the available pizzas.
        """

        limit, i, trashed = len(self.pizzas), 0, False
        if self.current_pizza:
            previous_requirements = self.current_pizza.requirements
        while i < limit:
            pizza = self.pizzas[i]
            if pizza.trashed:
                self.bad_pizzas += [self.pizzas.pop(i)]
                trashed = True
                limit -= 1
            i += 1
        if trashed:
            if limit > 0:
                self.current_pizza = self.pizzas[-1]
                self.current_pizza.setRequirements(previous_requirements)
                if self.context.difficulty == "Advanced":
                    self.current_pizza.toppings = self.bad_pizzas[-1].toppings
            else:
                self.current_pizza = None
        if not self.current_pizza and (len(self.pizzas) <= 0):
            self.gameOver()

    def checkForGoodPizzas(self):
        """
        Checks for Pizzas in the current game instance and if a pizza is to
        the client's satisfaction as denounced by the pizza_instance.perfected
        propety it adds it to the good_pizzas pile and removes it from the
        available pizzas.
        """

        limit, i, perfected = len(self.pizzas), 0, False
        while i < limit:
            pizza = self.pizzas[i]
            if pizza.perfected:
                self.good_pizzas += [self.pizzas.pop(i)]
                perfected = True
                limit -= 1
            i += 1
        if perfected:
            if limit > 0:
                self.current_pizza = self.pizzas[-1]
            else:
                self.current_pizza = None

    def createToppingOptions(self):
        """
        Create the the ui for topping selection
        """

        X = 600
        Y = 650
        K = 10
        self.cheeseBtn = Button(self.context, "Cheese")
        self.cheeseBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.cheeseBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.cheeseBtn.setOnLeftClick(self.addCheeseTopping)
        self.cheeseBtn.setLocation(X, Y)
        self.mushroomBtn = Button(self.context, "Mushroom")
        self.mushroomBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.mushroomBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.mushroomBtn.setOnLeftClick(self.addMushroomTopping)
        self.mushroomBtn.setLocation(X, Y + self.cheeseBtn.height + K)
        self.pepperoniBtn = Button(self.context, "Pepperoni")
        self.pepperoniBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.pepperoniBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.pepperoniBtn.setOnLeftClick(self.addPepperoniTopping)
        self.pepperoniBtn.setLocation(X + self.cheeseBtn.width + K, Y)
        self.pineappleBtn = Button(self.context, "Pineapple")
        self.pineappleBtn.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.pineappleBtn.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.pineappleBtn.setOnLeftClick(self.addPineappleTopping)
        self.pineappleBtn.setLocation(X + self.mushroomBtn.width + K,
                                      Y + self.pepperoniBtn.height + K)
        self.buttons += [self.cheeseBtn, self.mushroomBtn, self.pepperoniBtn, self.pineappleBtn]

    def createToppingOptionsWithFractions(self):
        """
        Create the ui for the fractions options
        """

        X = 590
        Y = 620
        K = 4
        height = 50
        textOffset = 6
        
        toppings = ["Cheese", "Pepperoni", "Mushroom", "Pineapple"]
        for i in range(0, len(toppings)):
            text = Text(self.context, toppings[i])
            text.setPen(self.context.font)
            text.setColor((0, 0, 0))
            text.setLocation(X, 620 + i * height + textOffset)
            self.texts.append(text)
            
        X = X + 130

        increaseCallbacks = [self.increaseCheeseTopping, self.increaseMushroomTopping,
                             self.increasePepperoniTopping, self.increasePineappleTopping]
        decreaseCallbacks = [self.decreaseCheeseTopping, self.decreaseMushroomTopping,
                             self.decreasePepperoniTopping, self.decreasePineappleTopping]

        self.fractionTexts = []

        for i in range(0, 4):
            leftButton = Button(self.context, "<")
            leftButton.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
            leftButton.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
            leftButton.setOnLeftClick(decreaseCallbacks[i])
            leftButton.setLocation(X + K * 3, Y + height * i)
            leftButton.width = 30
            leftButton.dirty = True

            fracText = Text(self.context, "0")
            fracText.centered = True
            fracText.setLocation(leftButton.location[0] + leftButton.width + 35,
                                 Y + textOffset + height * i)
            rightButton = Button(self.context, ">")
            rightButton.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
            rightButton.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
            rightButton.setOnLeftClick(increaseCallbacks[i])
            rightButton.setLocation(leftButton.location[0] + 100, Y + height * i)
            rightButton.width = 30
            rightButton.dirty = True

            self.fractionTexts += [fracText]
            self.buttons += [leftButton, rightButton]


    def addCheeseTopping(self):
        """
        Add topping
        """
        if self.current_pizza:
            self.current_pizza.addTopping(0)

    def addMushroomTopping(self):
        """
        Add topping
        """
        if self.current_pizza:
            self.current_pizza.addTopping(1)

    def addPepperoniTopping(self):
        """
        Add topping
        """
        if self.current_pizza:
            self.current_pizza.addTopping(2)

    def addPineappleTopping(self):
        """
        Add topping
        """
        if self.current_pizza:
            self.current_pizza.addTopping(3)

    def increaseCheeseTopping(self):
        """
        increase topping
        """
        self.changeToppingAmount(0, 1)

    def increaseMushroomTopping(self):
        """
        increase topping
        """
        self.changeToppingAmount(1, 1)

    def increasePepperoniTopping(self):
        """
        increase topping
        """
        self.changeToppingAmount(2, 1)

    def increasePineappleTopping(self):
        """
        increase topping
        """
        self.changeToppingAmount(3, 1)

    def decreaseCheeseTopping(self):
        """
        decrease topping
        """
        self.changeToppingAmount(0, -1)

    def decreaseMushroomTopping(self):
        """
        decrease topping
        """
        self.changeToppingAmount(1, -1)

    def decreasePepperoniTopping(self):
        """
        decrease topping
        """
        self.changeToppingAmount(2, -1)

    def decreasePineappleTopping(self):
        """
        decrease topping
        """
        self.changeToppingAmount(3, -1)

    def changeToppingAmount(self, index, amount):
        """
        change topping amound
        """
        newAmount = self.current_pizza.toppings[index] + amount
        if newAmount >= 0 and newAmount < len(self.context.fractions):
            self.current_pizza.changeTopping(index, newAmount)
            self.fractionTexts[index].setText(str(self.context.fractionStrings[newAmount]))

    def addCookingButton(self):
        """
        Create the cook button ui
        """

        self.cook = Button(self.context, "Cook")
        self.cook.setLocation(120, 770)
        self.cook.setBackgroundImg(self.context.button_bg, STATE.NORMAL)
        self.cook.setBackgroundImg(self.context.button_bg_active, STATE.ACTIVE)
        self.cook.setOnLeftClick(self.handleCooking)
        self.buttons += [self.cook]

    def handleCooking(self):
        """
        On cook check the accuracy of the user choices
        """

        if self.current_pizza:
            validity = self.current_pizza.checkRequirements()
            if validity[0]:
                self.current_pizza.setPerfect()
                self.levelUp()
            else:
                self.current_pizza.moveToTrash((1000, 600), self.trashCan)
            for i in range(1, len(validity)):
                if self.context.difficulty == "Advanced":
                    self.message_bubbles[i-1].messages = []
                self.message_bubbles[i-1].addMessage(None, validity[i])

    def createMessageBubble(self):
        """
        Create message ui
        """
        
        self.message_bubbles = []
        self.message_bubbles.append(MessageBubble(self.context))
    
    def createMessageBubbles(self, i):
        """
        Create message ui
        """
        
        self.message_bubbles = []
        exes = [280, 724, 280, 724]
        whys = [255, 255, 380, 380]
        for x in range(0, i):
            bubble = MessageBubble(self.context)
            bubble.flip = True
            bubble.setLocation(exes[x], whys[x])
            bubble.setScale(300, 150)
            self.message_bubbles.append(bubble)
        
    def createTrashCan(self):
        """
        Create the trashcan ui
        """

        #trashcan is imaginary only back and front are drawn.
        self.trashCan = self.context.trash_can_img
        self.trashCanFront = self.context.trash_can_front_img
        self.trashCanBack = self.context.trash_can_back_img

    def generateCurrentPizzaRequirements(self):
        """
        Create the next pizza for the user to guess
        """

        requires = []
        if self.context.difficulty == "Easy":
            for _ in self.game_toppings:
                requires += [random.choice((0, 1))]
            print requires
        else:
            requires = [0 for _ in range(0, self.num_customers)]
            for x in range(0, self.num_customers):
                req = []
                for _ in self.game_toppings:
                    req += [random.choice((0, 1.0/4.0))]
                requires[x] = req

        if self.current_pizza:
            if self.context.difficulty == "Advanced":
                print "Requirements:"
            for i in range(0, self.num_customers):
                self.message_bubbles[i].addMessage("I need a pizza")
                if self.context.difficulty == "Advanced":
                    print str(requires[i])
            
            self.current_pizza.setRequirements(requires)

    def levelUp(self):
        """
        Level up the player
        """

        self.leveling_up = True
        self.context.total_good_pizza += 1
        if self.context.level < len(self.context.game_characters):
            self.context.level += 1
            print "Leveling up"
        else:
            print "Max level reached"

    def gameOver(self):
        """
        End the game
        """

        self.game_over = True
