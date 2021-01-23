from tkinter import *
'''通过设定初始值(或为空)来进行下拉选择，选择成功后会返回选择的值'''
root = Tk()

variable = StringVar()
variable.set("one")
w = OptionMenu(root, variable, "one", "two", "three")
w.pack()
Label(root, textvariable=variable).pack()
mainloop()
