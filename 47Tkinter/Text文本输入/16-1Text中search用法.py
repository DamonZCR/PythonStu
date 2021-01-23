from tkinter import *
'''使用search方法，查找字符'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Damon is very hungray')

def getindex(text, index):
    return tuple(map(int, str.split(text.index(index), '.')))

start = '1.0'
while True:
    pos = text.search('a', start, stopindex=END)
    if not pos:
        break
    print('位置为：', getindex(text, pos))
    start = pos + '+1c'

mainloop()