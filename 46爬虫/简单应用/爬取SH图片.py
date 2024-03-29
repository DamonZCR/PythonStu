import urllib.request
import re
import os
import urllib.error
'''爬取某网站上的图片，使用模块化获取网页，和获取图片是分开的。使用爬虫的异常处理。
网站服务器具有反爬虫，所以需要加上浏览器标识。
'''

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


def getphoto(url):
    # 生成request对象
    res = urllib.request.Request(url)
    # 使用第二种方法add_header()隐藏 py
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/86.0.4240.111 Safari/537.36')
    response = urllib.request.urlopen(res)
    photo = response.read()
    return photo


# 从网站中的图片地址下载图片
def downPFromUrl(html):
    ''' 正则表达式规则：src后[]字符类里有^"表示除了“以外的所有字符，后面的+ 表示一个或多个
    用来匹配照片的命名。加上()号后，就成了捕获组，捕获组才被保留。'''
    p = r'<img src="([^"]+\.jpg)"'
    result = re.findall(p, html)
    for each in result:
        try:
            filename = each.split('/')[-1]
            photo = getphoto(each)
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a serve.')
                print('Reason:', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code:', e.code)
        else:
            with open(filename, 'wb') as f:
                f.write(photo)


if '__main__' == __name__:
    try:
        os.mkdir('D:\\Download')
    except FileExistsError as reason:
        print("异常：此文件夹已存在"+str(reason))
    os.chdir('D:\\Download')
    url = list()
    url = ['https:/pic/html28/39458.html',
           'https:/pic/html28/39426.html',
           'https:/pic/html28/39453.html']
    # print(url)
    for i in url:
        downPFromUrl(getHtml(i))