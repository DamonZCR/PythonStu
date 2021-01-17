from tkinter import *
'''通过实时监测，要求输入框内必须为数字，加法计算器'''
master = Tk()
frame = Frame()
frame.pack(padx=10, pady=10)
def atest(content):
    return content.isdigit()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
testCMD = master.register(atest)
# %P就是根据输入框发生的任何改变而实时获取。
e1 = Entry(frame,width=10, textvariable=v1, validate='key',validatecommand=(testCMD, '%P'))\
    .grid(row=0, column=0, padx=10,pady=5)
str1 = Label(frame, text='+').grid(row=0, column=1, padx=10,pady=5)
e2 = Entry(frame, width=10, textvariable=v2, validate='key',validatecommand=(testCMD, '%P'))\
    .grid(row=0, column=2, padx=10,pady=5)
str2 = Label(frame, text='=').grid(row=0, column=3, padx=10,pady=5)
e3 = Entry(frame, width=10, textvariable=v3, state="disabled")\
    .grid(row=0, column=4, padx=10,pady=5)

def calculate():
    v3.set(int(v1.get())+int(v2.get()))

button = Button(frame, text='计算', command=calculate)\
    .grid(row=1, column=2, padx=10,pady=5)
mainloop()