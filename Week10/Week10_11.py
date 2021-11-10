from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('my_tiele')
root.geometry('300x400')
l1 = Label(root, text='pack01', bg='blue').pack(fill=BOTH, expand='yes', side='left', padx=10)
l2 = Label(root, text='pack02', bg='green').pack(fill=Y, expand='yes', side='left', padx=10, ipadx=50)
l3 = Label(root, text='pack03', bg='red').pack(side='bottom', padx=10, ipadx=10)
root.mainloop()
