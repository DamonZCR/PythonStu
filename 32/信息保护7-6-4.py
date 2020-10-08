import sys
numc = int(input('请输入x寄存器中的 c :'))
num = int(input('输入x寄存器的比特位数 m :'))
intM = int(input('输入待分解的数 M :'))

oneM = 1
downum = 2**num
while oneM < intM:
    i = 1
    while i < oneM:
        juedui = abs((numc/downum) - (i/oneM))
        if juedui < (1/(2*downum)):
            print('仅有的分式为：%d/%d'%(i,oneM))
            #sys.exit(0) 
        i +=1
    oneM +=1
