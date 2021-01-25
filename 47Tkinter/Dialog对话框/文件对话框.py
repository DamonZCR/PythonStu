from tkinter import *
from tkinter import filedialog
"""以上导入* 还并不能把这个模块的所有的功能导入！非要单独导入才可以
"""
root = Tk()

def callback():
    # 打开选择文件框
     fileName = filedialog.askopenfilename(defaultextension=".jpg")
     print(fileName)
    # 打开另存为框,返回值是一个对象，怎么用？
    # 它会返回一个空的文件对象，包含了对象的位置和需要规定的属性如后缀，可以用于写入
     savefile = filedialog.asksaveasfile()
     print(type(savefile))
Button(root,text='打开文本',command=callback).pack()
mainloop()