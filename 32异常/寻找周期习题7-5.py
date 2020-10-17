num = int(input('输入底数a：'))
Mnum = int(input('输入M：'))
print('计算周期中ing...')

r = 1
while r <= Mnum:
    if ((num**r)%Mnum) == 1:
        print('周期为：%d'%r)
        break
    r +=1
else:
    print('未找到')
