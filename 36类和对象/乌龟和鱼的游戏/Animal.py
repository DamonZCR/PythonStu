import random
#全局变量
split = 10
heigh = 10

'''在fish类中继承此类，fish实例化的对象去调用这个类的方法，并不会执行__init__方法！'''
class Animal:
    def __init__(self):
        print('Python垃圾')

    #移动类
    def wguiMove(self, x, y):
        #global x,y
        if (x != split and y != split) and (x != 0 and y != 0):
            #决定下一步的步数
            nextstep = random.randint(-2, 2)
            #决定是走水平还是竖直，0是水平，1是竖直。
            choose = random.randint(0, 1)
            if choose == 0:
                g = x
            else:
                g = y

            #对这个方向值进行操作
            if 0 <= g + nextstep <= split:
                g += nextstep
            elif 0 > g + nextstep:
                g = 0
            else :
                g = 10
            #把最终的值交换回来
            if choose == 0:
                x = g
            else:
                y = g
        else:
            if split in (x, y):
                if x == 10:
                    x -= 1
                else:
                    y -= 1
            else:
                if x == 0:
                    x += 1
                else:
                    y += 1
        return x, y

    def fishMove(self, x, y):
        if (x != split and y != split) and (x != 0 and y != 0):
            #决定下一步的步数
            nextstep = random.randint(-1, 1)
            #决定是走水平还是竖直，0是水平，1是竖直。
            choose = random.randint(0, 1)
            if choose == 0:
                g = x
            else:
                g = y

            #对这个方向值进行操作
            if 0 <= g + nextstep <= split:
                g += nextstep
            elif 0 > g + nextstep:
                g = 0
            else:
                g = 10
            #把最终的值交换回来
            if choose == 0:
                x = g
            else:
                y = g
        else:
            if split in (x, y):
                if x == split:
                    x -= 1
                else:
                    y -= 1
            else:
                if x == 0:
                    x += 1
                else:
                    y += 1
        return x, y
    
