from tkinter import *
'''改变按钮的方式，以及填充方式。'''
root = Tk()
v = IntVar()
v.set(1)
langs = [('Python', 1),('Perl',2),('Java',3),('PHP',4)]
for lang, num in langs:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)\
        .pack(anchor=W)
# mainloop()

root2 = Tk()
v2 = IntVar()
v2.set(1)
langs = [('Python', 1),('Perl',2),('Java',3),('PHP',4)]
for lang, num in langs:
    b = Radiobutton(root2, text=lang, variable=v2, value=num, indicatoron=False)\
        .pack(fill=Y)
mainloop()