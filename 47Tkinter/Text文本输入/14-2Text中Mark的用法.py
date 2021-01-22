from tkinter import *
'''Mark 
这里面就是将这个索引位标记为‘here’这个名字，
可以使用mark.unset()删除这个索引名。'''
root = Tk()
text = Text(root, width=30, height=20)
text.pack()
text.insert(INSERT, 'Damon wants to sleep')
text.mark_set('here', 1.2)
text.insert('here', '插入')



mainloop()