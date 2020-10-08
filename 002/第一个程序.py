print("---------第一个测试程序文件----------")
temp = input("猜一下这个数字是几？")
guess = int(temp)
if guess == 8:
    print("成功猜对，牛逼了！")
    print("猜对并没有什么奖励")
else:
    print("猜错了，正确数字是8")
print("游戏结束")
