from tkinter import *
'''删除Mark标记
'''
root = Tk()
text = Text(root, width=30, height=20)
text.pack()
text.insert(INSERT, 'Damon wants to sleep')
text.mark_set('here', 1.2)
text.mark_unset('here')

text.delete('1.1', 1.7)
text.insert('here', '一个')


mainloop()