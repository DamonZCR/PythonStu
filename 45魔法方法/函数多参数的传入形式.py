# 一个函数的参数传入如果是多参的，那么传入形式是列表嘛？
# (34, 34, 33, 33, 0, 8)
# <class 'tuple' >元组
#
def valueprint(*arg):
    print(arg)
    print(type(arg))


valueprint(34, 34, 33, 33, 0, 8)
