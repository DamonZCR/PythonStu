from tkinter import *
from tkinter import colorchooser
"""colorchooser (颜色选择对话框)
颜色选择对话框提供一个友善的界面让用户选择需要的颜色
返回一个元组，第一元组值是RGB值，第二个值是RGB的十六进制，如果点击取消返回(None,None)
"""
root = Tk()
def callback():
    fileName = colorchooser.askcolor()
    print(fileName)
Button(root, text="选择颜色", command=callback).pack()

mainloop()
