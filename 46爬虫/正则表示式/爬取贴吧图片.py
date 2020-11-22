import urllib.request
import time
import re
'''使用正则爬取贴吧图片，这个程序只是输出个网址。'''

def getHtml(url):
    # 生成request对象
    res = urllib.request.Request(url)
    # 使用第二种方法add_header()隐藏 py
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/86.0.4240.111 Safari/537.36')
    response = urllib.request.urlopen(res)
    # 网页刚获取的时候是二进制形式或Utf-8，如果对网页进行查找或者分片之类的需要解码成Unicode形式。
    html = response.read().decode('utf-8')
    # 线程睡眠5秒后，获取网页。防止被发现是爬虫。
    time.sleep(5)
    return html


def printUrl(html):
    ''' 正则表达式规则：src后[]字符类里有^"表示除了“以外的所有字符，后面的+ 表示一个或多个
    用来匹配照片的命名。'''
    p = r'<img class="BDE_Image" src="[^"]+\.jpg"'
    result = re.findall(p, html)
    for i in result:
        print(i[28:])


if '__main__' == __name__:
    url = 'https://tieba.baidu.com/p/6833783429'
    printUrl(getHtml(url))