from tkinter import *
'''创建PanedWindow进行窗口的布局管理，实现分模块'''
# 创建一个总的模块,开启横线和手柄，手柄的位置是可以调节的，默认是在8的位置。
m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN)
# 填充方式fill为BOTH为布满全局
m1.pack(fill=BOTH, expand=1)
left = Label(m1, text="left pane")
m1.add(left)
m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)
bottom = Label(m2, text="bottom")
m2.add(bottom)
mainloop()

