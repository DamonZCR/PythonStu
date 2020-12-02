# 用于测试文件 使用__init__方式.py的跨包引用
class A:
    def aPrint(self):
        print('A类访问，欢迎访问~')
class B:
    def bPrint(self):
        print('B类访问，欢迎访问！')
def atest():
    print('调用atest()方法，测试成功！')