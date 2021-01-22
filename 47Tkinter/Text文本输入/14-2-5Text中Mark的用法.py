from tkinter import *
'''默认插入内容到Mark，是插入到它的左侧(就是说插入一个字符的话，
Mark向后移动了一个字符的位置)。那能不能插入到Mark的右侧呢?其实是可以的，
通过mark _gravity0方法就可以实现。
'''
root = Tk()
text = Text(root, width=30, height=20)
text.pack()
text.insert(INSERT, 'Damon wants to sleep')
text.mark_set('here', 1.2)
# 改为依靠左边
text.mark_gravity('here', LEFT)
text.insert('here', '插入')
text.insert('here', '一个')


mainloop()