'''程序首先使用for遍历每一行，将每行加入到列表中，
之后对每一行中的替换词进行查找，若存在则+1，并记下
该行的行数。之后再对每一行进行写入文件，遇到记录中的
行数进行替换。注意r+是可读，写入时覆盖写入还是追加写入看情况。'''
addre = input('请输入文件名：')
front = input('请输入需要替换的单词或字符：')
toword = input('请输入新的单词或字符：')

ofile = open(addre, 'r+',encoding = 'UTF-8')
filelist = list(ofile)
countword = 0
i = 0
locate = []

for filelistline in filelist:
    if filelistline.count(front) != 0:
        countword += filelistline.count(front)
        locate.append(i)
    i += 1   
print('文件'+addre+'中共有'+str(countword)+'个【'+front+'】')
print('您确定要把所有的【'+front+'】替换为【'+toword+'】吗？')
choice = input('【YES/NO】：')

ofile.seek(0, 0)
if choice == 'YES':
    i = 0
    for filelistline in filelist:
        #print(filelistline,end='')
        if i in locate:
           filelistline = filelistline.replace(front, toword)
        i +=1
        ofile.writelines(filelistline)
ofile.close()
