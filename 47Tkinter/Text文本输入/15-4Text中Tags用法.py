from tkinter import *
import webbrowser
'''将文本( "Baidu.com" )与鼠标事件进行绑定，当鼠标进入该文本段的时候，
鼠标样式切换为"arrow"形态，离开文本段的时候切换回”xterm”形态。
当触发鼠标“左键点击操作”事件的时候，使用默认浏览器打开百度首页( www.baidu.com ) 
'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Damon doing web')
text.tag_add('link', '1.12','1.end')
text.tag_config('link', foreground='blue', underline=True)
# 当光标放置到文字上时，光标改变为点击
def show_arrow_cursor(event):
    text.config(cursor='arrow')
# 当光标离开时设置为编辑
def show_xterm_cursor(event):
    text.config(cursor='xterm')
# 当当点击此链接时
def click(event):
    webbrowser.open('http://www.baidu.com')
#<Enter>代表光标进入此文件区域，<Leave>代表离开，<Button-1>代表鼠标左键点击
text.tag_bind('link', '<Enter>', show_arrow_cursor)
text.tag_bind('link', '<Leave>', show_xterm_cursor)
text.tag_bind('link', '<Button-1>', click)
mainloop()

