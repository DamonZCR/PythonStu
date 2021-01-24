import tkinter as tk
"""如果多个容器使用同一个side，那么将会按照从里到外的方向进行排列"""
window = tk.Tk()
window.geometry("250x250")

tk.Label(window, text="1", bg="green").pack(side="left")
tk.Label(window, text="2", bg="green").pack(side="left")

tk.Label(window, text="3", bg="red").pack(side="right")
tk.Label(window, text="4", bg="red").pack(side="right")

tk.Label(window, text="5", bg="yellow").pack(side="top")
tk.Label(window, text="6", bg="yellow").pack(side="top")

tk.Label(window, text="7", bg="pink").pack(side="bottom")
tk.Label(window, text="8", bg="pink").pack(side="bottom")

window.mainloop()
