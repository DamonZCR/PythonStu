from tkinter import *

root = Tk()
def callback(event):
    """event.char会得到点击的某一个按键。.char会显示字母名，
    但是对于ALT和其他控制键不会显示，这些键会需要使用下面这个keysym形式显示
    event.keycode显示出按键的具体数字编码"""
    print('点击按键：', event.char, event.keysym, event.keycode)
frame = Frame(root, width=200, height=200)
# 事件由<Key>、<KeyPress>、<KeyRelease>分别是键盘，键盘按下，键盘松开后面添加'-'跟上具体的按键也可以
frame.bind("<Key>", callback)
frame.focus_set()
frame.pack()

mainloop()