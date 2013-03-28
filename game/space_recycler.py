import spyral
import sys, time, random

SIZE = (1200, 900)
BG_COLOR = (0, 0, 0)

class Asteroid(spyral.Sprite):
    pass
    
class JunkFactory(spyral.Actor):
    def __init__(self, scene):
        spyral.Actor.__init__(self)
        self.scene = scene
        
    def main(self, dt):
        delay = spyral.Animation('delay', spyral.animator.Linear(600, 0), duration = 4.0)
        while True:
            self.run_animation(delay)
            self.scene.junks.append(Junk(self.scene))
        
class Junk(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        self.x = random.randrange(100, 500)
        self.y = random.randrange(100, 500)

class Ship(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)

class SpaceRecycler(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self)
        self.load_style("game\style.spys")
        self.register("system.quit", sys.exit)
        
        self.ship = Ship(self)
        self.junks = []
        self.junkFactory = JunkFactory(self)
        

if __name__ == "__main__":
    spyral.director.init(SIZE) # the director is the manager for your scenes
    spyral.director.run(scene=SpaceRecycler()) # This will run your game. It will not return.
