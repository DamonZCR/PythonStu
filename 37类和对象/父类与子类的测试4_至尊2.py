import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('我的位置是：',self.x, self.y)
        
class Carp(Fish):
    pass

class Sharp(Fish):
    def __init__(self):#此方法会覆盖父类的方法
        super().__init__()#使用super（）
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃！')
            self.hungry = False
        else:
            print('我吃饱了')
