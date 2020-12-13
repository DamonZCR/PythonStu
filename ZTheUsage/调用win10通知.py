from win10toast import ToastNotifier
toast = ToastNotifier()
# 这个图标是win10系统自带的。
toast.show_toast(title="This is a title", msg="This is a message",
                 icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)