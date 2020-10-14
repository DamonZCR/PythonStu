class A(object):
    def fun(self):
        print('A.fun')

class B(object):
    def fun(self):
        print('B.fun')

class C(object):
    def fun(self):
        print('C.fun')

class D(A,B):
    def fun(self):
        print('D.fun')

class E(B, C):
    def fun(self):
        print('E.fun')

class F(D, E):
    def fun(self):
        print('F.fun')
