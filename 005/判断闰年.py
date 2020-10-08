temp = input('请输入年数:')

# isdigit 测试出字符串是否都是数字
# 当输入全是数字时重新输入
while not temp.isdigit():
    temp = input('输入类型错误，请重新输入：')
num = int(temp)

# 数字类型不能直接用+号 与字符串相连输出
# py中+号两种用处：1、数学运算 2、仅字符串链接
if (num % 4 == 0)and(num % 100 != 0):
    print(str(num)+'是闰年')
elif num % 400 == 0:
    print(str(num)+'是闰年')
else:
    print(str(num)+'不是闰年')
