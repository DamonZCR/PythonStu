import math
import numpy

# 需要的参数 维数 d
def calculLange(degree, demen):
    for j in range(demen):
        resUp = 1
        resDown = 1
        for k in range(demen):
            if not k == j :
                resUp *= calE(degree) - calW(demen, k)
                resDown *= calW(demen, j) - calW(demen, k)
        print(resUp / resDown)

            

# cosx + i*sinx 返回 a + b*j的形式
def calE(degree):
    return complex(math.cos(degree), math.sin(degree))

# 计算 w ,其中demn代表维度d ,num代表次方默认设为 1
def calW(denem, num = 1):
    degree = 2 * math.pi * num / denem
    return calE(degree)

if '__main__' == __name__:
    calculLange(math.pi/3, 2)