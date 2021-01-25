from tkinter import *
'''这里使用PhotoImage显示图片的时候只能使用gif格式'''
def callback():
    var.set('我进来了！')
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
var = StringVar()# 设置为可变类型
var.set('请不要访问！')
textLabel = Label(frame1, textvariable=var,
                  justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)
photo = PhotoImage(file="布局管理器/aa.gif")
imageLabel = Label(frame1, image=photo)
imageLabel.pack(side=RIGHT)

button = Button(frame2, text='我想要访问', command=callback)
button.pack()
frame1.pack()
frame2.pack()
mainloop()