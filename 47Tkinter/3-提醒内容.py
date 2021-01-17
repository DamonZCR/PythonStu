from tkinter import *
'''这里使用PhotoImage显示图片的时候只能使用gif格式'''
root = Tk()

textLabel = Label(root, text='请不要访问！',
                  justify=LEFT,
                  padx=10) # 文字左对齐，已经行间距为10
textLabel.pack(side=LEFT)

photo = PhotoImage(file="aa.gif")
imageLabel = Label(root, image=photo)
imageLabel.pack(side=RIGHT)

mainloop()

