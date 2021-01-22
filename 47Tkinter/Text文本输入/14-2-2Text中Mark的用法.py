from tkinter import *
'''如果Mark前边的内容发生改变，那么Mark的位置也会跟着移动
(说白了就是Mark会“记住”它后边的那个字符
'''
root = Tk()
text = Text(root, width=30, height=20)
text.pack()
text.insert(INSERT, 'Damon wants to sleep')
text.mark_set('here', 1.2)
text.insert('here', '插入')
text.insert('here', '一个')
text.insert('here', '词语')


mainloop()