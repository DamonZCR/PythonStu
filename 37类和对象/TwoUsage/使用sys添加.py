import sys
# 以下两句意义相同。
sys.path.append(r'D:\PythonPro\FStudy\37类和对象')
# sys.path.insert(r'D:\PythonPro\FStudy\37类和对象')
print(sys.path)
from ImportTest import A

print('使用sys的insert插入搜索路径，测试引用！')
# 调用这个类需要加上括号即实例化，否则出错
A().aPrint()
# 以上类似于这样写。
a = A()
a.aPrint()