class O:
    pass

class A(O):
    def get_a(self):
        print('a')

class B:
    def __init__(self):
        print('这是B的__init__方法')
        self.x = 10
        
    def get_b(self):
        print('b')
