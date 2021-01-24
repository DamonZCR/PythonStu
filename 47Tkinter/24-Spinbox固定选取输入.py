from tkinter import *
'''从上下按键选择1-10的一个值，也可以自己输入。'''
root = Tk()
# 范围从0到10
w = Spinbox(root, from_=0, to=10, wrap=True)
w.pack()

w2 = Spinbox(root, values=('z','w','l','D'), wrap=True)
w2.pack()

mainloop()