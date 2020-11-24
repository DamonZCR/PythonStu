import urllib.request
import os
import time
'''此程序实现，下载煎蛋网的网页，并且获得当前页的下一页的地址。
getHtml()实现获得这个url 的HTML 文件，其中使用sleep(),使线程睡眠5秒钟，防止短时间内访问。
getNextUrl()实现煎蛋网这个Html文件里，固定位置的下页的url 地址
downphoto()函数将Html保存下来，并且输出下页的地址。
这里有个知识点：写入文件需要用到UTF-8，而getNextUrl()分割时需要用到Unicode。'''


# 参数定义为图片保存路径folder，及下载网页的多少页图片。
def downphoto(folder='D:\Download'):
    # 如果文件夹已经存在会抛出异常，但仍会正常执行。
    try:
        os.mkdir(folder)
    except FileExistsError as reason:
        print("此文件夹已存在"+str(reason))
    os.chdir(folder)

    # 获取这个网页
    indexUrl = 'http://jandan.net/ooxx'
    html = getHtml(indexUrl)
    # encode()转成UTF-8的格式
    html = html.encode('utf-8')
    with open(folder + '\\xx.html', 'wb') as f:
        f.write(html)
    print(getNextUrl(html))


# 获取当前页面的下一页的地址。
def getNextUrl(html):
    # 将html的utf-8格式decode转成UniCode格式。否则出错。
    html = html.decode('utf-8')
    # 加上22正好到下一页地址的位置
    begin = html.find('Older Comments') + 22
    # find()方法里可以带有从何处开始的起始点。
    end = html.find('previous-comment-page', begin) - 9
    return html[begin:end]


# 获得这个url 的HTML 文件。
def getHtml(url):
    # 生成request对象
    res = urllib.request.Request(url)
    # 使用第二种方法add_header（）隐藏 py
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/86.0.4240.111 Safari/537.36')
    response = urllib.request.urlopen(res)
    html = response.read().decode('utf-8')
    # 线程睡眠5秒后，获取网页。防止被发现是爬虫。
    time.sleep(5)
    return html


if __name__ == '__main__':
    downphoto()
