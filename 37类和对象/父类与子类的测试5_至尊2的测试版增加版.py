import random as r

class Animal:
    def __init__(self):
        print('午晴')
        self.agree = '是的'
        
    def live(self):
        print('活着最重要,%s'%self.agree)
        
class Fish(Animal):
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        super().__init__()

    def move(self):
        self.x -= 1
        print('我的位置是：',self.x, self.y)
        
class Sharp(Fish):
    def __init__(self):#此方法会覆盖父类的方法
        super().__init__()#使用super()

    def eat(self):
            print('吃货的梦想就是天天有的吃！')

