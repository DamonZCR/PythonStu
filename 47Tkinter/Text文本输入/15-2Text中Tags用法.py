from tkinter import *
'''如果你对同一个范围内的文本加上多个Tags，并且设置相同的选项，
那么新创建的Tag样式会覆盖比较旧的Tag:
'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Damon doing word')
text.tag_add('tag1', '1.6', '1.11', '1.12')
text.tag_add('tag2', '1.6', '1.11', '1.12')
text.tag_config('tag1', background='yellow', foreground='orange')
text.tag_config('tag2', background='blue')

# 那么新创建的Tag2会覆盖比较旧的Tagl 的相同选项
# 注意，与下边的调用顺序没有关系

text.insert(INSERT, 'Damon love sleep', ('tag2','tag1'))
mainloop()

