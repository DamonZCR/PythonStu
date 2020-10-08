import random

def guessnum():
    try:
        temp = input("猜一下这个数字是几？")
        guess = int(temp)

        # 随机数产生
        while guess != secret:
            if guess < secret:
                print("小了\n")
            else:
                print("大了\n")
            temp = input("猜一下这个数字是几？")
            guess = int(temp)
    except ValueError as reason:
        print('出错啦！输入值非纯数字哦;'+str(reason))
        guessnum()
    except (EOFError,KeyboardInterrupt) as reason:
        print('组合键输入错误！'+str(reason))
        guessnum()
    
secret = random.randint(1,10)
print("---------第一个测试程序文件----------")
guessnum()
print('恭喜你猜对了')
print("本次游戏结束")
