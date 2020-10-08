temp = input('请输入年数:')

# isdigit 测试出字符串是否都是数字
while not temp.isdigit():
    temp = input('输入类型错误，请重新输入：')
num = int(temp)
print(type(num))
