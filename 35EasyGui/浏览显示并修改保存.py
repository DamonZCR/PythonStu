'''选择一个文本文件，首先创建选择文件的窗口，通过该窗口选择后返回的
文件的路径，通过文件打开，显示在文本窗口中,可以修改文件，并且提示是否保存
或者另存为'''
import easygui as g

addre = g.fileopenbox(
    '选择文本文件啦', '文本选择', default='d:/*.txt', filetypes='*.txt')
flag = 0
try:
    with open(addre, 'r', encoding='UTF-8') as f:
        textstr = g.textbox('文件【%s】' % addre, '显示文件内容', text=f)
        if textstr != f.read():
            flag = 1
    if flag == 1:
        value = g.buttonbox('检测到文件内容发生改变，请选择一下操作：',
                            '提示',choices=('覆盖保存','放弃保存','另存为'),
                            default_choice='覆盖保存',cancel_choice='放弃保存')
        if value == '覆盖保存':
            with open(addre, 'w', encoding='UTF-8') as f:
                f.write(textstr)
        elif value == '放弃保存':
            pass
        elif value == '另存为':
            newaddre = g.filesavebox(
                        '另存为', '路径选择', default='d:/新文件.txt', filetypes='*.txt')
            with open(newaddre, 'w', encoding='UTF-8') as f:
                f.write(textstr)
except TypeError:
    print('取消选择文件！')

