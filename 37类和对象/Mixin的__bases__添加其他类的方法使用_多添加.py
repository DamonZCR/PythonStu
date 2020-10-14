class O:
    pass

class A:
    def get_a(self):
        print('a')

class B:
    def get_b(self):
        print('b')
class C(O):
    pass
      
C.__bases__ +=(A,B,)
c = C()
c.get_b()
c.get_a()
