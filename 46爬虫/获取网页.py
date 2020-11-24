from http.client import responses
import urllib.request

response = urllib.request.urlopen('https://weibo.com')
html = response.read()
with open('D:\\Download\\xx.html', 'wb') as f:
    f.write(html)

# 这个地方需要加上‘ignore’参数，否则报：utf-8' codec can't decode byte 0xca in position 94: invalid continuation byte
# 主要问题是 在二进制转换中出错，所以对不能转换加上忽略。
print(html.decode('utf-8', 'ignore'))