#使用super调用父类的方法进行
class Ractangle:
    def __init__(self, width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':#长高相等
            self.width = value
            self.heigh = value
        else:
            super().__setattr__(name, value)

    def getArea(self):
        return self.width * self.height
        
