from tkinter import *
'''1,设置某一区域的字符串改变，
    2,设置输入框里的值同步得到。'''
def callback():
    var.set('我进来了！')
root = Tk()
# 创建两个框架
frame1 = Frame(root)
frame2 = Frame(root)
# 设置初始字符
var = StringVar()# 设置为可变类型
var.set('请不要访问！')
textLabel = Label(frame1, textvariable=var,
                  justify=LEFT,
                  padx=10)
textLabel.pack()
button = Button(frame2, text='我想要访问', command=callback)
button.pack();frame1.pack();frame2.pack()

frame3 = Frame(root)
var2 = StringVar()
e1 = Entry(frame3, textvariable=var2)
e2 = Entry(frame3,textvariable=var2)
e1.pack();e2.pack();frame3.pack()
mainloop()