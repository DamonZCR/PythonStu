class A:
    def fun(self):
        print('A.fun')

class B(A):
    def fun(self):
        super(B , self).fun()
        print('B.fun')

class C(A):
    def fun(self):
        super(C , self).fun()
        print('C.fun')

class D(C , B):
    def fun(self):
        super(D , self).fun()
        print('D.fun')

D().fun()
