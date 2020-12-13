# ./代表当前目录      ../代表父级目录       /根目录
import sys, os
print(sys.path)

# sys.path.append(r'D:\PythonPro\FStudy\37类和对象')
sys.path.append(os.path.realpath('..'))

print(sys.path)