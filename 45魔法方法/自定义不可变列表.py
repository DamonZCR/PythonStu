"""自定义一个列表类，列表不可以被改变，并可以可以访问，
列表中的元素被访问的次数"""
class Newlist:
    def __init__(self, *arg):
        self.array = [x for x in arg]
        self.adict = {}.fromkeys(range(len(arg)), 0)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        self.adict[key] +=1
        return self.array[key]
