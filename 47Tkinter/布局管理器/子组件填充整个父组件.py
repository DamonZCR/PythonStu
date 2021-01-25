from tkinter import *
"""生成一个Listbox组件并将它填充到root窗口中"""
root = Tk()
listbox = Listbox( root)
# fill=“both”，表示横向和纵向都填充,expand参数表示的是容器在整个窗口上，将容器放置在剩余空闲位置上的中央(包括水平和垂直方向)
listbox. pack(fill=BOTH, expand=True)
for i in range(10):
    listbox. insert(END, str(i))
mainloop()





