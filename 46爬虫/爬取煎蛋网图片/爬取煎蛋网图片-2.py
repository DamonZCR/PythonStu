import urllib.request
import os
import time
'''使用模块化实现爬取此网站的美女图片。
从当前页面查找获取下一页的地址，保存当前页面，记录当前页面内的图片地址，保存图片'''

# 参数定义为图片保存路径folder，及下载网页的多少页图片。
def downphoto(folder='D:\Download', page=2):
    # 如果文件夹已经存在会抛出异常，但仍会正常执行。
    try:
        os.mkdir(folder)
    except FileExistsError as reason:
        print("此文件夹已存在" + str(reason))
    os.chdir(folder)

    # 目标地址
    indexUrl = 'http://jandan.net/ooxx'
    for i in range(page):
        # 获取网页，获取下一页的地址
        # 注意这里只有将网页转换为Unicode形式才可以进行分片操作。
        html = getHtml(indexUrl).decode('utf-8')
        indexUrl = 'http:' + getNextUrl(html)
        # 对findphoto() 返回的当前页面的所有图片地址进行保存
        savephoto(findphoto(html))


# 找到网页中的图片地址
def findphoto(html):
    # 存放当前页面里图片的链接地址
    photoadd = []
    # 当find() 未找到时才会返回 -1
    begin = html.find('<img src=')
    while begin != -1:
        end = html.find(".jpg", begin, begin + 225)
        if end != -1:
            photoadd.append(html[begin + 10:end + 4])
        else:
            end = begin + 10
        begin = html.find('<img src=', end)
    return photoadd


# 下载图片
def savephoto(photoadd):
    for one in photoadd:
        addr = 'http:' + one
        # 列表中，[-1]代表最后一项。
        filename = one.split('/')[-1]
        # 需要二进制写入
        with open(filename, 'wb') as f:
            photo = getHtml(addr)
            f.write(photo)


# 获取当前页面的下一页的地址。
def getNextUrl(html):
    # 加上22正好到下一页地址的位置
    begin = html.find('Older Comments') + 22
    end = html.find('previous-comment-page', begin) - 9
    return html[begin:end]


def getHtml(url):
    # 生成request对象
    res = urllib.request.Request(url)
    # 使用第二种方法add_header()隐藏 py
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/86.0.4240.111 Safari/537.36')
    response = urllib.request.urlopen(res)
    html = response.read()
    # 线程睡眠5秒后，获取网页。防止被发现是爬虫。
    time.sleep(5)
    return html


if __name__ == '__main__':
    downphoto()
