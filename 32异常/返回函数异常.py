def myfun1():
    x = 5
    def myfun2():
        nonlocal x
        x *=x
        return x
    return print(myfun2())

myfun1()
