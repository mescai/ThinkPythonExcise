
class Point(object):
    """
     Represents a point in 2-D space.
    """
import math
def distance_between_points(point1,point2):
    return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)

class Rectangle(object):
    """
    Represents a rectangle.
    attributes:width,height,corner.
    """

def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy

import copy
def move_rectangle_better(rect,dx,dy):
    box=copy.deepcopy(rect)
    box.corner.x+=dx
    box.corner.y+=dy
    return box

from swampy.World import World
def draw_rectangle(canvas,rectangle):
    bbox=[[rectangle.corner.x,rectangle.corner.y],[rectangle.corner.x+rectangle.width,rectangle.corner.y+rectangle.height]]
    canvas.rectangle(bbox,outline=None,fill=rectangle.color)

def creat_rectangle(cornerx,cornery,width,height,color):
    """creats a rectangle

    :param cornerx: site at x-axis of the lower left corner
    :param cornery: site at y-axis of the lower left corner
    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :return: a new rectangle with the attributes above
    """
    rectangle=Rectangle()
    rectangle.corner=Point()
    rectangle.corner.x=cornerx
    rectangle.corner.y=cornery
    rectangle.width=width
    rectangle.height=height
    rectangle.color=color
    return rectangle


def creat_point(x,y,color):
    """
    creats a new point in the world
    :param x: site at x-axis of the point
    :param y: site at y-axis of the point
    :param color: the color of the point
    :return: a new point
    """
    point=Point()
    point.x=x
    point.y=y
    point.color=color
    return point


def draw_point(canvas,point):
    bbox=[[point.x,point.y],[point.x,point.y]]
    canvas.rectangle(bbox,fill=point.color)

class Circle(object):
    """
    Represents a circle
    """
def creat_cicle(centrex,centrey,radius,color):
    cicle=Circle()
    cicle.centre=Point()
    cicle.centre.x=centrex
    cicle.centre.y=centrey
    cicle.radius=radius
    cicle.color=color
    return cicle

def draw_polygon(canvas,color,*args):
    points=[]
    for arg in args:
        points.append(arg)
    canvas.polygon(points,fill=color)



if __name__=="__main__":
    world=World()
    canvas=world.ca(width=500,height=500,background="white")
    rectangle=creat_rectangle(-100,-100,300,200,color="white")
    draw_rectangle(canvas,rectangle)
    draw_polygon(canvas,"blue",[-100,-100],[-100,100],[50,0])
    draw_polygon(canvas,"red",[-100,-100],[200,-100],[200,0],[50,0])
    world.mainloop()