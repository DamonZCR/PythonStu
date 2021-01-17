'''列表中的单个元素被打包成可以分开的两个个体，就可以使用第一种的for循环分配两个值，
否则会报错误：ValueError: too many values to unpack (expected 2)。2-如果使用元组打包
也是可以的，如第二种。'''
lang = ['dd','bb','ee']
for one, two in lang:
    print(one,two)

lang2 = [('dd', 1),('bb', 2),('ee', 3)]
for one, two in lang2:
    print(one,two)