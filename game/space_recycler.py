import spyral
import sys

SIZE = (1200, 900)
BG_COLOR = (0, 0, 0)

class Asteroid(spyral.Sprite):
    pass
    
class JunkFactory(spyral.Actor):
    def main(self, dt):
        while True:
            self.wait(1)
            print "Hello"
        
class Junk(spyral.Sprite):
    pass

class Ship(spyral.Sprite):
    pass

class SpaceRecycler(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self)
        self.load_style("game\style.spys")
        self.register("system.quit", sys.exit)
        
        self.ship = Ship(self)
        self.junkFactory = JunkFactory()
        

if __name__ == "__main__":
    spyral.director.init(SIZE) # the director is the manager for your scenes
    spyral.director.run(scene=SpaceRecycler()) # This will run your game. It will not return.
