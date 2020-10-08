print("---------第一个测试程序文件----------")
temp = input("猜一下这个数字是几？")
num = 3

# 输入 e 退出 三次比较
while temp != 'e' and num != 1:
    guess = int(temp)
    if guess == 8:
        print("成功猜对，牛逼了！")
        print("猜对并没有什么奖励")
    else:
        if guess <8:
            print("小了")
        else:
            print("大了")
    num = num -1
    temp = input("猜一下这个数字是几？")
print("本次游戏结束")
