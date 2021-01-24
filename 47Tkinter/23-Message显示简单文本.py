from tkinter import *
"""Message实现简单消息的显示，可以自动换行，当然也可以自己添加换行符"""
root = Tk()
w1 = Message(root, text="这是一-则消息", width=100)
w1.pack()
w2 = Message(root, text="这是一则骇人听闻的长长长长长长消息!", width=100)
w2. pack()

mainloop()
