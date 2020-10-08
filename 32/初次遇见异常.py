'''使用open打开一个不存在的文件会报错，
异常处理会捕获这个错误,而文件找不到这个异常
属于OSError这个异常里'''
try:
    f = open('我为什么会是一个文件.txt')
    print(f.read())
    f.close()
except OSError:
    print('出错啦')
