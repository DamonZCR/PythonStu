import random
secret = random.randint(1,10)
print("---------第一个测试程序文件----------")
temp = input("猜一下这个数字是几？")
guess = int(temp)
num = 3

# 随机数产生
while guess != secret:
    if guess == secret:
        print("成功猜对，牛逼了！")
        print("猜对并没有什么奖励")
    else:
        if guess < secret:
            print("小了\n")
        else:
            print("大了\n")
    temp = input("猜一下这个数字是几？")
    guess = int(temp)
    num = num -1
print("本次游戏结束")
