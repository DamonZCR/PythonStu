'''发现：
    使用sys加入路径时，就将此路径加到查找路径中，而如果此文件夹也就是目标文件夹37类和对象
    已经被Mask成Sourse Root文件夹，即在PyCharm看这个文件夹不是灰色而是蓝色。就不需要再使用
    sys.append()方法添加。
'''
import sys
# 以下两句意义相同。
sys.path.append(r'D:\PythonPro\FStudy\37类和对象')
# sys.path.insert(r'D:\PythonPro\FStudy\37类和对象')
# 以上添加路径的改进版，即添加相对路径看拓展文件中的讲解。

print(sys.path)
from Importex import A

print('使用sys的insert插入搜索路径，测试引用！')
# 调用这个类需要加上括号即实例化，否则出错
A().aPrint()
# 以上类似于这样写。
a = A()
a.aPrint()