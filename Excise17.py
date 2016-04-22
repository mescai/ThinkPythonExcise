def int_to_time(seconds):
    time=Time()
    minutes,time.second=divmod(seconds,60)
    time.hour,time.minute=divmod(minutes,60)
    return time

class Time(object):

    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__(self):
        return "%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second)

    def __add__(self, other):
        if isinstance(other,Time):
            seconds=self.time_to_int()+other.time_to_int()
            return int_to_time(seconds)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def print_time(self):
        print "%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second)

    def time_to_int(self):
        minutes=self.hour*60+self.minute
        seconds=minutes*60+self.second
        return seconds

    def increment(self,seconds):
        seconds+=self.time_to_int()
        return int_to_time(seconds)

    def is_after(self,other):
        return self.time_to_int()>other.time_to_int()

import types
class Point(object):
    """

    """
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y

    def __str__(self):
        return "%f,%f"  %(self.x,self.y)

    def __add__(self, other):
        if isinstance(other,Point):
            return Point(x=self.x+other.x,y=self.y+other.y)
        if type(other) is types.TupleType:
            return Point(x=self.x+other[0],y=self.y+other[1])

    def __radd__(self, other):
        return self.__add__(other)

class Kangaroo(object):
    """

    """
    def __init__(self,content=None):
        self.pouch_contents=content

    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = "  " + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self,other):
        self.pouch_contents.append(other)

import visual

if __name__=="__main__":
    visual.scene.range=(256,256,256)
    visual.center=(128,128,128)
    color=(0.1,0.1,0.9)
    visual.sphere(pos=visual.scene.center,radius=128,color=color)
