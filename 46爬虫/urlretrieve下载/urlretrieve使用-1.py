import os
from urllib.request import urlretrieve

'''使用urlretrieve下载百度的HTML，并且显示下载进度。'''

def cbk(a, b, c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


url = 'http://www.baidu.com'
dir = os.path.abspath('D:\\Download')
work_path = os.path.join(dir, 'baidu.html')
urlretrieve(url, work_path, cbk)