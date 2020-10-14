class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(A,B):
    pass

class E(B, C):
    pass

class F(D, E):
    pass

print(F.__mro__)
