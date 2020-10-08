'''查找目录下指定文件名的文件,原理是，将目录下的
文件及文件夹加入到列表中，采用递归进入文件夹。
'''

import os

def findfile(addr,filename):
    #获取该路径下所有的文件及文件夹名称
    #建立新的列表，存储当前文件夹下的所有,注意这里的列表是局部变量
    inallfile = list()
    inallfile = os.listdir(addr)
    for onefile in inallfile:
        newaddr = addr + onefile
        if os.path.isfile(newaddr):#第二思路：如果使用in来判断当前列表的该文件是否存在，
            if onefile == filename:
                thefile.append(newaddr)
            '''else:
                inallfile.remove(onefile)'''
        else:
            findfile(newaddr+'\\', filename)
    del inallfile





fileaddr = input('请输入查找地址:')
filename = input('请输入要查找的文件名:')

thefile = list()#查找到的文件路径

findfile(fileaddr+'\\', filename)
for afile in thefile:
    print(afile)
