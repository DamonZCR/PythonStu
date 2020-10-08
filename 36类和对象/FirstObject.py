 #Py中的类名约定为以大写字母开头
class Turtle:
    '''关于类的一个简单例子'''
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    #方法
    def climb(self):
        print('向前爬。。。。')

    def run(self):
        print('向前跑。。。')
    
    def eat(self):
        print('使劲吃。。。')

    def sleep(self):
        print('尽情睡。。。')
