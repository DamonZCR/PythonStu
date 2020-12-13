'''这里再使用__init__的方式下，进行__init__文件
提前准备包内需要被引用的各个模块中的变量，类似于向外部引用者暴露包内接口。
即在需要引用的文件所在的__init__文件中，提供出方便的调用类接口。
已在此文件中书写数接口 A 类 ,这里只需加上包名即可。'''
from test import A
from test.ImportTest import B

a = A()
a.aPrint()

B().bPrint()