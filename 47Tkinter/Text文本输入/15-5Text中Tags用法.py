from tkinter import *
import hashlib
'''使用Hash判断文本内容是否发生改变
'''
root = Tk()
text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Damon doing web')
contents = text.get('1.0', END)

def getdigest(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()
sig = getdigest(contents)

def check():
    cont = text.get('1.0', END)
    if sig != getdigest(cont):
        print('警告：文本被改动！')
    else:
        print('OK!')
Button(root, text='检查', command=check).pack()
mainloop()

