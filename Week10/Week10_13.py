from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('my_title')
root.geometry("400x300")
l1 = Label(root, text='姓名').grid(row=0, column=0)
et1 = Entry(root).grid(row=0, column=1, columnspan=2)

l2 = Label(root, text='密码').grid(row=1, column=0)
et2 = Entry(root).grid(row=1, column=1, columnspan=2)

btn1 = Button(root, text='确认').grid(row=2, column=1)
btn2 = Button(root, text='重置').grid(row=2, column=2)

root.mainloop()
