
'''
利用有道翻译进行在线翻译
'''

import urllib.request
import urllib.parse
import json

targetURL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

data = {}
data['i'] = 'PIG'
data['from'] =  'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '16028975973203'
data['sign'] = '6b534b3a7875f70ed5b4a8ee39091ef2'
data['lts'] = '1602897597320'
data['bv'] = '4abf2733c66fbf953861095a23a839a8'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data = urllib.parse.urlencode(data).encode('utf-8')

html = urllib.request.urlopen(targetURL, data)
# 读取并解码内容
rst = html.read().decode("utf-8")
target = json.loads(rst)
print(target['translateResult'][0][0]['tgt'])
