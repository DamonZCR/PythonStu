try:
    f = open('d:/不存在文件.txt','r',encoding='UTf-8')
    print(f.write('末尾追加上我哦。'))
    sum = 1 + '1'
except (OSError,TypeError) as reason:
    print('出错啦，出错原因是：'+str(reason))
finally:
    f.close()
