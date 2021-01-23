from tkinter import *
'''通过设置undo选项为True可以开启Text组件的“撤销”功能。
然后用edit._undo()方法实现“撤销”操作,用edit_ redo()方法实现“取消撤销”操作'''
root = Tk()
text = Text(root, width=30, height=5, undo=True)
text.pack()
text.insert(INSERT, 'Damon is very cool')
def show1():
    text.edit_undo()
def show2():
    text.edit_redo()
Button(root, text='撤销', command=show1).pack()
Button(root, text='取消撤销', command=show2).pack()

mainloop()