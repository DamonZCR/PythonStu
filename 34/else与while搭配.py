def showMaxFactor(num):
    # 这个地方一定是使用 // 号，而不是一个 / 号
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是：%d'%(num,count))
            break
        count -= 1
    else:
        print('%d是素数！'%num)


num = int(input('请输入一个数：'))
showMaxFactor(num)