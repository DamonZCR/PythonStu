from tkinter import *
root = Tk()
e = Entry(root)
e.pack(padx=10,pady=10)

e.insert(0, 'wocaowuqing!')
e.delete(0, 8)
# e.delete(0, END)
e.insert(0, '默认文本')
# normal、disabled和readonly
# 只有这种才能给输入框加上初始值。
v = StringVar()
v.set('eee')
e2 = Entry(root, textvariable=v, state='disabled')
e2.pack(padx=10,pady=10)
mainloop()