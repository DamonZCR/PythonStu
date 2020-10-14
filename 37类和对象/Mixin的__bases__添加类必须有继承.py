class A(object):
    def get_a(self):
        print('a')

class B:
    def get_b(self):
        print('b')
A.__bases__ +=(B,)
a = A()
a.get_b()
