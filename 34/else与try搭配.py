try:
    int('123')
except ValueError as reason:
    print('出错啦'+str(reason))
else:
    print('没有出现异常！')