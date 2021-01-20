from tkinter import *

master = Tk()

thelb = Listbox(master)
thelb.pack()

for item in ['a','b','c','d','e','f','g','h']:
         thelb.insert(END, item)

# 代表删除第二个选项。
thelb.delete(1)
#代表删除第二个选项。
thelb.delete(0, END)
mainloop()
