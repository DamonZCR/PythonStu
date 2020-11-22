python3中urllib.request模块提供的urlretrieve()函数。urlretrieve()方法直接将远程数据下载到本地。

urlretrieve(url, filename=None, reporthook=None, data=None)

    参数url：下载链接地址
    参数filename：指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
    参数reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
    参数data：指post到服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头