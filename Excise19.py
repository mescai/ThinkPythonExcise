
from Gui import *


g=Gui()
g.title("Gui")
button=g.bu(text="Press me.")


def make_label():
    g.la(text="Thank you.")

botton2=g.bu(text="No, Press me!",command=make_label())

g.mainloop()
