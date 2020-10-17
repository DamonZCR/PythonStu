#求出抽奖箱里的唯一一个一等奖。

astr = input()
it = iter(astr)
x = len(astr)
strs = next(it)
while x > 0:

    if astr.count(strs) == 1:
        print(strs)
        break
    x -=1
    strs = next(it)
