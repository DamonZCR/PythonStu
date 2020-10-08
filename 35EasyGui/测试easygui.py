import sys
import easygui as g

while 1:
    g.msgbox('嗨，欢迎使用第一个界面小游戏！')

    msg = '请问你希望更喜欢什么数据类型？'
    title = '小游戏互动'
    choices = ['列表','元组','字典','集合']
    choice = g.choicebox(msg,title,choices)
    #如果用户当即 关闭窗口将提示：你的选择是None
    g.msgbox('你的选择是：'+str(choice),'结果')

    msg = '你希望重新开始选吗？'
    title = '请选择'
    if g.ccbox(msg,title):
        #直接通过
        pass
    else:
        sys.exit(0)