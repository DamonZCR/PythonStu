#错误程序，__setattr__导致无限调用

class Ractangle:
    def __init__(self, width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        #为某个参数设置属性时发现它属性名为square
        if name == 'square':#长高相等
            self.width = value
            self.heigh = value
        else:
            self.name = value#普通的赋值

    def getArea(self):
        return self.width * self.height
        
