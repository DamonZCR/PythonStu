import os
import urllib.request


def cbk(a, b, c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)

url = 'https://www.python.org/ftp/python/doc/3.5.10/python-3.5.10-docs-html.tar.bz2'
dir = os.path.abspath('D:\\Download')
work_path = os.path.join(dir, 'python-3.5.10-docs-html.tar.bz2')
urllib.request.urlretrieve(url, work_path, cbk)