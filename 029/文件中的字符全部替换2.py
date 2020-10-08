'''问题很多，新写入的会追加到最后，并且不能统计总数'''
#统计总数已经解决，需要注意文件指针位置

addre = input('请输入文件名：')
front = input('请输入需要替换的单词或字符：')
toword = input('请输入新的单词或字符：')

ofile = open(addre, 'r+',encoding = 'UTF-8')
filelist = list(ofile)
countword = 0

ofile.seek(0, 0)
for ofiline in ofile:
    countword += ofiline.count(front)
    print(ofiline,end='')

print('文件'+addre+'中共有'+str(countword)+'个【'+front+'】')
print('您确定要把所有的【'+front+'】替换为【'+toword+'】吗？')
choice = input('【YES/NO】：')

ofile.seek(0, 0)
if choice == 'YES':
    for ofiline in ofile:
        ofiline = ofiline.replace(front, toword)
        ofile.writelines(ofiline)

ofile.close()
