"""先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性。
要求两个属性会自动转换，也就是说你可以给摄氏度这个属性赋值，
然后打印的华氏度属性是自动转换摄氏度后的结果。"""
class Sheshi:
    def __init__(self, value = 26.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)
    
class Huashi:
    def __init__(self):
        pass
    def __get__(self, instance, owner):
        return instance.she * 1.8 + 32   
    def __set__(self, instance, value):
        instance.she = (float(value) - 32) / 1.8

class Temperature:
    she = Sheshi()
    hua = Huashi()

