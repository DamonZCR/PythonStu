i = 777
num = 0
while i>0:
    # tho = i // 1000
    hun = i // 100
    mid = i // 10 - hun * 10
    bak = i % 10
    if (hun < 8 and mid < 8 and bak < 8):
        if (hun + mid + bak) % 8 == 0:
            print(i)
            num += 1
    i -= 1
print('总数是：',str(num))
    
