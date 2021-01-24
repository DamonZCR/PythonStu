import tkinter as tk
'''1.简单来说就是padx和pady表示的是2个容器，或者是容器和边框之间需要的间距(x是上和下对称，y是左和右对称)
2.ipadx和ipady表示容器的内容和容器边框之间的距离，同样是对称的；'''

window = tk.Tk()
tk.Button(window, text="Button-1").pack()
tk.Button(window, text="Button-2").pack(padx=50, pady=10)
window.mainloop()


