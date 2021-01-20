from tkinter import *
'''为了在某个组件上安装垂直滚动条,需要做两件事
1.设置该组件的yscrollbarcommand选项为Scrollbar组件的set()方法;
2.设置Scrollbar组件的command选项为该组件的yview()方法。
需要知道的是如果支持滚动条就会有yscrollbarcommand属性选项的（前面的字母y就代表竖直。）。
'''
root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb.set)
for i in range(500):
         lb.insert(END, i)

lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)

mainloop()
