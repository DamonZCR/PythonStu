from tkinter import *
'''for实现多个选框'''
root = Tk()
v = IntVar()
v.set(1)
langs = [('Python', 1),('Perl',2),('Java',3),('PHP',4)]
for lang, num in langs:
    b = Radiobutton(root, text=lang, variable=v, value=num)\
        .pack(anchor=W)
mainloop()