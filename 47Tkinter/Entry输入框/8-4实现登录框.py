from tkinter import *

root = Tk()
la1 = Label(root,text='账号：').grid(row=0, column=0)
la2 = Label(root,text='密码：').grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root,show='*')
e2.grid(row=1, column=1)
def getword():
    print('账号：%s'% e1.get())
    print('密码：%s'% e2.get())
button1 = Button(root,text='登录',command=getword)\
    .grid(row=3,column=0,sticky=W,padx=10,pady=5)
button2 = Button(root,text='退出',command=root.quit)\
    .grid(row=3,column=1,sticky=E,padx=10,pady=5)
mainloop()
