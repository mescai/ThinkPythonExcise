

import visual
import color_list

def create_cube():
    visual.scene.range=(256,256,256)
    visual.scene.center=(128,128,128)


    t=range(0,256,51)
    for x in t:
        for y in t:
            for z in t:
                pos=x,y,z
                color=(x/255.0,y/255.0,z/255.0)
                visual.sphere(pos=pos,radius=10,color=color)

def create_color_cube():
    visual.scene.range=(256,256,256)
    visual.scene.center=(128,128,128)
    color_dict,rgbs=color_list.read_colors()
    for rgb in color_dict.values():
        r=int(rgb[1:3],16)
        g=int(rgb[3:5],16)
        b=int(rgb[5:7],16)
        pos=(r,g,b)
        color=(r/255.0,g/255.0,b/255.0)
        visual.sphere(pos=pos,radius=10,color=color)


if __name__=="__main__":
    create_color_cube()