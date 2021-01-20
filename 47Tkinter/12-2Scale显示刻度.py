from tkinter import *
'''显示刻度'''
root = Tk()


Scale(root, from_=0, to=32, tickinterval=5, resolution=5, length=100).pack()
Scale(root, from_=0, to=100, tickinterval=10, orient=HORIZONTAL,length=300).pack()


mainloop()
