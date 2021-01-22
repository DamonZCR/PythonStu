from tkinter import *
'''想控制Tags间的优先级可以使用tag. raise() 和tag_ lower()方法来提高和降低某个Tag的优先级
'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Damon doing word')
text.tag_add('tag1', '1.6', '1.11', '1.12')
text.tag_add('tag2', '1.6', '1.11', '1.12')
text.tag_config('tag1', background='yellow', foreground='orange')
text.tag_config('tag2', background='blue')

# text.tag_lower('tag2')

text.insert(INSERT, 'Damon love sleep', ('tag2','tag1'))
mainloop()

