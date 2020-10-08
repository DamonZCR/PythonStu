'''无敌异常处理版之输出原因，不建议使用'''
try:
    f = open('我为什么会是一个文件.txt')
    print(f.read())
    f.close()
except:
    print('出错啦')
