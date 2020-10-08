'''输出文件夹下文件的大小（M）'''

import os
fileaddr = input('请输入目录地址:')


filename = list()
filesize = dict()#

#获取该路径下所有的文件名称
filename = os.listdir(fileaddr)

for onefile in filename:
    fileallname = fileaddr + onefile
    if os.path.isfile(fileallname):
        filesize[onefile] = os.path.getsize(fileallname)/(1024*1024)
for demodict in filesize:
    print(demodict+'大小为【%fM】'%filesize[demodict])
