from urllib.request import urlretrieve
import os
'''urlopen()可以轻松获取远端html页面信息，然后通过Python正则对所需要的数据进行分析，
匹配出想要用的数据，再利用urlretrieve()将数据下载到本地。
这个程序还是只能用在下载无反爬虫的下载中，不能加上浏览器标识。'''

def download(url, savepath='D:\\Download'):
    def reporthook(a, b, c):
        """
        显示下载进度
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件大小
        :return: None
        """
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")

    filename = os.path.basename(url)
    # 判断文件是否存在，如果不存在则下载
    if not os.path.isfile(os.path.join(savepath, filename)):
        print('Downloading data from %s' % url)
        urlretrieve(url, os.path.join(savepath, filename), reporthook=reporthook)
        print('\nDownload finished!')
    else:
        print('File already exsits!')
    # 获取文件大小
    filesize = os.path.getsize(os.path.join(savepath, filename))
    # 文件大小默认以Bytes计， 转换为Mb
    print('File size = %.2f Mb' % (filesize / 1024 / 1024))


if __name__ == '__main__':
    # 以下载cifar-10数据集为例
    url = "https://www.python.org/ftp/python/doc/3.5.10/python-3.5.10-docs-html.tar.bz2"
    download(url, savepath='D:\\Download')