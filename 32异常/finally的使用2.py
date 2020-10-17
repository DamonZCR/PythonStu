'''如果打开一个文件，在使用中出现异常，那么缓冲区里的
数据就没法写入了，这时使用finally可以读取缓冲区.
原理上是以上，但是上个文件没有加finally还是读取了缓冲区。。。
大概加上finally更安全'''
try:
    f = open('已存在文件.txt','w',encoding='UTf-8')
    print(f.write('末尾追加上我哦。'))
    sum = 1 + '1'
except (OSError,TypeError) as reason:
    print('出错啦，出错原因是：'+str(reason))
finally:
    f.close()
