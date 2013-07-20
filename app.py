"""
app.py

Runs advbtc
"""
import wx
import gettext
from MainWindowEx import MainWindowEx
from BitcoinThread import BitcoinThread
from Queue import Queue

work_queue = Queue()

if __name__ == "__main__":
    gettext.install("advbtc")

    btc = BitcoinThread(work_queue)
    btc.setDaemon(True)
    btc.start()

    app = wx.App(False)
    frame_1 = MainWindowEx(None, work_queue)
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
