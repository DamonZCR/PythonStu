'''程序的不足之处：1，只能比较两个相同行的文件，文件总行数不同报错。(已解决)
2，将文件2转换成列表内存占用是否增多'''

file1_sourse = input('请输入需要比较的头一个文件名:')
file2_sourse = input('请输入需要比较的另一个文件名:')
file1 = open(file1_sourse, 'r')
file2 = open(file2_sourse, 'r')

i = 0
file2_lines = list(file2)
worlist = list()
for file1_line in file1:
    if i < len(file2_lines):
        if file1_line != file2_lines[i]:
            worlist.append(str(i))
    else:
        worlist.append(str(i))
    i +=1
print('两个文件共有【'+str(len(worlist))+'】处不同',)


file1.close()
file2.close()
      
