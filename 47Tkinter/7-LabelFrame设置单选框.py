from tkinter import *
'''LabelFrame实现'''
root = Tk()
root.geometry('500x500')   #窗口大小
root.iconbitmap('damon.ico')
group = LabelFrame(root, text='谁是好用的语言？', padx=5,pady=5)
group.pack(padx=10, pady=10)

langs = [('Python', 1), ('Perl', 2), ('Java', 3), ('PHP', 4)]
v = IntVar()
for lang, num in langs:
    b = Radiobutton(group, text=lang, variable=v, value=num)\
        .pack()
mainloop()