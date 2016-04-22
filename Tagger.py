

from Wobbler import *
import math

class Tagger(Wobbler):
    """

    """

    def __init__(self, world, speed=1, clumsiness=60, color='red'):

        # call the __init__ method from Wobbler to initialize
        # world, speed, clumsiness, and color.
        Wobbler.__init__(self, world, speed, clumsiness, color)

        # then initialize the additional attributes that Taggers have
        self.it = 0
        self.sulking = 0

    def steer(self):
        a=math.atan2(self.y,self.x)
        self.rt(180-a+self.heading)





if __name__ == '__main__':
    world = make_world(Tagger)
    world.mainloop()