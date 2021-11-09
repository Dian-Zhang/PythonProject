from tkinter import *
from tkinter.messagebox import showinfo


def btn_command():
    showinfo(title="新title", message="点击")


root = Tk()
root.title("title")
root.geometry("400x300")

btn1 = Button(root, text="确定", command=btn_command())
btn1.pack()
root.mainloop()
