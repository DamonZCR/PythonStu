import random
import easygui as g

def guessnum():
    guess = g.integerbox('不妨猜一下我现在在想那个数字吧（1-10）？','猜数字小游戏',upperbound=10) 
    while guess != secret:
        if guess < secret:
            guess = g.integerbox('小了（1-10）？',
                                 '猜数字小游戏', upperbound=10)
        else:
            guess = g.integerbox('大了（1-10）？',
                                '猜数字小游戏', upperbound=10)
    g.msgbox('恭喜你猜对了！','恭喜')

secret = random.randint(1, 10)
print("---------第一个测试程序文件----------")
guessnum()
print("本次游戏结束")
