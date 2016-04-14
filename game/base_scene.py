import game


class SceneBase:
    def __init__(self, context):
        self.next = self
        self.context = context

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        if next_scene == None:
            self.next = next_scene
        else:
            self.next = next_scene(self.context)

    def Terminate(self):
        self.SwitchToScene(None)
