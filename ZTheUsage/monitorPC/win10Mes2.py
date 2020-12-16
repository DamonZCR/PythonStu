from win10toast import ToastNotifier
import time


def win10Mes2(unlocktime, locktime):
    toaster = ToastNotifier()
    # 采用自己的线程,这里图标不能使用相对路径，因为UseCemera.py已经更改路径。
    toaster.show_toast("解锁提示",
                       "锁定时间："+locktime+"\n解锁时间："+unlocktime,
                       icon_path=r"D:\PythonPro\FStudy\ZTheUsage\monitorPC\damon.ico",
                       duration=10,
                       threaded=True)

    # 等待提示框关闭
    while toaster.notification_active(): time.sleep(0.1)
