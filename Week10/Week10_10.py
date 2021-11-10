from tkinter import *
from tkinter.messagebox import *


def op(event):
    submenu2.post(event.x_root, event.y_root)


def openmenu():
    showinfo(title='my_title', message='打开')


def op_copy():
    showinfo(title='my_title', message="正在执行复制操作")


root = Tk()
root.title("my_title")
root.geometry('300x400')
text1 = Text(root)
text1.insert(END, '123456789')
submenu2 = Menu(text1)
# submenu1 = Menu(menubar, tearoff=0)
# submenu1.add_command(label="打开", command=openmenu)
# submenu1.add_command(label="保存")
# submenu1.add_command(label="退出", command=root.destroy)
# menubar.add_cascade(label="文件", menu=submenu1)

# submenu2 = Menu(menubar, tearoff=2)
submenu2.add_command(label="复制", command=op_copy)
submenu2.add_command(label="剪切")
submenu2.add_command(label="粘贴")
# menubar.add_cascade(label="编辑", menu=submenu2)
text1.bind('<Button-3>', op)
text1.pack()
# root['menu'] = menubar
root.mainloop()
