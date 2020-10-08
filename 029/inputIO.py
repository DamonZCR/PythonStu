file_name = input('请输入文件名：')
if file_name == '':
    file_name = input('文件名不能为空，请重新输入：')
file1 = open('d:/'+str(file_name), 'x')

inputStr = ''
print('请输入内容【单独输入\':w\'保存退出】:')
while 1:
    inputStr = input()
    if inputStr == ':w':
        break
    file1.write(inputStr+'\n')
file1.close()
