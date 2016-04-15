import pygame

from .base_scene import SceneBase
from .title_scene import TitleScene
from .game_scene import GameScene

class PyCutGame():
    """docstring for PyCutGame"""
    def __init__(self):
        self.data = None
        self.width = 600
        self.height = 500
        self.fps = 60
        self.title = "PyCut"
        self.font_name  = "freesans.ttf"
        self.start_button = None
        #everything necessary for the game should be initialized before here
        #the context is established based on these details and passed along to the active scene
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.starting_scene = TitleScene(self)
        self.active_scene = self.starting_scene
        """    def write(self, text, center, size=self.size):
        = pygame.font.Font"""

    def game_loop(self):
        pygame.init()

        while self.active_scene != None:
            pressed_keys = pygame.key.get_pressed()

            # Event filtering
            filtered_events = []
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == pygame.QUIT:
                    quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                                  pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_ESCAPE:
                        quit_attempt = True
                    elif event.key == pygame.K_F4 and alt_pressed:
                        quit_attempt = True

                if quit_attempt:
                    self.active_scene.Terminate()
                else:
                    filtered_events.append(event)

            self.active_scene.ProcessInput(filtered_events, pressed_keys)
            self.active_scene.Update()
            self.active_scene.Render()

            self.active_scene = self.active_scene.next

            pygame.display.flip()
            self.clock.tick(self.fps)


    def run(self):
        self.game_loop()
