from tkinter import *
'''<Motion>用于实时获取鼠标位置'''
root = Tk()
def callback(event):
    print('鼠标位置', event.x, event.y)
frame =  Frame(root, width=200, height=200)
frame.bind("<Motion>", callback)
frame.pack()

mainloop()