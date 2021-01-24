import tkinter as tk
'''expand参数表示的是容器在整个窗口上，将容器放置在剩余空闲位置上的中央(包括水平和垂直方向)
expand=1或者expand=“yes”，表示放置在中央
expand=0或者expand=“no”，表示默认不扩展'''
window = tk.Tk()
window.geometry("150x150")
tk.Button(window, text="Button-1", bg="green").pack(expand="yes")
tk.Button(window,text="Button-2",bg="yellow").pack(expand="no")
#tk.Button(window,text="Button-3",bg="yellow").pack()
window.mainloop()
