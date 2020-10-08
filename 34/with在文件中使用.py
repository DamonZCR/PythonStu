try:
    with open('data.txt','r') as f:
        print(f.read())
except (OSError, TypeError) as reason:
    print('出错啦，出错原因是：'+str(reason))
finally:
    print('f文件的关闭由with监视')