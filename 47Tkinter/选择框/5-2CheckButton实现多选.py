from tkinter import *
'''多选框'''
root = Tk()
word = ['明天','回家', '坐飞机', '去郑州']
v = []
for choic in word:
    v.append(IntVar())
    Checkbutton(root, text=choic, variable=v[-1])\
        .pack(anchor='w')
for i in range(len(v)):
    Label(root, textvariable=v[i]).pack(anchor='center')
mainloop()