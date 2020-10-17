#判断一个数是不是素数
import math

big = int(input('请输入一个正整数：'))
#素数个数
sunum = 1
flag = 1
for num in range(3,big):
    sma = int(math.sqrt(num))
    for i in range(2,sma+1):
        if num % i == 0:
            flag = 0
            break 
    if flag:
        sunum +=1
    flag = 1

print(sunum)
