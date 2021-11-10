from tkinter import *
from tkinter.messagebox import *


def getvalue():
    content = et2.get()
    showinfo(title='my_title', message=content)


root = Tk()
root.title("我的标题")
root.geometry('300x400')
v = StringVar()

et1 = Entry(root, textvariable=v)
v.set("请输入用户名")
et1.pack()
et2 = Entry(root)
et2['show'] = '*'
et2.pack()
loginable = Button(root, text='确认', command=getvalue).pack()

root.mainloop()
