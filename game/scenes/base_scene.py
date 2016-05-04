class SceneBase:
    def __init__(self, context):
        self.next = self
        self.context = context
        self.screen = self.context.screen

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene, context=None):
        if next_scene == None:
            self.next = next_scene
        else:
            if context:
                self.next = next_scene(context)
            else:
                self.next = next_scene(self.context)

    def Terminate(self):
        self.SwitchToScene(None)
