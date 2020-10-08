def count(*temp):
    how = 1
    for i in temp:
        squ = int()
        num = int()
        spa = int()
        oth = int()
        for j in i:
            if (j >= 'a' and j <= 'z')or(j >= 'A' and j <= 'Z'):
                squ += 1
            elif(j >= '0' and j <= '9'):
                num += 1
            elif j == ' ':
                spa += 1
            else:
                oth += 1
        print('第%d个字符串共有：英文字母%d个,数字%d个,空格%d个,其他字符%d个'%(how,squ,num,spa,oth))
        how += 1
count('kdfa;j309fjal;sdkf','jdfa asd ff asdfaslkdf093')
