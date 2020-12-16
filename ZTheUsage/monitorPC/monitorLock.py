# 检测windows锁屏和解锁的事件时间
import sys
import time
import UseCemera
import win10Mes2
from PyQt5.QtWidgets import *
import win32api
import win32con
import win32gui
import win32ts


WM_WTSSESSION_CHANGE = 0x2B1
WTS_SESSION_LOCK = 0x7
WTS_SESSION_UNLOCK = 0x8


class WndProcHookMixin:
    def __init__(self):
        self.msgDict = {}

    def hookWndProc(self):
        self.oldWndProc = win32gui.SetWindowLong(self.winId(), win32con.GWL_WNDPROC, self.localWndProc)

    def unhookWndProc(self):
        win32api.SetWindowLong(self.winId(), win32con.GWL_WNDPROC, self.oldWndProc)

    def addMsgHandler(self, messageNumber, handler):
        self.msgDict[messageNumber] = handler

    def localWndProc(self, hWnd, msg, wParam, lParam):
        if msg in self.msgDict:
            if not self.msgDict[msg](wParam, lParam):
                return

        if msg == win32con.WM_DESTROY:
            self.unhookWndProc()

        return win32gui.CallWindowProc(self.oldWndProc, hWnd, msg, wParam, lParam)


class Window(QWidget, WndProcHookMixin):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        # self.show()
        win32ts.WTSRegisterSessionNotification(self.winId(), win32ts.NOTIFY_FOR_ALL_SESSIONS)
        self.addMsgHandler(WM_WTSSESSION_CHANGE, self.on_session)
        self.hookWndProc()

    def on_session(self, wParam, lParam):
        event, session_id = wParam, lParam
        global locktime
        if event == WTS_SESSION_LOCK:
            print("Locked")
            locktime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event == WTS_SESSION_UNLOCK:
            print("Unlocked")
            unlocktime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            UseCemera.takephoto()
            win10Mes2.win10Mes2(unlocktime, locktime)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())