from easygui import*
import sys

if ccbox('要再来一次吗？',choices=('好的','算了')):
    msgbox('不给玩了')
else:
    sys.exit(0)#需要导入sys
    
