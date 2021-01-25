import tkinter as tk
'''fill表示的是容器相对于整个窗口是否进行填充，这个参数的优先级高于width和heigh；有三个选项可以配置，
fill=“x”，表示横向填充
fill=“y”，表示纵向填充
fill=“both”，表示横向和纵向都填充
上面几个填充选项当和side同时使用时需要注意：
当side="left"或side="right"时，fill="x"不起作用，只能填充y
side=“top”,side="bottom"时，fill="y"不起作用，只能填充x
'''
window = tk.Tk()
window.geometry("150x150")

tk.Label(window, text="上边", bg="green").pack(fill="x", side="top")
tk.Label(window, text="下边", bg="red").pack(fill="y", side="bottom")
tk.Label(window, text="左边", bg="green").pack(fill="y", side="left")
tk.Label(window, text="右边", bg="red").pack(fill="x", side="right")
tk.Button(window, text="中间", bg="yellow").pack(expand="yes")

window.mainloop()
