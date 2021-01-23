from tkinter import *

root = Tk()
w = Canvas(root, width=200, heigh=100)
w.pack()
# 前两个参数代表起点，后两个代表终点，dash代表线的样式，虚线
w.create_line(0, 50, 200, 50, fill='black')
w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))
w.create_rectangle(50, 25, 150, 75, fill='orange')

mainloop()