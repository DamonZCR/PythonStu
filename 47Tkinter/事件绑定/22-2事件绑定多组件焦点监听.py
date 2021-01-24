from tkinter import *
'''生成两个组件，当运行时焦点会集中在第二个组件中，第一个组件即点击键盘无反应，
点击鼠标在第二个组件中有反应，当点击Tab键后，第一个组件有反应，takefocus就是
将焦点移动到自己的。focus_set是一运行就获取焦点。takefocus是点击Tab键获取。'''
root = Tk()
def callback(event):
    # event.char会得到点击的某一个按键
    print('点击按键：', event.char)
def callback2(event):
    # event.char会得到点击的某一个按键
    print('点击位置：', event.x, event.y)
frame = Frame(root, width=200, height=200, takefocus=True)
frame.bind("<Key>", callback)
frame.pack()

frame2 = Frame(root, width=200, height=200)
frame2.bind("<Button-1>", callback2)
frame2.pack()

mainloop()