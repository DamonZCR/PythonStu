#寻找水仙花数
def findFlo():
    from1 = 153
    while from1 < 1000:
        bai = from1 // 100
        shi = from1 // 10 - bai*10
        ge = int((from1 / 10 - from1//10)*10)
        new = pow(bai,3) + pow(shi,3) + pow(ge,3)
        if from1 == new:
            print(from1,end='  ')
        from1 += 1
findFlo()
