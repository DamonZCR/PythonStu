str1 = input('请输入要打开的文件：')
ofile = open(str1,'r')
str2 = input('请输入需要显示该文件前几行：')
i = 0
for fileline in ofile:
    if i < int(str2):
        print(fileline,end='')
    i+=1
ofile.close()
