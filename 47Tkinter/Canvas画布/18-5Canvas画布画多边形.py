from tkinter import *
import math as m
root = Tk()
w = Canvas(root, width=200, height=100, background= "red")
w. pack()
center_x = 100
center_y = 50
r =50
points = [
    #左上点
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    #右上点
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    #左下点
    center_x - int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
    #顶点
    center_x,
    center_y - r,
    #右下点
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5))
    ]
# 当变为包围的图形才会填充颜色，如果fill这个属性直接不给，会使用黑色填充，如果给出却为空就使用透明色
w.create_polygon(points, outline="black", fill="yellow")
mainloop()
