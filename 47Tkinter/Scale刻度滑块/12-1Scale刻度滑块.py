from tkinter import *
'''使用get()方法可以获取当前滑块的位置'''
root = Tk()
s1 = Scale(root, from_=0, to=32)
s1.pack()
s2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
s2.pack()
def callvalue():
    print(s1.get(), s2.get())
Button(root,text='获取', command=callvalue).pack()

mainloop()
