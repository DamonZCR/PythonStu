from tkinter import *
'''显示文本，这里使用了像素点，如果使用坐标se,e,w,s，center会更方便'''
root = Tk()
w = Canvas(root, width=200, heigh=100)
w.pack()
# 前两个参数代表起点，后两个代表终点，dash代表线的样式，虚线
w.create_line(0, 0, 200, 100, fill='green', width=3)
w.create_line(200, 0, 0, 100, fill='green', width=3)
w.create_rectangle(40, 20, 160, 80, fill='green')
w.create_rectangle(65, 35, 135, 65, fill='yellow')

w.create_text(100, 50, text='Damon')

mainloop()