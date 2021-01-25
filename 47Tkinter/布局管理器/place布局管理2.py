from tkinter import *
"""通常用于
2）组件覆盖另一个组件"""
root = Tk()
photo = PhotoImage(file="aa.gif")
Label(root, image=photo).pack()

def callback():
    print("正中靶心! ")
Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor="center")
mainloop()

