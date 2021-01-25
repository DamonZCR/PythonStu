import tkinter as tk
'''首先anchor共有9个参数可以设置n, s, w, e ,nw, ne, sw, se, center. 分别是各个方向英语的缩写。
有一个注意点是，anchor 放置容器时是相对于每一行放置的，重点在控制每一个容器在每一行的位置比较有用。
如果要想实现相对于整个窗口的相对位置放置，可以参考side用法。'''
window = tk.Tk()
window.geometry("300x300")

tk.Button(window, text="1-North West").pack(anchor="nw")
tk.Button(window, text="2-North").pack(anchor="n")
tk.Button(window, text="3-North East").pack(anchor="ne")
tk.Button(window, text="4-West").pack(anchor="w")
tk.Button(window, text="5-East").pack(anchor="e")
tk.Button(window, text="6-South West").pack(anchor="sw")
tk.Button(window, text="7-South").pack(anchor="s")
tk.Button(window, text="8-South East").pack(anchor="se")
tk.Button(window, text="9-Center").pack(anchor="center")

window.mainloop()
