from tkinter import *
'''使用列表添加更多的选项'''
OPTIONS = [
    "a",
    "458",
    "FF",
    "Es",
    "Law"
    ]
root = Tk()
variable = StringVar()
variable. set(OPTIONS[0])
# 需要给列表加上* 星号，它是一个解包的操作。
w = OptionMenu(root, variable, *OPTIONS)
w. pack()
mainloop()
