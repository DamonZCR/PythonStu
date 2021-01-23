from tkinter import *
'''index(index)
--将index参数指定的位置以"line.column"的索弓|形式返回
index参数支持任何格式的索引
'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()
'''index 输入line.column的形式，返回Text中索引的形式，没发现用处'''
text.insert(INSERT, 'Damon is very hungray')
print(text.index(1.5))
pos = text.search('a', 1.0, stopindex=END)
print(pos)
mainloop()
