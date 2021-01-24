import tkinter as tk

app = tk.Tk()
app.title('zlw')
app.iconbitmap('damon.ico')
theLabel = tk.Label(app, text='第一个窗口')
theLabel.pack()# 设置这个模块的位置

app.mainloop()# 启动运行
