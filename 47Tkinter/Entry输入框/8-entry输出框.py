from tkinter import *
root = Tk()
e = Entry(root)
e.pack(padx=10,pady=10)

e.insert(0, 'wocaowuqing!')
e.delete(0, 8)
# e.delete(0, END)
e.insert(0, '默认文本')
mainloop()