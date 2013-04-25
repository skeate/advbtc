import sys
import wx
import wx.lib.mixins.listctrl as listmix
import shelve
import pyperclip
from gui import MainWindow, AboutWindow, SettingsWindow

class SettingsWindowEx(SettingsWindow):
  def __init__(self, parent, queue):
    SettingsWindow.__init__(self, parent)
    self.queue = queue
  def open(self, event):
    settings = shelve.open('settings')
    self.bccloc.SetPath(settings['bitcoin_conf_dir'])
    self.bcdaddr.SetValue(settings['bitcoin_rpc_address'])
    self.useSSL.SetValue(settings['use_ssl'])
    settings.close()
  def saveSettings(self, event):
    settings = shelve.open('settings')
    settings['bitcoin_conf_dir'] = self.bccloc.GetPath()
    settings['bitcoin_rpc_address'] = self.bcdaddr.GetValue()
    settings['use_ssl'] = self.useSSL.GetValue()
    settings.close()
    self.queue.put(('reconnect', self.close))
  def close(self, event):
    self.Close()

class MainWindowEx(MainWindow):
  def __init__(self, queue):
    MainWindow.__init__(self, None)
    self.workQueue = queue

    # set up address events
    self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.enableAddrButtons, self.addrList)
    self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.disableAddrButtons, self.addrList)

    # set up timer to check connection
    # and update balance
    self.timer = wx.Timer(self)
    self.Bind(wx.EVT_TIMER, self.update, self.timer)
    self.timer.Start(0)

  # Timer event
  def update(self, event):
    self.workQueue.put(('beat', self.updatecb))
    self.timer.Start(1000)
    event.Skip()
  def updatecb(self, data):
    if data is False:
      self.sb.SetStatusText('Connection error.')
      self.cBalance.SetLabel('connection error')
      self.ucBalance.SetLabel('connection error')
    else:
      self.sb.SetStatusText(
          'Connected to server (%d connections to network)'
          % data['connections'])
      self.cBalance.SetLabel('%.8f' % data['balance'])
      self.ucBalance.SetLabel('%.8f' % ( data['ubalance'] - data['balance'] ))

  # Menubar events
  def menu_exit(self, event):
    sys.exit()

  def menu_about(self, event):
    AboutWindow(wx.GetApp().TopWindow).Show()

  def menu_settings(self, event):
    SettingsWindowEx(wx.GetApp().TopWindow, self.workQueue).Show()

  # Address Panel events
  def enableAddrButtons(self, event):
    self.newTxBtn.Enable(True)
    self.copyAddrBtn.Enable(True)
    event.Skip()

  def disableAddrButtons(self, event):
    self.newTxBtn.Enable(False)
    self.copyAddrBtn.Enable(False)
    event.Skip()

  def copyAddress(self, event):
    addressRow = self.addrList.GetFirstSelected()
    address = self.addrList.GetItem(addressRow, 0).GetText()
    pyperclip.copy(address)

  def createAddress(self, event):
    self.workQueue.put(('create address', self.createAddressCB))
    event.Skip()
  def createAddressCB(self, data):
    print data

  def listAddresses(self, event):
    self.workQueue.put(('get addresses', self.listAddressesCB))
    self.showAddr.SetLabel('loading...')
    self.showAddr.Enable(False)
    event.Skip()
  def listAddressesCB(self, data):
    zeroCount = 0
    self.addrList.DeleteAllItems()
    dictForm = dict(zip(range(len(data)), data))
    self.addrList.setData(dictForm)
    index = 0
    for key, data in dictForm.items():
      if not self.showAll.IsChecked() and data[1] == 0:
        if not self.showLabeled.IsChecked() or data[2] == '':
          continue
      zeroCount += 1
      # some addresses do not have labels,
      # so set label field to empty string
      if len(data) == 2:
        data.append("")
      self.addrList.InsertStringItem(index, data[0])
      self.addrList.SetStringItem(index, 1, '%.8f' % data[1])
      self.addrList.SetStringItem(index, 2, data[2])
      self.addrList.SetItemData(index, key)
    self.addrList.SortListItems(1, 0)
    self.numAddrs.SetLabel('%d / %d' % (zeroCount, len(dictForm)))
    self.showAddr.SetLabel('Show Addresses')
    self.showAddr.Enable(True)

