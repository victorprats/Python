# https://pypi.org/project/win10toast/
# pip install win10toast

from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Hello !!!", "This is a notification for you.", icon_path=None, duration=10)
