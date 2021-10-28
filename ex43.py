class Scene(object):
    def enter(self):
        print("This scene is not configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        currentScene = self.sceneMap.openingScene()

        while True:
            print("\n----------")
            nextSceneName = currenScene.enter()