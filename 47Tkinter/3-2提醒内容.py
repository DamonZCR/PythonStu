from tkinter import *
'''这里使用PhotoImage显示图片的时候只能使用gif格式'''
root = Tk()
root.iconbitmap('damon.ico')
photo = PhotoImage(file="aa.gif")
imageLabel = Label(root,
                   text='明天就要寒假\n放假回家啦!',
                   justify=LEFT, # 调整文字左对齐
                   image=photo,# 加入图片
                   compound=CENTER,# 在图片中间显示
                   font=('宋体',20),# 文字字体
                   fg='black')# 文字颜色
imageLabel.pack()
mainloop()