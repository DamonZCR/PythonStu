from Animal import Animal
import random

split = 10
heigh = 10
#每个Fish的对象都需要一个 name 参数
class Fish(Animal):
    def __init__(self, name):
        self.name = name
        self.x = random.randint(0, split)
        self.y = random.randint(0, heigh)
    
    def live(self):
        loca = self.fishMove(self.x, self.y)
        self.x = loca[0]
        self.y = loca[1]
        return loca

    def setliveval(self):
        del self
        '''print('我是%s,我的坐标是：%s'%(self.name, str(self.fishMove())))
        del self
        print('I am over!')'''

'''bb = Fish('小三')
for i in range(15):
    print(bb.live())'''

 


 
