from tkinter import *

root = Tk()
text = Text(root, width=30, height=30)
text.pack()
text.insert(INSERT, 'Damon wants to sleep')
print(text.get(1.2, 1.6))

print(text.get("1.2", "1.end"))



mainloop()