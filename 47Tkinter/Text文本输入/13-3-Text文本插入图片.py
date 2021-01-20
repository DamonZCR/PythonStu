from tkinter import *
'''在Text组件中插入图片，其中需要用到创建图片窗口'''
root = Tk()
# width参数表示30个字符的平均宽度。height代表两行。
text = Text(root, width=30, height=100)
text.pack()

# insert代表在光标处插入。
text.insert(INSERT, "今天好困，我需要早睡\n")
photo = PhotoImage(file='D:\\PythonPro\FStudy\\47Tkinter\\aa.gif')

def show():
    text.image_create(END, image=photo)
b1 = Button(text, text='按钮', command=show)
text.window_create(INSERT, window=b1)

mainloop()