num = 100
flag = 0
while num > 0:
    if flag == 1:
        print(num,end=' ')
        flag = 0
    else:
        flag = 1
    num -= 1
