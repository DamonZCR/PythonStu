import easygui as g

num = g.integerbox('测试输入数字：','数字输入',upperbound=10)
print(num)