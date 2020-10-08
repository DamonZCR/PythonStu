def make_re(n):
    return lambda s : s * n

double = make_re(2)
print(double(8))
print(double('zlw  '))
