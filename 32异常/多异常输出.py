try:
    sum = 1 + '1'
    f = open('我为什么会是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('出错啦，出错原因是：'+str(reason))
except TypeError as reason:
    print('出错啦，出错原因是：'+str(reason))
