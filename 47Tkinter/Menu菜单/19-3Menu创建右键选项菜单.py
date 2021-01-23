from tkinter import *
'''创建一个菜单'''
root = Tk()

def callback():
    print('你好~')
menubar = Menu(root)
menubar.add_command(label= "hello", command=callback)
menubar.add_command(label= "quit", command=root.quit)
frame = Frame(root, width=100, height=130)
frame.pack()
def popup(event):
    menubar.post(event.x_root, event.y_root)

# 绑定鼠标左键事件,,<Button-1>是单次点击鼠标左键，<Button-2>单击鼠标中间键<Button-3>单次鼠标右键
frame.bind("<Button-3>", popup)
mainloop()
