from tkinter import *
from tkinter.messagebox import *


def cb_command():
    showinfo(title="复选框", message="被选中")


root = Tk()
root.title("title")
root.geometry("400x300")
cb1 = Checkbutton(root, text="软件工程", command=cb_command())
cb1.pack()
cb2 = Checkbutton(root, text="计算机")
cb2.pack()
root.mainloop()
