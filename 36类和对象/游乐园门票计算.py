class Ticket:
    def __init__(self, weekend=False, child=False):
        self.cost = 100
        if weekend :
            self.expen = 1.2
        else:
            self.expen = 1
        if child :
            self.count = 0.5
        else:
            self.count = 1
    def comput(self):
        return self.cost*self.count*self.expen
