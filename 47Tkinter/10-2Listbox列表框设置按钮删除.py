from tkinter import *
'''使用一些特殊的索引号:比如ACTIVE表示选中的项目(如果Listbox允许多选,那么它表示最后一个被选中
的项目) ; 又如END表示Listbox的最后-行,所以当要插入一个项目到列表时可以使用END :
'''
master = Tk()

thelb = Listbox(master)
thelb.pack()

for item in ['a','b','c','d','e','f','g','h']:
         thelb.insert(END, item)

theButton = Button(master, text='删除',\
                   command=lambda x=thelb:x.delete(ACTIVE))
theButton.pack()
mainloop()
