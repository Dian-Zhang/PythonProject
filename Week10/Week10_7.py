from tkinter import *
from tkinter.messagebox import *


def rb_command():
    if v.get() == "1":
        showinfo(title="信息", message="A")
    if v.get() == "2":
        showinfo(title="信息", message="B")
    if v.get() == "3":
        showinfo(title="信息", message="C")
    if v.get() == "4":
        showinfo(title="信息", message="D")


root = Tk()
root.title("title")
lframe = LabelFrame(root, text="选择你的答案")
v = StringVar()
v.set("1")
rb1 = Radiobutton(lframe, text="A", command=rb_command, variable=v, value="1")
rb1.pack()
rb2 = Radiobutton(lframe, text="B", command=rb_command, variable=v, value="2")
rb2.pack()
rb3 = Radiobutton(lframe, text="C", command=rb_command, variable=v, value="3")
rb3.pack()
rb4 = Radiobutton(lframe, text="D", command=rb_command, variable=v, value="4")
rb4.pack()
lframe.pack()
root.mainloop()
