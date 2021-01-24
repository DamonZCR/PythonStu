from tkinter import *

"""Toplevel (顶级窗口)组件类似于Frame组件，但Toplevel组件是一个独立的顶级窗口，
这种窗口通常拥有标题栏、边框等部件。
何时使用Toplevel组件?
Toplevel组件通常用在显示额外的窗口、对话框和其他弹出窗口上。"""
root = Tk()


def create():
    top = Toplevel()
    top.title("Damon")
    msg = Message(top, text="现在是晚上23点39分！")
    msg.pack()


Button(root, text="创建顶级窗", command=create).pack()
mainloop()
