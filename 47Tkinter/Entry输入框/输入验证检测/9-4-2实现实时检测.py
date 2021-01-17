from tkinter import *
'''使用冷却函数,实现实时检测，
实时检测是否输入的为数字，如果不是将清空输入框，但是当输入了111后再接着输入其他非数字，
将只会保留111，因为，当输入正确的数字后,验证函数返回Ture，将正确的值赋值给textvariable=v，
那么，框中的值还是保留的上次正确的textvariable=v的值。'''
master = Tk()
def atest(content):
    return content.isdigit()

v = StringVar()
testCMD = master.register(atest)
# %P就是根据输入框发生的任何改变而实时获取。
e1 = Entry(master, textvariable=v, validate='key',
           validatecommand=(testCMD, '%P'))
e2 = Entry(master)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()