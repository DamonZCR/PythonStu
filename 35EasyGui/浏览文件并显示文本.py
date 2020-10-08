'''选择一个文本文件，首先创建选择文件的窗口，通过该窗口选择后返回的
文件的路径，通过文件打开，显示在文本窗口中'''
import easygui as g

addre = g.fileopenbox('选择文本文件啦','文本选择',default='d:/*.txt',filetypes='*.txt',)
try:
    with open(addre, 'r',encoding='UTF-8') as f:
        ss = g.textbox('文件【%s】'%addre,'显示文件内容',text=f)
except TypeError:
    print('取消选择文件！')
print(ss)   