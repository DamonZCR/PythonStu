from tkinter import *
'''我希望插入一个字符就算一次完整的操作，然后每次点击“撤销”就去掉一个字符。
先将autoseparators选项设置为False (因为这个选项是让Tkinter在
认为一次完整的操作结束后自动插入"分隔符”)了然后绑定键盘事件,
每次有输入就用edit.separator()方法人为地插入一个“分隔符”'''
root = Tk()
text = Text(root, width=30, height=5, undo=True, autoseparators=False)
text.pack()
text.insert(INSERT, 'Damon is very cool')

def callback(event):
    text.edit_separator()
text.bind('<Key>', callback)
def show1():
    text.edit_undo()

Button(root, text='撤销', command=show1).pack()

mainloop()