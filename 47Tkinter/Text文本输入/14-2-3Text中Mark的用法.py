from tkinter import *
'''如果Mark周围的文本被删除了, Mark仍然还是在的
(只是它后边的那个字符被删除了，所以它六神无主，只能初始化为"1.0"):
结果显示，插入的位置并不固定
'''
root = Tk()
text = Text(root, width=30, height=20)
text.pack()
text.insert(INSERT, 'Damon wants to sleep')
text.mark_set('here', 1.2)
text.insert('here', '插入')
text.delete('1.1', 1.7)
text.insert('here', '一个')


mainloop()