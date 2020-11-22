import urllib.request
import urllib.error

req = urllib.request.Request('https://www.baidu.com/zlw')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
    print(e.read().decode('utf-8'))