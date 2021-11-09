from tkinter import *
from tkinter.messagebox import *


def cb_command():
    if v.get() == "1":
        showinfo(title="信息", message="我是学生")
    else:
        showinfo(title="信息", message="我不是学生")


root = Tk()
root.title("title")
root.geometry("400x300")
v = StringVar()
v.set("0")
cb1 = Checkbutton(root, text="软件工程", command=cb_command(), variable=v,
                  onvalue="1", offvalue="0")
cb1.pack()
root.mainloop()
