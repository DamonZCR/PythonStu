from tkinter import *
'''创建次级菜单
Menu都带有一个叫做tearoff的属性，他的作用是撕开，即将这个菜单栏单独的
生成一个窗口分裂出来Menu都带有一个叫做tearoff的属性，他的作用是撕开，
即将这个菜单栏单独的生成一个窗口分裂出来'''
root = Tk()

def callback():
    print("你好~")
menubar = Menu(root)
# 创建次菜单，将要显示的次菜单加入到主菜单中。
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
# 添加横线
filemenu.add_separator()
filemenu.add_command(label= "退出", command=root.quit)
# 添加到主菜单中
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label= "剪切", command=callback)
editmenu.add_command(label="拷贝", command=callback)
editmenu.add_command(label="黏贴", command=callback)
menubar.add_cascade(label="编辑", menu=editmenu)
root.config(menu=menubar)
mainloop()
