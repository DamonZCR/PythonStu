from tkinter import *
'''使用冷却函数,validatecommand=(f, s1, s2,…..)其中，
f就是“冷却后”的验证函数名，s1,s2,s3这些事额外的选项，这些选项会作为参数一次传给f 函数。
冷却就是调用register() 将验证函数包装起来使用。'''
master = Tk()
def atest(content, reason, name):
    if content == '111':
        print('正确')
        print(content, reason, name)
        return True
    else:
        print('错误')
        print(content, reason, name)
        return False
v = StringVar()
testCMD = master.register(atest)
e1 = Entry(master, textvariable=v, validate='focusout',
           validatecommand=(testCMD, '%P', '%v', '%W'))
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()