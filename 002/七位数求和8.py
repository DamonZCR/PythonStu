i = 7777777
num = 0
while i > 0:
    seven = i // 1000000
    six = i % 1000000 // 100000
    five = i % 100000 // 10000
    four = i % 10000 // 1000 
    three = i % 1000 // 100
    two = i % 100 // 10
    one = i % 10
    if (six < 8 and five < 8 and four < 8 and three < 8 and two < 8 and one < 8):
        if (six + five + four + three + two + one) % 8 == 0:
            #print(i,end='  ')
            num += 1
    i -= 1
print('七位数求解总数是：',str(num))
    
