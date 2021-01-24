from tkinter import *

"""Toplevel (顶级窗口)组件类似于Frame组件，但Toplevel组件是一个独立的顶级窗口，
attribute属性的使用与设置"""
root = Tk()


def create():
    top = Toplevel()
    top.title("Damon")
    # 设置Toplevel窗口为透明并且一直位于顶层,"-toolwindow", True工具窗口，即只带右上角的关闭选项
    top.attributes("-alpha", 0.9, "-topmost", True, "-toolwindow", True)
    msg = Message(top, text="现在是晚上23点39分！")
    msg.pack()


Button(root, text="创建顶级窗", command=create).pack()
mainloop()
