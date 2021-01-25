from tkinter import*
import tkinter.messagebox as tk
"""askokcancel()，askretrycancel() 和askyesno()返回布尔类型的值:
●返回True表示用户点击了“确定”或“是”按钮
●返回False表示用户点击了“取消”或“否”按钮
askquestion)返回"yes" 或"no” 字符串表示用户点击了“是”或“否”按钮。
showerror()，showinfo()和showwarning0返回"ok” 表示用户按下了“是”按钮。
"""
# 确定和取消
print(tk.askokcancel("对话框", '1-提示内容！'))
# 问题询问，确定和取消
tk.askquestion("问题询问", "你想玩手机嘛？")
# 警告重试或取消
tk.askretrycancel("警告", "启动失败，重试？")
# 问题询问，是或者否
tk.askyesno("问题询问", "我帅吗?")
# 出错框，确定选项
tk.showerror("出错框", "出错啦！")
# 消息框，确定选项
tk.showinfo("消息框", "2021新年快乐")
# 警告框，确定选项
tk.showwarning("警告框", "你在偷懒！")



mainloop()