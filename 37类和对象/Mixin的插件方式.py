class PlugIn(object):
    def __init__(self):
        self._exported_methods = []
        
    def plugin(self, owner):
        for f in self._exported_methods:
            owner.__dict__[f.__name__] = f

    def plugout(self, owner):
        for f in self._exported_methods:
            del owner.__dict__[f.__name__]

class AFeature(PlugIn):
    def __init__(self):
        super(AFeature, self).__init__()
        self._exported_methods.append(self.get_a_value)

    def get_a_value(self):
        print('a feature.')

class BFeature(PlugIn):
    def __init__(self):
        super(BFeature, self).__init__()
        self._exported_methods.append(self.get_b_value)

    def get_b_value(self):
        print('b feature.')

class Combine:
    pass

c = Combine()
AFeature().plugin(c)
BFeature().plugin(c)

c.get_a_value()
c.get_b_value()
