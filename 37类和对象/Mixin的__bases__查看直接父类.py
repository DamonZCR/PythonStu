class O:
    pass

class A(O):
    def get_a(self):
        print('a')

class B:
    def get_b(self):
        print('b')

class C(A,B): 
    pass

print(A.__bases__)
print(C.__bases__)
