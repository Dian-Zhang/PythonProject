from tkinter import *

root = Tk()

MainLabel = Label(root, text="Hello Tkinter GUI", font="隶书 20 bold",
                  fg="red", bg="blue", bitmap="warning",compound="right")
root.title("Week10")
root.geometry("400x300")
root.resizable(width="False", height="False")
root.update()
MainLabel.pack()
root.mainloop()
