from tkinter import *
'''使用焦点判断，当焦点移出这个输入框时，就开始执行检测，
如果输入值与要求值相同就输出正确，否则错误，错误的话就执行invalidcommand
的执行功能,可反复检测。'''
master = Tk()
def atest():
    if e1.get() == '111':
        print('正确')
        return True
    else:
        print('错误')
        e1.delete(0, END)
        return False
def btest():
    print('错误情况下，我被调用啦')
    return True
v = StringVar()
e1 = Entry(master, textvariable=v, validate='focusout',
           validatecommand=atest, invalidcommand=btest)
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()