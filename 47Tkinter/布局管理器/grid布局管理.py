from tkinter import *
"""使用grid排列组件，只需告诉它你想要将组件放置的位置(行/列，row选项指定行，
cloumn选项指定列)。此外,你并不用提前指出网格(grid分布给组件的位置称为网格)的尺寸，
因为管理器会自动计算。"""

root = Tk()
Label(root, text="用户名").grid(row=0, sticky=W)
Label(root, text="密码").grid(row=1, sticky=W)
photo = PhotoImage(file="aa.gif")

# rowspan可实现跨行，即有的东西使用grid一行显示不完，就需要跨行显示
Label(root, image=photo).grid(row=0, column=2, rowspan=2)
Entry(root).grid(row=0, column=1)
Entry(root, show="*").grid(row=1, column=1)

# columnspan=3 跨三列
Button(text='提交', width=10).grid(row=2, columnspan=3, pady=5)
mainloop()
