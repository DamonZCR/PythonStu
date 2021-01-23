from tkinter import *
'''画布中，样式的修改共有三个方法：coords(),itemconfig(),move()或者delete()'''
root = Tk()
w = Canvas(root, width=200, heigh=100)
w.pack()
# 前两个参数代表起点，后两个代表终点，dash代表线的样式，虚线
line1 = w.create_line(0, 50, 200, 50, fill='black')
line2 = w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))
rect1 = w.create_rectangle(50, 25, 150, 75, fill='orange')
# 实现样式的移动，
w.coords(line1, 0, 25, 200, 20)
# 用于设置样式的各个选项
w.itemconfig(rect1, fill='blue')
w.delete(line2)
# 这里的ALL是一个tag,代表画布上的所有对象。
Button(root, text='清除所有', command=(lambda x=ALL:w.delete(x))).pack()

mainloop()