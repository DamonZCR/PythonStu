flag = 0
squre = 2
while (squre <= 100)and flag ==0:
    gue = 7*squre
    if gue % 2 == 1:
        if gue % 3 == 2:
            if gue % 5 == 4:
                if gue % 6 == 5:
                    print('阶梯最少为：',gue)
                    flag = 1
    squre += 1
