addr = input('请输入要打开的文件：')
goal = input('请输入显示的行数【格式:13:21或:21或21:】：')
ofile = open(addr, encoding='utf-8')
body = goal.split(':')

#将文件转换成列表形式
filelist = list(ofile)

if body[0] == '' and body[1] != '':
    print(addr+'从开始到第'+body[1]+'行的内容如下：')
    toend = int(body[1])
    for fline in filelist[:toend]:
        print(fline,end='')
elif body[0] != '' and body[1] != '':
    form, toend = int(body[0]), int(body[1])
    print(addr+'从第'+body[0]+'到第'+body[1]+'行的内容如下：')
    for fline in filelist[form:toend]:
        print(fline,end='')
elif body[0] != '' and body[1] == '':
    form = int(body[0])
    print(addr+'从第'+body[0]+'到末尾的内容如下：')
    for fline in filelist[form:]:
        print(fline,end='')
elif body[0] == '' and body[1] == '':
    print(addr+'从开始到末尾的内容如下：')
    for fline in filelist[:]:
        print(fline,end='')

ofile.close()
