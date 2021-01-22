from tkinter import *
'''Tags (标签)通常用于改变Text组件中内容的样式和功能。你可以修改文本的字体、尺寸和颜色。'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Damon doing word')
text.tag_add('tag1', '1.6', '1.11', '1.12')
text.tag_config('tag1', background='yellow', foreground='red')

mainloop()

