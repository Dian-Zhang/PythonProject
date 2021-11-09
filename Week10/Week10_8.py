from tkinter import *
from tkinter.messagebox import *


def lb_command(event):
    position = lb2.curselection()
    if position:
        text = lb2.get(lb2.curselection())
        content = "选中项目：", position[0], ";选中内容：", text
        showinfo(message=content)


root = Tk()
root.title("my title")
root.geometry("300x400")
lb2 = Listbox(root, selectmode=EXTENDED)
lb2.insert(1, "python")
lb2.insert(2, "java")
lb2.insert(3, "C++")
lb2.insert(4, "GO")
lb2.bind('<Button-1>', lb_command)
lb2.pack()

root.mainloop()
