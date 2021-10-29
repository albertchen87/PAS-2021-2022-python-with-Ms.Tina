from sys import exit

class Scene(object):
    def enter(self):
        print("This scene is not configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, sceneMap):
        self.sceneMap = sceneMap
    
    def play(self):
        currentScene = self.sceneMap.openingScene()

        while True:
            print("\n----------")
            nextSceneName = currentScene.enter()
            currentScene = self.sceneMap.nextScene(nextSceneName)

class Death(Scene):
    lines = "you write essays till death"

    def enter(self):
        print(Death.lines)
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("you are about to apply college, what should you do ?")

        action = input(">")
        if action == "creative mode":
            return "win"

        elif action == "play games":
            print("you start to play games on the hallway and meet Pamela")
            print("Then pamela makes you finish your essays in one day")
            return "death"

        elif action == "procrastinate":
            print("you can't apply early action and need to go to regular")
            return "regularApplication"
        elif action == "Write essays":
            print("you are a good student and gets to apply during ea, but pamela also wants you to apply in regular")
            return "regularApplication"
        else:
            print("what do you mean? you don't have this choice")
            return "CentralCorridor"

class regularApplication(Scene):
    def enter(self):
        print("you are now in regular application and what should you be doin?")

        action = input(">")
        if action == "write essays":
            print("you are so hard working")
            return "win"
        elif action == "procrastinate":
            print("you have no essays to apply so you need to finish quick")
            return "death"

class Win(Scene):
    def enter(self):
        print("you get into a good college")
        exit(1)

class Map(object):
    scenes = {"CentralCorridor": CentralCorridor(), "regularApplication": regularApplication(), "death": Death(), "win": Win()}

    def __init__(self, startScene):
        self.startScene = startScene

    def nextScene(self, sceneName):
        return Map.scenes.get(sceneName)
    
    def openingScene(self):
        return self.nextScene(self.startScene)

aMap = Map("CentralCorridor")
aGame = Engine(aMap)
aGame.play()