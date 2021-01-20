from tkinter import *
root = Tk()
# width参数表示30个字符的平均宽度。height代表两行。
text = Text(root, width=30, height=5)
text.pack()

# insert代表在光标处插入。
text.insert(INSERT, "今天好困，我需要早睡\n")
def show():
    print('你碰到我了哦！')
b1 = Button(text, text='按钮', command=show)
# 需要创建按钮的窗口，进行刷新
text.window_create(INSERT, window=b1)

mainloop()