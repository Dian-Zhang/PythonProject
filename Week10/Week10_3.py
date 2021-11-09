from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("title")
root.geometry("400x300")

btn3 = Button(root, text="正常状态", state="normal")
btn3.pack()
btn4 = Button(root, text="激活状态", state="active")
btn4.pack()
btn5 = Button(root, text="不可编辑状态", state="disable")
btn5.pack()
root.mainloop()
