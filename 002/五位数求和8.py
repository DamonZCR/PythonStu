i = 77777
num = 0
while i > 0:
    five = i // 10000
    four = i // 1000 - five * 10
    three = i // 100 - four * 10 - five * 100
    two = i // 10 - three * 10 - four * 100 - five * 1000
    one = i % 10
    if (five < 8 and four < 8 and three < 8 and two < 8 and one < 8):
        if (five + four + three + two + one) % 8 == 0:
            print(i,end='  ')
            num += 1
    i -= 1
print('总数是：',str(num))
    
