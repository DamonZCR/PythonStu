'''可能与检测开锁冲突，不能使用win10通知'''
from win10toast import ToastNotifier


def win10Mes(unlock, lock):
    toast = ToastNotifier()
    toast.show_toast(title="解锁提示", msg='锁屏时间：'+lock+'\n上次离开：'+unlock,
                    icon_path="damon.ico", duration=10)


if '__main__' == __name__:
    win10Mes('44','66')