from tkinter import *
'''显画出一个椭圆'''
root = Tk()
w = Canvas(root, width=200, heigh=100)
w.pack()
# 前两个参数代表起点，后两个代表终点，dash代表线的样式，虚线
w.create_rectangle(40, 20, 160, 80, dash=(4, 4))
w.create_oval(40, 20, 160, 80, fill='pink')
w.create_text(100, 50, text='Damon')

w2 = Canvas(root, width=200, heigh=100)
w2.pack()
w2.create_rectangle(40, 20, 160, 80, dash=(4, 4))
w2.create_oval(70, 20, 130, 80, fill='pink')
w2.create_text(100, 50, text='Damon')
mainloop()