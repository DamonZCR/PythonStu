from io import SEEK_CUR
from Animal import Animal
import random

#每个Fish的对象都需要一个 name 参数
split = 10
heigh = 10
class Wgui(Animal):
    def __init__(self, name):
        self.life = 30
        self.name = name
        self.x = random.randint(0, split)
        self.y = random.randint(0, heigh)

    def live(self):
        #global self.x, self.y
        if self.life > 0:
            loca = self.wguiMove(self.x, self.y)
            if (self.x != loca[0]) or (self.y != loca[1]):
                self.life -= 1
                self.x = loca[0]
                self.y = loca[1]
            return loca
        else:
            del self
            return (-1, -1)
            #print('I am over!🐢')


'''bb = Wgui('小龟')
xx = Wgui('小乌')
for i in range(15):
    print(bb.live())
    print(xx.live())'''
