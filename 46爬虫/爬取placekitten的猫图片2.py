from http.client import responses
import urllib.request
#urlopen里可以是一个url地址，也可以是一个request对象。
#urlopen里是一个request，1 中的相当于执行了下面两句。

res = urllib.request.Request('http://placekitten.com/200/300')
response = urllib.request.urlopen(res)
image = response.read()
with open('D:/xxx.jpg', 'wb') as f:
    f.write(image)

