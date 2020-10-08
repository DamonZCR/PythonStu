#寻找水仙花数
def findFlo():
    from1 = 153
    #while from1 < 1000:
    bai = from1 // 100
    print('计算出来的百位是bai = %d',bai)
    shi = from1 // 10 - bai*10
    print('计算出来的十位是shi = %d',shi)
    ge = (from1 / 10 - from1//10)*10
    print('计算出来的个位是ge = %d',ge)
    new = pow(bai,3) + pow(shi,3) + pow(ge,3)
    print('计算出来的新数是new = %d',new)
    if from1 == new:
        print(from1,end='  ')
    from1 += 1
findFlo()
