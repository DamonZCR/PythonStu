from tkinter import *
'''使用焦点判断，当焦点移出这个输入框时，就开始执行检测，
如果输入值与要求值相同就输出正确，否则错误，其中，focusout为移出检测，
还可以使用其他几种。'''
master = Tk()
def atest():
    if e1.get() == '111':
        print('正确')
        return True
    else:
        print('错误')
        return False
v = StringVar()
e1 = Entry(master, textvariable=v, validate='focusout',
           validatecommand=atest)
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)

mainloop()