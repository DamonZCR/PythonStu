import urllib.request
import time
import re
import os
'''使用正则爬取贴吧图片
（ ）在findall()中的妙用，可以只返回（）里的内容。'''

def getHtml(url):
    # 生成request对象
    res = urllib.request.Request(url)
    # 使用第二种方法add_header()隐藏 py
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/86.0.4240.111 Safari/537.36')
    response = urllib.request.urlopen(res)
    # 网页刚获取的时候是二进制形式或Utf-8，如果对网页进行查找或者分片之类的需要解码成Unicode形式。
    html = response.read().decode('utf-8')
    return html


# 从贴吧地址下载图片
def downPFromUrl(html):
    ''' 正则表达式规则：src后[]字符类里有^"表示除了“以外的所有字符，后面的+ 表示一个或多个
    用来匹配照片的命名。加上()号后，就成了捕获组，捕获组才被保留。'''
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    result = re.findall(p, html)
    for each in result:
        filename = each.split('/')[-1]
        # urlretrieve将文件直接下载过来。
        urllib.request.urlretrieve(each, filename)


if '__main__' == __name__:
    try:
        os.mkdir('D:\\Download')
    except FileExistsError as reason:
        print("异常：此文件夹已存在"+str(reason))
    os.chdir('D:\\Download')

    url = 'https://tieba.baidu.com/p/7138691716'
    downPFromUrl(getHtml(url))