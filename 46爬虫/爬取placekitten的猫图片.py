from http.client import responses
import urllib.request
#urlopen里可以是一个url地址，也可以是一个request对象。
#是一个request的方式参见二。当前的这个方法相当于执行了2 的两句。

response = urllib.request.urlopen('http://placekitten.com/200/300')
image = response.read()
with open('D:/xx.jpg','wb') as f:
    f.write(image)
