import hashlib
'''md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256

Hash objects have these methods:
 - update(data): 用数据中的字节更新哈希对象。重复调用相当于将所有参数串联在一起的单个调用。可以用于加盐，即对这个字符串继续添加字符。
 - digest():     Return the digest of the bytes passed to the update() method
                 so far as a bytes object.就是返回一个二进制的消息摘要。
 - hexdigest():  Like digest() except the digest is returned as a string
                 of double length, containing only hexadecimal（十六进制的） digits.字符串形式的摘要
 - copy():       Return a copy (clone) of the hash object. This can be used to
                 efficiently compute the digests of datas that share a common
                 initial substring.返回哈希对象的副本（克隆）。这可以用来有效地计算共享一个公共初始子串的数据摘要。
'''

mess = 'wocaowuqing!'
print(hashlib.md5(mess.encode()).hexdigest())
print(hashlib.sha1(mess.encode()).hexdigest())