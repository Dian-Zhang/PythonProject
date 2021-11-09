from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("title")
root.geometry("400x300")

btn6 = Button(root, text="确定", width=20)
btn6.pack(side="left")
btn7 = Button(root, text="取消", width=20)
btn7.pack(side="right")
btn6.focus_force()
root.mainloop()
