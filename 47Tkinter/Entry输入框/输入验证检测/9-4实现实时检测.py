from tkinter import *
'''使用冷却函数,
如果想要实现实时检测，使用简单的get()检测输入框，是不行的。
无法输入信息，并且控制台输出一栏为空，因为Entry的textvariable属性只有当验证函数返回为Ture
时才被赋值，所以get()的调用就是从它这里获取没有读取到。只有使用冷却函数注册'''
master = Tk()
def atest():
    if e1.get() == '111':
        print('正确')
        print(e1.get())
        return True
    else:
        print('错误')
        print(e1.get())
        return False
v = StringVar()
e1 = Entry(master, textvariable=v, validate='key',
           validatecommand=atest)
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()