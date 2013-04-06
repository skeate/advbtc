from MyFrame import MyFrame
import wx
import wx.lib.mixins.listctrl as listmix
import glbls

class AdvFrame(MyFrame):
  def __init__(self, *args, **kwds):
    MyFrame.__init__(self, *args, **kwds)
    self.addrlist.InsertColumn(0, 'Address')
    self.addrlist.InsertColumn(1, 'Balance', width=100)
    self.addrlist.InsertColumn(2, 'Label', width=100)
    glbls.workQueue.put(('getbalance', self.updateBalance))
    glbls.workQueue.put(('getucbalance', self.updateUCBalance))

  def loadAddresses(self, event):  # wxGlade: MyFrame.<event_handler>
    glbls.workQueue.put(('listaddressgroupings', self.listAddresses))
    self.showAddr.SetLabel('loading...')
    self.showAddr.Enable(False)
    event.Skip()

  def updateBalance(self, data):
    self.cBalance.SetLabel('%.8f' % data)

  def updateUCBalance(self, data):
    self.ucBalance.SetLabel('%.8f' % data)

  def listAddresses(self, data):
    zeroCount = 0
    self.addrlist.DeleteAllItems()
    dictForm = dict(zip(range(len(data)), data))

    self.addrlist.setData(dictForm)
    index = 0
    for key, data in dictForm.items():
      if data[1] == 0 and not self.showZero.IsChecked():
        continue
      zeroCount += 1
      # some addresses do not have labels,
      # so set label field to empty string
      if len(data) == 2:
        data.append("")
      self.addrlist.InsertStringItem(index, data[0])
      self.addrlist.SetStringItem(index, 1, '%.8f' % data[1])
      self.addrlist.SetStringItem(index, 2, data[2])
      self.addrlist.SetItemData(index, key)
    self.addrlist.SortListItems(1, 0)
    self.numAddrs.SetLabel('%d / %d' % (zeroCount, len(dictForm)))
    self.showAddr.SetLabel('Show Addresses')
    self.showAddr.Enable(True)
