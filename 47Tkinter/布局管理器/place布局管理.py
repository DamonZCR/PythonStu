from tkinter import *
"""通常用于
1)将子组件显示在父组件的正中间"""
root = Tk()
def callback():
    print("正中靶心! ")
Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor="center")
mainloop()

