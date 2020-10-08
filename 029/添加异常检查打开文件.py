'''添加异常处理，当try里出现异常，仍然执行finally关闭文件'''
f = ''
try:
    f = open('d:/gx对话.txt', 'r', encoding='utf-8')
    print(f.read())
    num = 10 / 0
finally:
    print('>>>>>>finally')
    if f:
        f.close()
