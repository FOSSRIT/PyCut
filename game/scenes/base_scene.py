"""
Scene Module
"""
class SceneBase(object):
    """
    Base Scene class
    Contains required functions of each implemented scene
    """
    def __init__(self, context):
        self.next = self
        self.context = context
        self.screen = self.context.screen
        self.override_render = False

    def ProcessInput(self, events, pressed_keys):
        """
        Handle incoming inputs from the user

            Args:   self
                    events
                    pressed_keys
        """

        # print the args to remove unused arg warning
        print "events: " + events
        print "pressed keys: " + pressed_keys
        print "uh-oh, you didn't override this in the child class"

    def Update(self):
        """
        Scene's update loop
        """
        print "uh-oh, you didn't override this in the child class"

    def Render(self):
        """
        Scene's draw loop
        """
        print "uh-oh, you didn't override this in the child class"

    def SwitchToScene(self, next_scene, context=None):
        """
        Call the next/specified Scene

            Args:   self
                    next_scene - the next scene object to move to
                    context - game context and data
        """
        if next_scene is None:
            self.next = next_scene
        else:
            if context:
                self.next = next_scene(context)
            else:
                self.next = next_scene(self.context)

    def Terminate(self):
        """
        Terminate this scene, this will call SwitchToScene on None
        """
        self.SwitchToScene(None)
