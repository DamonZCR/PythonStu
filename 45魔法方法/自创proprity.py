#自创property，使用描述符
class MyProperty:
    def __init__(self, fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)#里面的参数可删嘛？不

    def __set__(self, instance, value):
        self.fset(instance,value)
    
    def __delete__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None
    
    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value
    
    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)
    
