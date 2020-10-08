try:
    f = open('d:/不存在文件.txt','r')
    print(f.read())
    sum = 1 + '1'
except (OSError,TypeError) as reason:
    print('出错啦，出错原因是：'+str(reason))
finally:
    if 'f' in locals():#如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()
