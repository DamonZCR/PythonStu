from tkinter import *

root = Tk()
# width参数表示30个字符的平均宽度。height代表两行。
text = Text(root, width=30, height=2)
text.pack()

# insert代表在光标处插入。
text.insert(INSERT, "今天好困，我需要\n")
text.insert(END, "早点睡")

mainloop()