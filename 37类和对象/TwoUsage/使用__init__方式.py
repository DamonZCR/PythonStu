'''使用跨包引用成功。
为什么是这个文件可以调用test.ImportTest文件呢？
在运行这个文件是，系统将总项目路径 和 这个文件所在的文件夹路径加入到系统路径。
所以如果是同路径下的文件引用就直接引用好了。如果不是，就需要从上述路径开始接着加上
想要引用文件的路径。如系统已经有了这个文件TwoUsage的路径，在使用test.ImportTest
就够了。'''
from test.ImportTest import A

a = A()
a.aPrint()
