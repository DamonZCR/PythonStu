from tkinter import *
'''Scale (刻度)组件看起来像是一个带数据的Scrollbar (滚动条)组件，
但事实上它们是不同的。Scale 组件允许用于通过滑动滑块来选择一个范围内的数字
控制该组件的最大值、最小值，以及分辨率。'''
root = Tk()
Scale(root, from_=0, to=32).pack()
Scale(root, from_=0, to=100, orient=HORIZONTAL).pack()

mainloop()
