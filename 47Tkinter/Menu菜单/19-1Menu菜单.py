from tkinter import *
'''创建一个菜单'''
root = Tk()

def callback():
    print('你好~')
menubar = Menu(root)
menubar.add_command(label= "hello", command=callback)
# root.quit 退出窗口
menubar.add_command(label= "quit", command=root.quit)
root.config(menu=menubar)
mainloop()
