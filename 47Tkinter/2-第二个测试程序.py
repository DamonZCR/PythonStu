import tkinter as tk

class App:
         def __init__(self, master):
                  frame = tk.Frame(master)# 创建一个模块
                  frame.pack(side=tk.LEFT, padx=10,pady=20)# 设置这个模块的位置
                  # 设置这个按钮的前景色，背景色和按钮的事件。
                  self.hi_there = tk.Button(frame, text='打招呼',bg='black',fg='white',command=self.say_hi)
                  self.hi_there.pack()

         def say_hi(self):
                  print('你好')
root = tk.Tk()
app = App(root)
root.mainloop()
