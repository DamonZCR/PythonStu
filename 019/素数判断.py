#判断一个数是不是素数
import math

num = int(input('请输入一个正整数：'))
sma = int(math.sqrt(num))
flag = 0

for i in range(2,sma+1):
    if num % i == 0:
        flag = 1
        break 
if flag:
    print('不是素数')
else:
    print('是素数')
