i = 100
while i < 1000:
    bai = i // 100
    shi = i //10 - bai*10
    ge = i % 10
    if(bai**3 + shi**3 + ge**3 == i):
        print(i,end=' ')
    i +=1 
