import easygui as g

'''我在easygui的源文件中修改了窗口显示的位置，此文件的路径是：
Python37\Lib\site-packages\easygui\boxes下的global_state.py文件
window_position = "+1320+820"前一个值为水平，后一个为竖直。'''
def showInfo(unlock, lock):
    g.msgbox(msg='锁屏时间：'+lock+'\n上次离开：'+unlock, title='解锁提示')


if '__main__' == __name__:
    showInfo(4,6)