from tkinter import *
'''创建PanedWindow进行窗口的布局管理，注意这里没有使用Tk()类对象，
并且这里面的组件是可以拖拉改变大小的，showhandle=False是线条的手柄，当为True时开启，
sashrelief=SUNKEN代表开启线条。'''
# 规定了面板的朝向，此为竖直铺平
m = PanedWindow(orient=VERTICAL, showhandle=False, sashrelief=SUNKEN)
m. pack(fill=BOTH, expand=1)
top = Label(m, text="top pane")
m. add(top)

bottom = Label(m, text="bottom pane")
m. add(bottom)
mainloop()
