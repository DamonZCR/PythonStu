'''判断此目录下的每个文件类型文件数.
使用字典的存储后缀名作为键，数量作为字典对应的值'''

import os
fileaddr = input('请输入目录地址:')


filename = list()
filexten = dict()#保存文件后缀名以及对应后缀名文件的个数

#获取该路径下所有的文件名称
filename = os.listdir(fileaddr)

for onefile in filename:
    fileallname = fileaddr + onefile
    if os.path.isfile(fileallname):
        filepart = os.path.splitext(onefile)
        #使用字典，对应的文件后缀名+1,若字典中不存在这个键则创建
        if filepart[1] in filexten:
            filexten[filepart[1]] = filexten[filepart[1]] + 1
        else:
            filexten[filepart[1]] =+ 1
        
    #似乎不是文件就是文件夹了，所以这个判断能省嘛?
    elif os.path.isdir(fileallname):
        if '文件夹' in filexten:
            filexten['文件夹'] = filexten['文件夹'] + 1
        else:
            filexten['文件夹'] =+ 1
for dictvalue in filexten:
    print('该文件夹下共有类型为【%s】的文件%d'%(dictvalue,filexten[dictvalue]))
