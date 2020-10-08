'''查找目录下指定视频文件,原理是，。
'''

import os

#查找视频
def findfile(addr):
    #获取该路径下所有的文件及文件夹名称
    #建立新的列表，存储当前文件夹下的所有,注意这里的列表是局部变量
    inallfile = list()
    inallfile = os.listdir(addr)
    for onefile in inallfile:
        newaddr = addr + onefile
        if os.path.isfile(newaddr):#第二思路：如果使用in来判断当前列表的该文件是否存在，
            name = os.path.splitext(onefile)#或使用字符串中的endswith()函数
            if name[1] in movie:
                thefile.append(newaddr)
        else:
            findfile(newaddr+'/')
    del inallfile

#输出视频路径
def outfile(thefile, outaddr):
    f = open(outaddr+'/videolist.txt', 'x')
    for oneline in thefile:
        f.write(oneline+'\n')
    f.close()

addr = input('请输入查找地址:')

thefile = list()#查找到的文件路径
#视频格式
movie = ['.mp4','.MP4','.avi','.AVI','.rmvb','.RMVB']

findfile(addr+'/')
outfile(thefile, addr)
