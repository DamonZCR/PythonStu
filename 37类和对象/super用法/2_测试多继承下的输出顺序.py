'''在不使用super进行多继承时，会进行多次访问一个函数'''
class A:
    def fun(self):
        print('A.fun')

class B(A):
    def fun(self):
        A.fun(self)
        print('B.fun')

class C(A):
    def fun(self):
        A.fun(self)
        print('C.fun')

class D(B , C):
    def fun(self):
        B.fun(self)
        C.fun(self)
        print('D.fun')

D().fun()
