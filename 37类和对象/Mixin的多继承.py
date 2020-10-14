class A:
    def get_a(self):
        print('a')

class B:
    def get_b(self):
        print('b')

class C(A, B): 
    pass

c = C()
c.get_a()
c.get_b()
