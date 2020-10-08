# 使用了elif的简洁性


temp = input('请输入一个分数:')
score = int(temp)
if 100>= score >= 90:
    print('成绩为A')
elif 89 >= score >= 80:
    print('成绩为B')
elif 79 >= score >= 70:
    print('成绩为C')
elif 69 >= score >= 0:
    print('成绩为D')
else:
    print('输出错误')
