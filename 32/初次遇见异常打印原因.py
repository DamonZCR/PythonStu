'''打印原因'''
try:
    f = open('我为什么会是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('出错啦,错误的原因是：'+str(reason))
