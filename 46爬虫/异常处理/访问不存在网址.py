import urllib.request
import urllib.error

req = urllib.request.Request('http://zlw.com')
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)