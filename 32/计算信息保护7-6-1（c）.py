allc = list(range(0,8))
j = 0

for c in allc:
    while c > j:
        if 1/2 >= abs(c - j*(8/3)):
            print('j值为：'+str(j)+', c值为：'+str(c))
            break
        j +=1
    j = 0
