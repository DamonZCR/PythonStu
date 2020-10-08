def CheckBac(str1):
    str2 = list(str1)
    str3 = str2.copy()
    str3.reverse()
    if str3 == str2:
        print('是回文联！')
    else:
        print('不是回文联！')
temp = input('请输入一句话：')
CheckBac(temp)
