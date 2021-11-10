from tkinter import *
from tkinter.messagebox import *


def btn_command(event):
    print("%d,%d" % (event.x, event.y))


def press_command(event):
    print("%s" % event.char)


root = Tk()
root.title('my_tiele')

root.bind("<Button-1>", btn_command)
root.bind("<Key>", press_command)
root.mainloop()
