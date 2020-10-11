from wgui import Wgui
#可以访问导入类的初试变量
#还可以对导入类的初始变量的值进行操作，并且通用
def index():
    bb = Wgui('小二')
    print(bb.name)
    bb.life += 1
    print(bb.life)

    #print((-1, -1)==bb.live())


index()