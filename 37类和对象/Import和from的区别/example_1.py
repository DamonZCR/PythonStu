'''发现：
    使用sys加入路径时，就将此路径加到查找路径中，而如果此文件夹也就是目标文件夹37类和对象
    已经被Mask成Sourse Root文件夹，即在PyCharm看这个文件夹不是灰色而是蓝色。就不需要再使用
    sys.append()方法添加。

   目的：
    这里使用ImportTest.py中的atest方法，书写方式就是从文件中导入这个方法名，如果使用类，就是从文件
    中import 类名（记得实例化）。导入方法就可以用方法名直接使用，只导入文件也可以。
'''
import sys
sys.path.append(r'D:\PythonPro\FStudy\37类和对象')
print(sys.path)

from Importex import atest
# import ImportTest
atest()
