def int_put():
        try:
            num = int(input('请输入一个整数：'))
        except ValueError:
            print('出错，您输入的不是一个整数！')
            int_put()

int_put()
