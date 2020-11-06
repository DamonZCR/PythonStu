import urllib.request
#未知错误导致每次返回的都是自己的IP地址
#可能是代理服务器无法使用。

url = 'http://45.32.164.128/ip.php'

#daili = {'https': '222.37.125.26:32221', 'https': '175.18.27.42:42221' }
proxy_support = urllib.request.ProxyHandler({'http:':'123.56.75.226:3128'})

opener = urllib.request.build_opener(proxy_support)
opener.add_header = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36')]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('UTF-8')

print(html[297:315])
