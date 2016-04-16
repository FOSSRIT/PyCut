import pygame

from . import scenes, events, objects

class PyCutGame():
    """docstring for PyCutGame"""
    def __init__(self):

        self.data = None
        self.width = 600
        self.height = 500
        self.fps = 60
        self.title = "PyCut"
        self.font_path  = "game/assets/Roboto-Thin.ttf"
        self.quit_attempt = False
        #everything necessary for the game should be initialized before here
        #the context is established based on these details and passed along to the active scene
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(self.font_path, 72)
        self.font = pygame.font.Font(self.font_path, 24)
        self.font_small = pygame.font.Font(self.font_path, 14)
        pygame.display.set_caption(self.title)
        self.starting_scene = scenes.TitleScene(self)
        self.active_scene = self.starting_scene
        """    def write(self, text, center, size=self.size):
        = pygame.font.Font"""

    def game_loop(self):
        while self.active_scene != None:
            pressed_keys = pygame.key.get_pressed()
            # Event filtering
            filtered_events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                                  pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_ESCAPE:
                        self.quit_attempt = True
                    elif event.key == pygame.K_F4 and alt_pressed:
                        self.quit_attempt = True

                if self.quit_attempt:
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

    def quit(self):
        self.quit_attempt = True
